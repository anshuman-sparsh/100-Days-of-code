const textBox = document.getElementById("textBox");
const charCount = document.getElementById("charCount");

textBox.addEventListener("input", function () {
  const maxLength = 100;
  const remaining = maxLength - textBox.value.length;
  charCount.innerText = `Remaining: ${remaining} characters`;
});
