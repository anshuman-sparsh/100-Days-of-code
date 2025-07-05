// 🔹 5. Show/Hide Paragraph
// Create a paragraph and a button. Clicking the button hides/shows the paragraph text.



const btn = document.getElementById("toggleBtn");
const para = document.getElementById("textPara");

btn.addEventListener("click", function () {
  if (para.style.display === "none") {
    para.style.display = "block";
    btn.innerText = "Hide";
  } else {
    para.style.display = "none";
    btn.innerText = "Show";
  }
});
