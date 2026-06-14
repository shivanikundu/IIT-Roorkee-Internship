def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
def cube(a):
    return a ** 3
def gcd(a,b):
    i=0
    while i == 0:
        r = a % b
        a = b
        b = r
        if r == 0:
            i = 1
    return a