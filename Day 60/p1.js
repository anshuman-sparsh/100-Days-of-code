function createCounter() {
  let count = 0;

  return function () {
    count++;
    return count;
  };
}

// Usage
const counter1 = createCounter();
console.log(counter1()); // 1
console.log(counter1()); // 2
console.log(counter1()); // 3

const counter2 = createCounter();
console.log(counter2()); // 1 (separate counter)
