# 🔹 2. Marks Average
# Ask the user to input marks of 5 subjects
# Store them in a list
# Print the total and average
# Print “Passed” if average ≥ 40, else “Failed”




subject_marks=[]
print("Enter marks of each subject")

for i in range(5):
    sub_marks = int(input(f"Subject {i+1}: "))               
    subject_marks.append(sub_marks)             
                       
# sub_marks1 =int(input("Enter marks of 1st subject: "))
# sub_marks2 =int(input("Enter marks of 2nd subject: "))                                 
# sub_marks3 =int(input("Enter marks of 3rd subject: "))
# sub_marks4 =int(input("Enter marks of 4th subject: "))
# sub_marks5 =int(input("Enter marks of 5th subject: "))
                      
# list.append(sub_marks1)
# list.append(sub_marks2)
# list.append(sub_marks3)
# list.append(sub_marks4)
# list.append(sub_marks5)

total = sum(subject_marks) #total = sub_marks5 + sub_marks1 + sub_marks2 + sub_marks3 + sub_marks4
average = total/len(subject_marks)

print(f"Total marks: {total}")
print(f"Average marks: {average}")

if average>= 40:
    print("You have passed the exam! ")
else : 
    print("You Failed! Try next year!")