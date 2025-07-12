function countUniqueWords(sentence) {
  const words = sentence.toLowerCase().split(" ");
  const unique = new Set(words);
  return unique.size;
}

console.log(countUniqueWords("JavaScript is fun and JavaScript is powerful"));
// node "Day 47/p3.js"