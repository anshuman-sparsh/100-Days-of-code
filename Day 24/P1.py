# 🔹 1. Animal Class → Dog Class
# Create a base class Animal with method speak() → “Animal speaks”.
# Create Dog subclass that overrides speak() → “Woof!”





class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Woof!"

a = Animal()
d = Dog()
print(a.speak())
print(d.speak())
