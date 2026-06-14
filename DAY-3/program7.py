#Factorial calculator : iterative and recursive approaches
#Iterative function to calculate factorial of a number
def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        return fact
    #Recursive function to calculate factorial of a number
def factorial_recursive(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
    #Take number as input from user
num = int(input("Enter a number: "))
print("Iterative Factorial: ", factorial_iterative(num))
print("Recursive Factorial: ", factorial_recursive(num))