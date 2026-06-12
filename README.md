# IIT-Roorkee-Internship
Day report
CODE
#Takes marks as input
marks = float(input("Enter your marks(0-100): "))
if marks >= 90:
    grade="A"
elif marks >= 80:
    grade="B"
elif marks >= 70:
    grade="C"
elif marks >= 60:
    grade="D"
else:
    grade="F"
print("Grade:", grade)            #Display grade
OUTPUT
Enter your marks(0-100): 76
Grade: C



code
#Takes number as input 
num = int(input("Enter a number:  "))
print("Multiplication Table of", num)
for i in range(1, 11):
    print(num, "x", i, "=", num*i)      #Display table of num
output
Enter a number:  9
Multiplication Table of 9
9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
9 x 10 = 90


CODE-
num = 2
while num <=50:
    print(num)      #Display number
    num += 2

  OUTPUT-
  2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
CODE-
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:     #Check multiple of both 3 and 5
        print("FizzBuzz")
    elif i % 3 == 0:                  #Check multiple of 3
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")                  #Check multiple of 5
    else:
        print(i)
OUTPUT-
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
Fizz
52
53
Fizz
Buzz
56
Fizz
58
59
FizzBuzz
61
62
Fizz
64
Buzz
Fizz
67
68
Fizz
Buzz
71
Fizz
73
74
FizzBuzz
76
77
Fizz
79
Buzz
Fizz
82
83
Fizz
Buzz
86
Fizz
88
89
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
Buzz

CODE-
secret_number = 42       #NUMBER TO GUESS
while True:
    guess = int(input("Guess the number: "))
    if guess == secret_number:
        print("Found the secret number!")
        break
    elif guess != secret_number:
        print("Try again.")
        OUTPUT-
        Guess the number: 5
Try again.
Guess the number: 4
Try again.
Guess the number: 78
Try again.
Guess the number: 56
Try again.
Guess the number: 42
Found the secret number!


code-
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()
OUTPUT-
    *
   ***
  *****
 *******
*********


CODE-

        
