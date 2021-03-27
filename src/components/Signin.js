import React from 'react'

export const Signin = () => {
    return (
        <div className="signin">
            <h2>Welcome Back</h2>
            <form>
            <input type="text" placeholder="Username" required/>
            <input type="password" placeholder="Password" required/>
            <a href="#"><h6 className="Forget">Forget Password</h6></a>
            <h2><button type="submit">Sign In</button></h2>
            </form>
            <span>Don't have a account<a href="#">Create One</a></span>
        </div>
    )
}
