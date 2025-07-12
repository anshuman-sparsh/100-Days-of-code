function findCommon(arr1, arr2) {
  const set2 = new Set(arr2);
  return arr1.filter(num => set2.has(num));
}

console.log(findCommon([1, 2, 3, 4], [3, 4, 5, 6]));
// node "Day 47/p2.js"