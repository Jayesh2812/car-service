import {Cookies} from 'react-cookie'

const API_HOST = 'http://localhost:8000';

export async function POST (url, post_data) {

    const response = await fetch(`${API_HOST}/${url}/`, {
    method : 'POST',
    headers: ({
          'X-CSRFToken': await getCsrfToken(),
        }
      ),
    credentials: 'include',
    body : JSON.stringify(post_data)
    });
    const data = await response.json();
    return data.result;
}

export async function GET (url) {
    const response = await fetch(`${API_HOST}/${url}/`, {
      headers: ({ }),
      credentials: 'same-origin'
    });
    const data = await response.json();
    return data.result;
}

export async function getCsrfToken() {
    let _csrfToken = null;
    let cookies = new Cookies()

    if (_csrfToken === null) {
      const response = await fetch(`${API_HOST}/csrf/`, {
        // credentials: 'include',
      });
      const data = await response.json();
      _csrfToken = data.csrfToken;
      cookies.set('csrftoken',_csrfToken)
    }
    return _csrfToken;
  }

