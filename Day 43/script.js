// Get elements
const nameInput = document.getElementById("expense-name");
const amountInput = document.getElementById("expense-amount");
const addBtn = document.getElementById("add-btn");
const list = document.getElementById("expense-list");
const totalEl = document.getElementById("total");
const toggleBtn = document.getElementById("toggle-mode");

let total = 0;

// Load from localStorage on start
window.onload = function () {
  const saved = JSON.parse(localStorage.getItem("expenses")) || [];
  saved.forEach(item => {
    addExpenseToDOM(item.name, item.amount);
    total += Number(item.amount);
  });
  updateTotal();
};

// Add expense button
addBtn.addEventListener("click", () => {
  const name = nameInput.value.trim();
  const amount = parseFloat(amountInput.value);

  if (name === "" || isNaN(amount)) {
    alert("Please enter valid expense name and amount.");
    return;
  }

  addExpenseToDOM(name, amount);
  saveToLocalStorage(name, amount);

  total += amount;
  updateTotal();

  nameInput.value = "";
  amountInput.value = "";
});

// Add to screen
function addExpenseToDOM(name, amount) {
  const li = document.createElement("li");
  li.innerHTML = `
    ${name} - ₹${amount.toFixed(2)}
    <button onclick="deleteExpense(this, ${amount})">❌</button>
  `;
  list.appendChild(li);
}

// Delete expense
function deleteExpense(button, amount) {
  const li = button.parentElement;
  list.removeChild(li);
  total -= amount;
  updateTotal();
  updateLocalStorage();
}

// Update total
function updateTotal() {
  totalEl.innerText = `Total: ₹${total.toFixed(2)}`;
}

// Save expense to localStorage
function saveToLocalStorage(name, amount) {
  const existing = JSON.parse(localStorage.getItem("expenses")) || [];
  existing.push({ name, amount });
  localStorage.setItem("expenses", JSON.stringify(existing));
}

// Update localStorage after deleting
function updateLocalStorage() {
  const items = [];
  list.querySelectorAll("li").forEach(li => {
    const [text] = li.innerText.split(" - ₹");
    const amt = parseFloat(li.innerText.split("₹")[1]);
    items.push({ name: text.replace(" ❌", ""), amount: amt });
  });
  localStorage.setItem("expenses", JSON.stringify(items));
}

