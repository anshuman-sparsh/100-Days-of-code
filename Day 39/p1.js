function filterEvenNumbers(arr) {
  let result = [];
  for (let num of arr) {
    if (num % 2 === 0) {
      result.push(num);
    }
  }
  return result;
}

console.log(filterEvenNumbers([1, 2, 3, 4, 5, 6]));
// node "Day 39/p1.js"
