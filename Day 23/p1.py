# 🔹 1. Laptop Class
# Create a Laptop class with instance variables: brand, ram, price.
# Add a class variable total_laptops to count all objects created.



class Laptop:
    total_laptops = 0

    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price
        Laptop.total_laptops += 1  

    def show_details(self):
        print(f"Brand: {self.brand}, RAM: {self.ram}GB, Price: ₹{self.price}")


l1 = Laptop("Dell", 8, 50000)
l2 = Laptop("HP", 16, 65000)
l3 = Laptop("Apple", 8, 90000)

l1.show_details()
l2.show_details()
l3.show_details()

print(f"Total Laptops: {Laptop.total_laptops}")