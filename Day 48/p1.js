const input = document.getElementById("titleInput");

input.addEventListener("input", function () {
  document.title = input.value;
});