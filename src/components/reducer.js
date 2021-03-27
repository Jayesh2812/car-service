import {Cookies} from 'react-cookie'
export const initialState = {
    user : null
}

function reducer(state, action){
    switch(action.type){
        case "SET_USER":
            let cookies = new Cookies()
            cookies.set("user",action.user)
            return { 
                ...state,
                user : action.user
            }      

        default:
            return state
    }
}

export default reducer