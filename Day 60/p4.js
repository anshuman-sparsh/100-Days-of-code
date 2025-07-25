const startBtn = document.getElementById('startBtn');
const loader = document.getElementById('loader');
const loaded = document.getElementById('loaded');

startBtn.addEventListener('click', () => {
  startBtn.style.display = 'none';
  loader.style.display = 'block';
  loaded.style.display = 'none';

  setTimeout(() => {
    loader.style.display = 'none';
    loaded.style.display = 'block';
  }, 3000); // 3 seconds
});
