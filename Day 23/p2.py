# 🔹 2. Employee Class
# Add a company_name class variable, and use @classmethod to change it.



class Employee:
    company_name = "TechCorp"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name

    def show(self):
        print(f"{self.name} works at {Employee.company_name}")


e1 = Employee("Anjali kumari")
e2 = Employee("Rohit mehra")

e1.show()
Employee.change_company("DataSoft")
e2.show()