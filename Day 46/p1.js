function mostFrequentChar(str) {
  const freq = {}; // Object to store character counts

  for (let char of str) {
    if (freq[char]) {
      freq[char] += 1;
    } else {
      freq[char] = 1;
    }
  }

  let maxChar = null;
  let maxCount = 0;

  for (let char in freq) {
    if (freq[char] > maxCount) {
      maxChar = char;
      maxCount = freq[char];
    }
  }

  return maxChar;
}

console.log(mostFrequentChar("mississippi")); // Output: "i"
