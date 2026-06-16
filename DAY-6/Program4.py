#write a safe division function that handles zeroDivisionError
def safe_division(a , b):
    try:
       result = a / b
       return result
    except ZeroDivisionError :
       return "Cannot divide by zero!"
m = float(input("Enter Dividend : "))
n =float(input("Enter Divisor : "))
print("Result :" ,(safe_division(m ,n)))