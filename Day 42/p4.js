const phoneInput = document.getElementById("phone");
const validateBtn = document.getElementById("validateBtn");
const result = document.getElementById("result");

validateBtn.addEventListener("click", function () {
  const phone = phoneInput.value;


  const isTenDigits = phone.length === 10;
  const isOnlyDigits = !isNaN(phone); // checks if number
  const startsWithValidDigit = phone[0] === '7' || phone[0] === '8' || phone[0] === '9' || phone[0] === '6';

  if (isTenDigits && isOnlyDigits && startsWithValidDigit) {
    result.innerText = "Valid number ✅";
    result.style.color = "green";
  } else {
    result.innerText = "Invalid phone number ❌";
    result.style.color = "red";
  }
});
