const textArea = document.getElementById("inputText");
const wordCount = document.getElementById("wordCount");
const charCount = document.getElementById("charCount");

textArea.addEventListener("input", () => {
  const text = textArea.value.trim();
  const words = text === "" ? 0 : text.split(/\s+/).length;
  const chars = text.replace(/\s/g, "").length;

  wordCount.textContent = words;
  charCount.textContent = chars;
});
