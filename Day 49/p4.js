function removeDuplicates(arr) {
  let result = [];

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] !== arr[i + 1]) {
      result.push(arr[i]);
    }
  }

  return result;
}

console.log(removeDuplicates([1, 1, 2, 2, 3, 4, 4]));
