import { POST } from "./Fetch"
import {Cookies} from 'react-cookie'

const LOGIN_URL = 'login'
const LOGOUT_URL = 'logout'

export async function login (username, password, type){
    // const [{user}, dispatch] = useStateValue()
    
    let user = await POST(LOGIN_URL,{username, password, type})
    return user
        
}

export async function logout(){

    let result = await POST(LOGOUT_URL,{})
    console.log(result)
}

export function checkLogin(){
    let cookies = new Cookies()
    let user = cookies.get('user')
    return user
}