function findLongestWord(sentence) {
  const words = sentence.split(" ");
  let longest = "";

  for (let word of words) {
    if (word.length > longest.length) {
      longest = word;
    }
  }

  return longest;
}

console.log(findLongestWord("The quick brown fox jumps over the lazy dog"));
// node "Day 45/p3.js"