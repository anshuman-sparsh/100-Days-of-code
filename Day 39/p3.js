// 🔹 3. Student Object Summary
// Create an object student with name, age, and grades (array). Write a method to print the average grade.



const student = {
  name: "Anshuman",
  age: 19,
  grades: [90, 85, 92],
  getAverage: function () {
    let total = 0;
    for (let grade of this.grades) {
      total += grade;
    }
    return total / this.grades.length;
  }
};

console.log(`Average Grade: ${student.getAverage()}`);
// node "Day 39/p3.js"