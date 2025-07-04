// 🔹 4. Multiples of 3 and 5
// Print all numbers from 1 to 50. For multiples of 3, print "Fizz", for 5 "Buzz", and for both "FizzBuzz".




for (let i = 1; i <= 50; i++) {
  if (i % 3 === 0 && i % 5 === 0) {
    console.log("FizzBuzz");
  } else if (i % 3 === 0) {
    console.log("Fizz");
  } else if (i % 5 === 0) {
    console.log("Buzz");
  } else {
    console.log(i);
  }
}
// node "Day 39/p4.js"