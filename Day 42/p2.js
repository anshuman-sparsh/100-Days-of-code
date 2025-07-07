const passwordInput = document.getElementById("password");
const checkBtn = document.getElementById("checkBtn");
const message = document.getElementById("message");

checkBtn.addEventListener("click", function () {
  const password = passwordInput.value;
  
  const hasLetter = /[a-zA-Z]/.test(password);  
  const hasNumber = /[0-9]/.test(password);     

  if (password.length >= 8 && hasLetter && hasNumber) {
    message.innerText = "Strong";
    message.style.color = "green";
  } else {
    message.innerText = "Weak";
    message.style.color = "red";
  }
});
