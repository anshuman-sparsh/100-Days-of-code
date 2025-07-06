const quotes = [
  { text: "Stay hungry, stay foolish.", author: "Steve Jobs" },
  { text: "Code is like humor. When you have to explain it, it’s bad.", author: "Cory House" },
  { text: "Fix the cause, not the symptom.", author: "Steve Maguire" },
  { text: "Programs must be written for people to read.", author: "Harold Abelson" },
  { text: "First, solve the problem. Then, write the code.", author: "John Johnson" },
  { text: "Simplicity is the soul of efficiency.", author: "Austin Freeman" },
  { text: "Make it work, make it right, make it fast.", author: "Kent Beck" }
];

const quoteEl = document.getElementById("quote")
const authorEl = document.getElementById("author")
const btn = document.getElementById("generateBtn")

function getRandomQuote(){
    const index = Math.floor(Math.random()*quotes.length);
    const quote = quotes[index];
     
    quoteEl.style.opacity = 0;
    authorEl.style.opacity = 0;

     setTimeout(() => {
    quoteEl.textContent = `"${quote.text}"`;
    authorEl.textContent = `— ${quote.author}`;
    quoteEl.style.opacity = 1;
    authorEl.style.opacity = 1;
  }, 300);
}


console.log("JS file loaded");
console.log(quoteEl, authorEl, btn);


// Button click
btn.addEventListener("click", getRandomQuote);

// Press Enter key
document.addEventListener("keydown", function (e) {
  if (e.key === "Enter") {
    getRandomQuote();
  }
});