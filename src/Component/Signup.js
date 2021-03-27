import React from 'react'

export const Signup = () => {
    return (
        <div className="signup">
            <h2>Please fill in this form</h2>
            <form>
            <input type="text" placeholder="Enter Your Name" id="name" required/>
            <input type="number" placeholder="Enter Your Number"  required/>
            <input type="email" placeholder="Enter your Email" required/>
            <input type="password" placeholder="Enter your Password"/>
            <button type ="submit">Sign Up</button>
            </form>
            <h5>Already had a account <a href="#">Click Here</a></h5>

        </div>
    )
}
