# 🔹 1.
# Create a JSON string of a student object (name, age, grades) and load it into a Python dictionary using json.loads().

import json


student_obj = {
 "name": "Ankit",
 "age": 21,
 "grades": ["A","B","C"]
}


json_string = json.dumps(student_obj)
print("json string:", json_string)


data = json.loads(json_string)
print("Python Dict:", data)