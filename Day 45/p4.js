function getUniqueNumbers(numbers) {
  const uniqueArray = [...new Set(numbers)];
  return uniqueArray;
}

console.log(getUniqueNumbers([1, 2, 2, 3, 4, 4, 5]));
// node "Day 45/p4.js"