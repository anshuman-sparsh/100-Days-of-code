# 🔹 2. BMI Category Reporter
# 📌 Ask for height (in meters) and weight (in kg).
# ✅ Use calculate_bmi() and get_bmi_category(bmi)
# Categorize into: Underweight, Normal, Overweight, Obese.




def calculate_bmi(height, weight):
    return weight / (height ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))

bmi = calculate_bmi(height, weight)
category = get_bmi_category(bmi)

print(f"Your BMI is: {bmi:.2f}")
print(f"BMI Category: {category}")
