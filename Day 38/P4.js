// 4. Simple Calculator
// Write a function calculate(a, b, operator) that performs +, –, *, / based on the operator.



function calculate(a, b, operator) {
  if (operator === "+") {
    console.log(a + b);
  } else if (operator === "-") {
    console.log(a - b);
  } else if (operator === "*") {
    console.log(a * b);
  } else if (operator === "/") {
    console.log(a / b);
  } else {
    console.log("Invalid operator");
  }
}

calculate(1, 9, "+"); 
calculate(2,8,"/");
calculate(2,8,"-");
calculate(2,8,"*");
// node "Day 38/p4.js"