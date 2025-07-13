// Here to Select each button
const redBtn = document.getElementById("redBtn");
const blueBtn = document.getElementById("blueBtn");
const greenBtn = document.getElementById("greenBtn");
const yellowBtn = document.getElementById("yellowBtn");

// Adding click event listeners
redBtn.addEventListener("click", function () {
  document.body.style.backgroundColor = "red";
});

blueBtn.addEventListener("click", function () {
  document.body.style.backgroundColor = "blue";
});

greenBtn.addEventListener("click", function () {
  document.body.style.backgroundColor = "green";
});

yellowBtn.addEventListener("click", function () {
  document.body.style.backgroundColor = "yellow";
});

greyBtn.addEventListener("click", function () {
  document.body.style.backgroundColor = "grey";
});
