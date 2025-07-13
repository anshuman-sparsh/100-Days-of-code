const bulb = document.getElementById("bulb");
const btn = document.getElementById("toggleBtn");

btn.addEventListener("click", function () {
  if (bulb.src.includes("off.png")) {
    bulb.src = "on.png";
    btn.textContent = "Turn Off";
  } else {
    bulb.src = "off.png";
    btn.textContent = "Turn On";
  }
});
