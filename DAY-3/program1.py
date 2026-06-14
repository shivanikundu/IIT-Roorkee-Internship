#Create a function to check whether a number is a palindrome
def is_palindrome(num):                 #Function to check whether a number is a palindrome
    original = num
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return original == reversed_num
number = int(input("enter a number: "))        #Takes number as input from user
if is_palindrome(number):                       #Calling is_palindrome() function
    print((number)," is a palindrome.")
else:
    print((number)," is not a palindrome.")