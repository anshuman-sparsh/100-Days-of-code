function boilWater() {
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log("🫧 Water boiled");
      resolve();
    }, 1000);
  });
}

function addTeaLeaves() {
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log("🍃 Tea leaves added");
      resolve();
    }, 1000);
  });
}

function pourTea() {
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log("🍵 Tea poured into cup");
      resolve("✅ Tea is ready!");
    }, 1000);
  });
}

// Chaining the tasks step-by-step
boilWater()
  .then(addTeaLeaves)
  .then(pourTea)
  .then((finalMsg) => {
    console.log(finalMsg);
  })
  .catch((error) => {
    console.error("Something went wrong:", error);
  });
