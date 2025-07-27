document.getElementById("calculateBtn").addEventListener("click", function () {
    const billAmount = parseFloat(document.getElementById("billAmount").value);
    const tipPercent = parseFloat(document.getElementById("tipPercent").value);
    const numPeople = parseInt(document.getElementById("numPeople").value);

    if (isNaN(billAmount) || isNaN(tipPercent) || isNaN(numPeople) || numPeople <= 0) {
        alert("Please enter valid values!");
        return;
    }

    const totalTip = (billAmount * tipPercent) / 100;
    const tipPerPerson = totalTip / numPeople;
    const totalPerPerson = (billAmount + totalTip) / numPeople;

    document.getElementById("totalTip").textContent = totalTip.toFixed(2);
    document.getElementById("tipPerPerson").textContent = tipPerPerson.toFixed(2);
    document.getElementById("totalPerPerson").textContent = totalPerPerson.toFixed(2);
});
