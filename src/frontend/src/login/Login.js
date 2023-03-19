const Login = () => {
  return (
    <form id="info">
        <h3>Username : <input type="text" id="username" name="username" /></h3>  
        <h3>Password: <input type="password" id="password" name="pwd" class="password" /></h3>
        <a href="forgotpass.html" id="forgotpwd"><h5>Forgot Password?</h5></a>
        <button class="fancy-button">Submit</button>
    </form>
  )
}

export default Login