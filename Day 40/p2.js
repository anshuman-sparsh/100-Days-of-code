// 🔹 2. Toggle Background Color
// Add a button that toggles the background color between light and dark mode.




const button = document.getElementById('toggle-btn');
let darkMode = false;

button.addEventListener('click', function () {
  if (darkMode) {
    document.body.style.backgroundColor = 'white';
    document.body.style.color = 'black';
  } else {
    document.body.style.backgroundColor = '#222';
    document.body.style.color = 'white';
  }
  darkMode = !darkMode;
});
