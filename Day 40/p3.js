// 🔹 3. Counter App
// Create a number counter with:
// ➕ Increment button
// ➖ Decrement button
// 🔄 Reset button





let count = 0;
const countDisplay = document.getElementById("count");

document.getElementById("increment").addEventListener("click", function () {
  count++;
  countDisplay.innerText = count;
});

document.getElementById("decrement").addEventListener("click", function () {
  count--;
  countDisplay.innerText = count;
});

document.getElementById("reset").addEventListener("click", function () {
  count = 0;
  countDisplay.innerText = count;
});
