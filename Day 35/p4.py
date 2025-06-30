# User Info Badge

name = input("Enter your name: ")
age = input("Enter your age: ")
country = input("Enter your country: ")


width = max(len(name), len(age), len(country), 20) + 10

print("+" + "-" * (width - 2) + "+")
print(f"| Name: {name:<{width - 8}}|")
print(f"| Age: {age:<{width - 7}}|")
print(f"| Country: {country:<{width - 11}}|")
print("+" + "-" * (width - 2) + "+")
