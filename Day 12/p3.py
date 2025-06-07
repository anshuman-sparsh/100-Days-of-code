# 🔹 3.
# Create a function that receives a dictionary and prints all keys and values in a clean format.





input_string = input("Enter Data: (format= key1: value1,key2: value2): ").strip()
pair = input_string.split(",")

my_dict = {}
for item in pair:
        key,value = item.strip().split(":")
        my_dict[key] = value

def clean_format(my_dict):
        print("Cleaned Format:")
        for key,value in my_dict.items():
                  print(f"{key}:{value}")
     


clean_format(my_dict)