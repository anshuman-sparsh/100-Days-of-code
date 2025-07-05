// 🔹 1. Change Heading Text
// Create a page with a heading and a button. On clicking the button, change the heading text to "Hello, DOM!".




const button = document.getElementById('change-btn');
const heading = document.getElementById('main-heading');

button.addEventListener('click', function () {
  heading.innerText = 'Hello, DOM!';
});
