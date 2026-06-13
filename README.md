# IIT-Roorkee-Internship
Day repor
def is_palindrome(number):
...     num_str = str(number)
...     return num_str == num_str[::-1]
... print (is_palindrome(121))
...
True
>>> print(is_palindrome(123))
False
>>>
 def fibonacci(n):
...     if n == 0:
...         return 0
...     elif n == 1:
...         return 1
...     return fibonacci(n - 1) + fibonacci(n - 2)
...
... for i in range(10):
...     print(fibonacci(i), end=" ")
...
0 1 1 2 3 5 8 13 21 34 >>>

>>> def add(a, b):
...     return a + b
...     print(add(10,5))
...
>>>
>>> def add(a, b):
...     return a + b
...     print(add(10, 5))
...
>>> def add(a, b):
...     return a + b
...
... def subtract(a, b):
...     return a - b
...
... def multiply(a, b):
...     return a * b
...
... def square(n):
...     return n * n
...
... def factorial(n):
...     if n == 0 or n == 1:
...         return 1
...
...     result = 1
...     for i in range(2, n + 1):
...         result *= i
...
...     return result
...
...
... print("Addition:", add(10, 5))
... print("Subtraction:", subtract(10, 5))
... print("Multiplication:", multiply(10, 5))
... print("Square:", square(6))
... print("Factorial:", factorial(5))
...
Addition: 15
Subtraction: 5
Multiplication: 50
Square: 36
Factorial: 120
 import random
>>> dice=random.randint(1,6)
>>> print("you rolled:",dice)
you rolled: 5
>>> print("you rolled:",dice)
you rolled: 5
 def quiz():
...     questions = [
...         ("who is the host of sx6?", "karan kundra"),
...         ("who is the winner of sx6?", "gullu"),
...         ("who is the connection of yogesh?", "akansha+ruru")
...     ]
...
...     score = 0
...
...     for q, correct_answer in questions:
...         answer = input(q + " ")
...
...         if answer.lower() == correct_answer:
...             print("Correct!")
...             score += 1
...         else:
...             print("Wrong!")
...
...     print("\nFinal Score:", score, "/", len(questions))
...
... quiz()
...
who is the host of sx6? sunny leone
Wrong!
who is the winner of sx6? himashu
Wrong!
who is the connection of yogesh? ruru
Wrong!

Final Score: 0 / 3
>>> import random
... import string
...
... def generate_password(length):
...     chars = string.ascii_letters + string.digits + string.punctuation
...     return ''.join(random.choice(chars) for _ in range(length))
...
... print(generate_password(8))
...
G0N*C\??
>>>
>>>
>>> import random
... import string
...
... def generate_password(length):
...     chars = string.ascii_letters + string.digits + string.punctuation
...     return ''.join(random.choice(chars) for _ in range(length))
...
... print(generate_password(8))
...
dc?YmG/A
>>> import random
... import string
...
... def generate_password(length):
...     chars = string.ascii_letters + string.digits + string.punctuation
...     return ''.join(random.choice(chars) for _ in range(length))
... print(generate_password(8))
...
CQ<(K5Y<
>>>
>>> iterative approach
>>> def factorial_iterative(n):
...     result = 1
...
...     for i in range(1, n + 1):
...         result = result * i
...
...     return result
...
... print(factorial_iterative(9))
...
362880
>>> iterative approach
>>> def factorial_iterative(n):
...     result = 1
...
...     for i in range(1, n + 1):
...         result = result * i
...
...     return result
...
... print(factorial_iterative(9))
...
362880
>>> RECURSIVE APPROACH
>>>  def factorial_recursive(n):
...     if n == 0 or n == 1:
...         return 1
...
...     return n * factorial_recursive(n - 1)
...
... print(factorial_recursive(6))
...
720
