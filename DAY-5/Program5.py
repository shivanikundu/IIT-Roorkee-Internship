#Student report card : dict of name--.{marks , grade}
students = {}
n = int(input("Enter number of students : "))
for i in range(n) :
     name = input("Enter student name : ")
     marks = int(input("enter marks : "))
     grade = input("Enter grade : ")
     students[name] = {"Marks" : marks , "Grade" : grade}
print("\nStudent Report Card ")
print("-"*30)
for name , details in students.items() :
     print("Name :" , name)
     print("Marks : " , details["Marks"])
     print("Grade : " , details["Grade"])
     print("-"*30)