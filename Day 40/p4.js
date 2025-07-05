// 🔹 4. Live Input Display
// Add an input box. As you type, the text should appear live below it.





const inputBox = document.getElementById("inputBox");
const output = document.getElementById("output");

inputBox.addEventListener("input", function () {
  output.innerText = inputBox.value;
});
