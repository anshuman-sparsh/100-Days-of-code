# 🔹 4. Car Class
# Make a class with brand, model, and year.
# Add a method start_engine() that prints a message.


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"{self.brand} {self.model} Engine started!")

my_car = Car("Toyota", "Fortuner", 2023)
my_car.start_engine()
