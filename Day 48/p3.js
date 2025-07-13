const btn = document.getElementById("toggleBtn");
const para = document.getElementById("para");

btn.addEventListener("click", function () {
  if (para.style.display === "none") {
    para.style.display = "block";
    btn.textContent = "Hide";
  } else {
    para.style.display = "none";
    btn.textContent = "Show";
  }
});
