const form = document.getElementById("registerForm");
const message = document.getElementById("message");

form.addEventListener("submit", function (e) {
  e.preventDefault();

 
  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value;
  const phone = document.getElementById("phone").value.trim();

  
  if (name === "") {
    message.innerText = "Name is required ❌";
    message.style.color = "red";
    return;
  }

  
  if (!email.includes("@")) {
    message.innerText = "Email must contain '@' ❌";
    message.style.color = "red";
    return;
  }

  
  let hasLetter = false;
  let hasNumber = false;

  for (let i = 0; i < password.length; i++) {
    const char = password[i];
    if (isNaN(char)) {
      hasLetter = true;
    } else {
      hasNumber = true;
    }
  }

  if (password.length < 8 || !hasLetter || !hasNumber) {
    message.innerText = "Password must be 8+ characters and include letters and numbers ❌";
    message.style.color = "red";
    return;
  }

 
  if (phone.length !== 10) {
    message.innerText = "Phone must be exactly 10 digits ❌";
    message.style.color = "red";
    return;
  }

  let isAllDigits = true;
  for (let i = 0; i < phone.length; i++) {
    if (isNaN(phone[i])) {
      isAllDigits = false;
      break;
    }
  }

  if (!isAllDigits) {
    message.innerText = "Phone must contain only digits ❌";
    message.style.color = "red";
    return;
  }

  if (phone[0] !== "9" && phone[0] !== "8" && phone[0] !== "7" && phone[0] !== "6" && phone[0] !== "0") {
    message.innerText = "Phone must start with 9, 8, 7, 6 or 0 ❌";
    message.style.color = "red";
    return;
  }

  
  message.innerText = "Registration successful ✅";
  message.style.color = "green";
});
