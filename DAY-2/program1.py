#write a grade classifier : input marks , output A/B/C/D/F
#Takes marks as input from user
marks = float(input("Enter your marks(0-100): "))
if marks >= 90:
    grade = "A"
elif marks >= 80 and marks < 90 :
    grade = "B"
elif marks >= 70 and marks < 80 :
    grade = "C"
elif marks >= 50 and marks < 70 :
    grade = "D"
else:
    grade = "F"
print("Grade:", grade)            #Display grade
