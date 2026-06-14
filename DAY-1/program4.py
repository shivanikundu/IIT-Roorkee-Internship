#BMI Calculator : input height & weight , output BMI category
#Takes weight and height as input
weight = float(input("enter your weight(in kg): "))
height = float(input("enter your height(in m): "))
#Calculate BMI
bmi = weight/(height**2)
#Display BMI
print("your BMI is: ",round(bmi, 4))   
#Determine BMI Category
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else: 
     print("Category: Obese")