function mergeSorted(arr1, arr2) {
  let i = 0, j = 0;
  let result = [];

  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] < arr2[j]) result.push(arr1[i++]);
    else result.push(arr2[j++]);
  }

// adding remaining items
  while (i < arr1.length) result.push(arr1[i++]);
  while (j < arr2.length) result.push(arr2[j++]);

  return result;
}

console.log(mergeSorted([1, 3, 5], [2, 4, 6])); 
