function firstUniqueChar(str) {
  const count = {};

  // Count frequency of each character
  for (let char of str) {
    count[char] = (count[char] || 0) + 1;
  }

  // Loop again to find the first non-repeating character
  for (let char of str) {
    if (count[char] === 1) {
      return char;
    }
  }

  return null;
}

console.log(firstUniqueChar("aabccdeff")); // b
console.log(firstUniqueChar("aabbcc"));    // null
