from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
import json
from django.contrib.auth import get_user_model, authenticate, login, logout


def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})

def ping(request):
    if request.method == 'GET':
        return JsonResponse({'result': 'Got'})
    else:
        # print(request.headers)
        return JsonResponse({'result': 'Posted'})

def login_view(request):
    data = json.loads(request.body)
    username = data['username']
    password = data['password']

    if username is None or password is None:
        return JsonResponse({'result': 'Please provide username and password.'}, status=400)

    user = authenticate(username=username, password=password)

    if not user:
        JsonResponse({'result' : 'Invalid Credentials'}, status=400)

    login(request, user)
    return JsonResponse({'result': "SuccesFully Logged In"})

@ensure_csrf_cookie
def session_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': False})

    return JsonResponse({'isAuthenticated': True})

def logout_view(request):
    print(request.user)
    if not request.user.is_authenticated:
        return JsonResponse({'result': 'You\'re not logged in.'}, status=400)

    logout(request)
    return JsonResponse({'result': 'Successfully logged out.'})