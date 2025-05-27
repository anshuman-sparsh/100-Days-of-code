# Practice_2 :  Simple Interest Calculator

# Inputs: Principal, rate, time

# Output: Simple interest using formula




print("Simple Interest Calculator")
principal = int(input("Principal = "))
rate = int(input("Rate = "))
time = int(input("Time = "))

interest = principal*(rate/100)*time

print(f"Simple Interest: {interest}")