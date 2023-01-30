// frontend/src/components/SignupFormPage/index.js
import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import * as sessionActions from "../../store/session";


//THIS IS THE ONE ACTUALLY RUNNING ON THE SITE!!!!!!!!!

function SignupFormPage({showSignUpModal, setShowSignUpModal}) {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
//   const [firstName, setFirstName] = useState("")
//   const [lastName, setLastName] = useState("")
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [errors, setErrors] = useState([]);

  if (sessionUser) return <Redirect to="/" />;

  const handleSubmit = (e) => {
    e.preventDefault();
    if (password === confirmPassword) {
      setErrors([]);

      return dispatch(sessionActions.signUp(username, email, password ))
      .then((res) => {
        //not ideal solution to this issue, should be throwing an error
        if(res) {
          setErrors(res)
        } else {
          console.log("then are we getting the errors in the data v bc it doesn't see this as an error", res)
        setShowSignUpModal(false)
        }
      })
        .catch(async (res) => {
         // const data = await res.json();
          //if (data && data.errors) setErrors(data.errors);
          if(res && res.errors) setErrors(res)
        })

    }
    return setErrors(['Confirm Password field must be the same as the Password field']);
  };

  return (
    <div className="jc-c ai-c col all-margin-small">
    <div className=''>
    <button className="bg-white just-text-button circle" onClick={() => setShowSignUpModal(false)}>X</button>
    <h4>Sign Up</h4>
      <div className=''>
        <ul className=''>
        {errors.map((error, idx) => <li key={idx}>{error}</li>  )}
        </ul>
      </div>
    </div>

    <form onSubmit={handleSubmit} className="C" >
      <div className='b-margin'>
      <label>
        <input
          className='circle thin-bor bg-white'
          placeholder="Username"
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
      </label>
      </div>
      <div className='b-margin'>
      <label>
        <input
          className='circle thin-bor bg-white'
          placeholder="Email"
          type="text"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
      </label>
      </div>
      <div className='b-margin'>
      <label>
        <input
          className='circle thin-bor bg-white'
          placeholder="Password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
      </label>
      </div>
      <div className='b-margin'>
      <label>
        <input
          className='circle thin-bor bg-white'
          placeholder="Confirm Password"
          type="password"
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
          required
        />
      </label>
      </div>

      <div>
      <button className='circle thin-bor bg-white' type="submit">Sign Up</button>
      </div>

    </form>

    </div>

  );
}

export default SignupFormPage;
