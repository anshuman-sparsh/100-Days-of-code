// 🔹 2. Count Vowels in String
// Take a string and count how many vowels are in it using a loop and conditionals.


function countVowels(str) {
  let count = 0;
  let vowels = "aeiouAEIOU";
  for (let char of str) {
    if (vowels.includes(char)) {
      count++;
    }
  }
  return count;
}

console.log(countVowels("Anshuman Sparsh"));
// node "Day 39/p2.js"
