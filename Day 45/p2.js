function removeVowels(str) {
  const vowels = ['a', 'e', 'i', 'o', 'u'];
  let result = '';

  for (let char of str.toLowerCase()) {
    if (!vowels.includes(char)) {
      result += char;
    }
  }

  return result;
}

console.log(removeVowels("Hello World")); // Output: "hll wrld"
// node "Day 45/p2.js"