#Build a simple calculator that adds , subtracts , multiples and divides two numbers
#Input two numbers from user
num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
#perform operation(+,-,*,/)
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
if num2 != 0:                   #check denominator = 0
    division = num1 / num2
else:
    division = "Error: Division by zero is not allowed."
#Display results
print("Addition: ", (addition))
print("Subtraction: ", (subtraction))
print("Multiplication: ", (multiplication))
print("Division: ", (division))