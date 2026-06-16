#Write student data to a CSV file and read it back
import csv
with open("students.csv" ,"w+" , newline = "") as f :
   data = csv.writer(f)
   header = ["Roll no." , "Name" , "Age"]
   n = int(input("Enter number of students : "))
   for i in range(n) :
      name = input("Enter name of student : ")
      age = int(input("Enter age of " +(name) + " : "))
      roll_no = int(input("Enter Roll no. " + (name) + " : "))
      data.writerow([name , age , roll_no])
   cursor = f.seek(0)
   reader = csv.reader(f)  #read data from csv file
   print("Student data written to students.csv")
   print("\nStudent Data : ")
   for row in reader :
       print(row)