#Build a student grade tracker using a list of tuples
student = [("Vandana" , 85) ,
            ("Chetna" , 78) ,
            ("Udita" , 92) ,
            ("Varsha" , 67) ,
            ("Vishavbharti" , 74)]
print (" student Grade report : ")
total_marks = 0
for name, marks in student:
    total_marks += marks
    if marks >=90:
        grade = "A"
    elif marks >=80 and marks < 90 :
        grade = "B"
    elif marks >= 70 and marks < 80 :
        grade = "C"
    elif marks >= 60 and marks < 70 :
        grade = "D"
    else:
        grade = "F"
    print("Name : ", name, ", Marks : ", marks, ", Grade : ", grade)
average_marks = total_marks / len(student)
print("Average Marks : ", average_marks)
