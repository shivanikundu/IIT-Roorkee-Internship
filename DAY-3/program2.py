#Write a recursive function for fibonacci series
def fibonacci(n):                 #Recursive function to generate Fibonacci series
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter the number of terms: "))     #Takes no of terem as input from user
print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci(i))