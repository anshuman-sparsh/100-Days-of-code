# 🔹 3. Vehicle → Car
# Vehicle has brand & max_speed. Car adds seats and overrides a method details() to include both base and child data.




class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed

    def details(self):
        print(f"Brand: {self.brand}")
        print(f"Max Speed: {self.max_speed} km/h")

class Car(Vehicle):
    def __init__(self, brand, max_speed, seats):
        super().__init__(brand, max_speed)
        self.seats = seats

    def details(self):
        super().details()
        print(f"Seats: {self.seats}")

v = Vehicle("Yamaha", 120)
c = Car("Tesla", 250, 5)

v.details()
c.details()
