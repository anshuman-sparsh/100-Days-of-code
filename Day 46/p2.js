function wordFrequency(sentence) {
  const words = sentence.split(" "); // split sentence into words
  const freq = {}; // frequency object

  for (let word of words) {
    if (freq[word]) {
      freq[word] += 1;
    } else {
      freq[word] = 1;
    }
  }

  return freq;
}

console.log(wordFrequency("I love JS and I love learning"));
