class Animal:
    def speak(self):
        return "Some generic animal sound"


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Cow(Animal):
    def speak(self):
        return "Moo!"


# Function demonstrating polymorphism
def animal_sound(animal):
    if isinstance(animal, Animal):
        print(f"{animal.__class__.__name__} says: {animal.speak()}")
    else:
        print("Not an Animal object")


# Create instances
dog = Dog()
cat = Cat()
cow = Cow()

# Use polymorphic function
for a in [dog, cat, cow]:
    animal_sound(a)
