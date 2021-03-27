import '../css/App.css';

import {useEffect, useState} from 'react'
import { useStateValue } from './StateProvider';
import { GET , POST} from './Fetch';
import { login, logout, checkLogin} from './auth';
import {Signin} from './Signin.js'
import {Signup} from './Signup.js'


function App() {
  const [testGet, setTestGet] = useState("NO")
  const [testPost, setTestPost] = useState("NO")

  const [{user}, dispatch] = useStateValue()

  const authLogin = ()=>{
    login('admin', 'admin', 'passenger').then(authuser => {
      if (authuser){  
        dispatch({
          type:'SET_USER',
          user : authuser
        })
      }
      
    })
  }
  const authLogout = ()=>{
    logout()
    dispatch({
      type:'SET_USER',
      user : null
    })
  }
  useEffect(() => {
    GET('ping').then(data=>{setTestGet(data)})
    POST('ping',{name:'Jayesh'}).then(data=>{setTestPost(data)})

    let authUser = JSON.stringify(checkLogin())
    if (authUser !== 'null')
      dispatch({type:"SET_USER", user:authUser})
    else
      dispatch({type:"SET_USER", user:null})


    
  },[user]);

  return (
    <div className="App">
      {/* <h1>Jayesh</h1>
      <div>
        <p>Test GET request: {testGet}</p>
        <p>Test POST request: {testPost}</p>
        <p>User : {user}</p>
        <button onClick={authLogin}>Login</button>
        <button onClick={authLogout}>Logout</button>
      </div> */}
      <Signup/>
    </div>
  );
}

export default App;
