// 🔹 5. Reverse an Array
// Write a function that reverses an array without using .reverse().



function reverseArray(arr) {
  let reversed = [];
  for (let i = arr.length - 1; i >= 0; i--) {
    reversed.push(arr[i]);
  }
  return reversed;
}

let originalArray = [1, 2, 3, 4, 5];
let result = reverseArray([1, 2, 3, 4, 5]);
console.log(result);
// node "Day 39/p5.js"