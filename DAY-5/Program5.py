#Student report card : dict of name--.{marks , grade}
students = {"Vandana" : {"marks" : 92 , "grade" :"A"} , 
            "Chetna" : {"marks" : 88 , "grade" :"B"} ,
            "Versha" : {"marks" : 70 , "grade" :"C"}}
print("Student Report Card ")
print("-"*30)
for name , details in students.items() :
     print("Name :" , name)
     print("Marks : " , details["marks"])
     print("Grade : " , details["grade"])
     print("-"*30)