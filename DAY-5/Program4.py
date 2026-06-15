#Build a word reversal and palindrome checker
word = input("Enter a word :")
reversed_word = word[::-1]      #reverse the word 
print("Reversed word is : " , reversed_word)
if word.lower() == reversed_word.lower() :          #check palindrome
     print("The word is a palindrome. ")
else :
     print("The word is not a palindrome.")
