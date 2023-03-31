function validate() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    if ((username == "angelo" && password == "1234")||(username == "heyron" && password == "4567")||(username == "harshed" && password == "9188")||(username == "sameer" && password == "4567")) {
      window.location.href = "success.html";
    } else {
      document.getElementById("message").innerHTML = "Invalid username or password!";
    }
  }
 