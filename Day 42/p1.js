const form = document.getElementById("form");
const nameInput = document.getElementById("name");
const emailInput = document.getElementById("email");
const errorMsg = document.getElementById("error");

form.addEventListener("submit", function (e) {
  e.preventDefault(); // it prevents real submission

  const name = nameInput.value.trim();
  const email = emailInput.value.trim();

  //  Basic Validation
  if (name === "") {
    errorMsg.innerText = "Name is required.";
    return;
  }

  if (!email.includes("@")) {
    errorMsg.innerText = "Email must contain '@'.";
    return;
  }

  //  Passed all checks!?
  errorMsg.innerText = "";
  alert("Form submitted successfully!");
});
