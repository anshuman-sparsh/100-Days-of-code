// Mobile nav toggle
const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('.nav-links');
navToggle.addEventListener('click', () => {
  navLinks.classList.toggle('active');
});

// Scroll to section
const scrollLinks = document.querySelectorAll('a[href^="#"]');
scrollLinks.forEach(link => {
  link.addEventListener('click', function(e) {
    const targetId = this.getAttribute('href').slice(1);
    const target = document.getElementById(targetId);
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth' });
      navLinks.classList.remove('active'); // Close nav on mobile
    }
  });
});

// Modal show/hide
const modal = document.getElementById('modal');
const ctaBtn = document.getElementById('cta-btn');
const closeModalBtn = document.querySelector('.close-modal');
ctaBtn.addEventListener('click', () => {
  modal.setAttribute('aria-hidden', 'false');
});
closeModalBtn.addEventListener('click', () => {
  modal.setAttribute('aria-hidden', 'true');
});
modal.addEventListener('click', (e) => {
  if (e.target === modal) {
    modal.setAttribute('aria-hidden', 'true');
  }
});

// Form validation
const subscribeForm = document.getElementById('subscribe-form');
const emailInput = document.getElementById('email');
const formMessage = document.querySelector('.form-message');
subscribeForm.addEventListener('submit', function(e) {
  e.preventDefault();
  const email = emailInput.value.trim();
  if (!validateEmail(email)) {
    formMessage.textContent = 'Please enter a valid email address.';
    return;
  }
  formMessage.style.color = '#388e3c';
  formMessage.textContent = 'Thank you for subscribing!';
  subscribeForm.reset();
  setTimeout(() => {
    modal.setAttribute('aria-hidden', 'true');
    formMessage.textContent = '';
    formMessage.style.color = '';
  }, 1500);
});
function validateEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
} 