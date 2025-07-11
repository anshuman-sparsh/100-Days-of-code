function isAnagram(str1, str2) {
  if (str1.length !== str2.length) return false;

  const count1 = {};
  const count2 = {};

  for (let char of str1) {
    count1[char] = (count1[char] || 0) + 1;
  }

  for (let char of str2) {
    count2[char] = (count2[char] || 0) + 1;
  }

  for (let key in count1) {
    if (count1[key] !== count2[key]) {
      return false;
    }
  }

  return true;
}

console.log(isAnagram("listen", "silent")); // true
console.log(isAnagram("hello", "world"));   // false
