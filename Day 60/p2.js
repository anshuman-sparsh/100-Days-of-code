// Function hoisting
greet(); // Works — "Hello from function declaration!"

function greet() {
  console.log("Hello from function declaration!");
}

// Variable hoisting with var
console.log(a); // undefined (declared but not initialized)
var a = 10;

// Variable hoisting with let and const
try {
  console.log(b); // ReferenceError: Cannot access 'b' before initialization
} catch (err) {
  console.log("Error with let:", err.message);
}

let b = 20;

try {
  console.log(c); // ReferenceError: Cannot access 'c' before initialization
} catch (err) {
  console.log("Error with const:", err.message);
}

const c = 30;

// Function expression with var
try {
  sayHi(); // TypeError: sayHi is not a function
} catch (err) {
  console.log("Error with function expression:", err.message);
}

var sayHi = function () {
  console.log("Hi there!");
};
