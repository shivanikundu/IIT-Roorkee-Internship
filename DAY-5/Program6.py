#Anagram checker using sorted strings or sets
#using sorted string
str1 = input("Enter 1st string : ")
str2 = input("Enter 2nd string : ")
#remove spaces and convert lowercase
str1 = str1.replace(" ","").lower()
str2 = str2.replace(" ","").lower()
if sorted(str1) == sorted(str2) :
    print("The strings are Anagrms. ")
else :
    print("The strings are not Anagrms. ")