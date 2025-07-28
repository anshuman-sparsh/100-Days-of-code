class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_role(self):
        return "Employee"

    def __str__(self):
        return f"{self.name} - {self.get_role()} - ₹{self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_role(self):
        return "Manager"


class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def get_role(self):
        return "Developer"


# Sample usage
e1 = Employee("Ravi", 40000)
m1 = Manager("Anjali", 60000, "Sales")
d1 = Developer("Karan", 50000, "Python")

for emp in [e1, m1, d1]:
    print(emp)
