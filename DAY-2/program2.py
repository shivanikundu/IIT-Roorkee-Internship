#Print multiplication table of a number
#Takes number as input from user
num = int(input("Enter a number:  "))
print("Multiplication Table of", num)
for i in range(1, 11):
    print(num, "x", i, "=", num*i)      #Display table of num