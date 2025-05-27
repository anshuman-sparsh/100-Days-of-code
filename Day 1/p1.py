# Practice_1 : Age Group Classifier

# Input: Age

# Output: “Child”, “Teen”, “Adult”, “Senior” based on range



age = float(input("Enter your age: "))
if age > 0 and age < 1:
   print("Baby")
elif (age == 1 and age == 12) or (age  > 1 and age < 13): 
    print("child")
elif (age == 13 and age == 19) or (age > 13 and age < 20):
    print("Teen")
elif (age == 20 and age == 59) or (age > 20 and age < 60):
    print("Adult")
elif (age == 60 ) or age > 60:
    print("Senior")
else: age == 0
print( "You doesn't exist.")
    
 
    