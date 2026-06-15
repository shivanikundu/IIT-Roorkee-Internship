#Find unique characters in a string using sets
text = input("Enter a string : ")
unique_char = set(text)
print("Unique characters are : ")
for char in unique_char :
    print(char , end =" ")