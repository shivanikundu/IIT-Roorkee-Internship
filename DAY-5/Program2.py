#Count word frequency in a sentence using a dictionary
sentence = input("Enter a sentance : ")
words = sentence.split()   #.split() is used to break that string into a list
frequency = {}
for word in words :
  if word in frequency :
    frequency[word] += 1
  else :
    frequency[word] = 1
print("\nWord Frequencies : ")
for word , count in frequency.items() :
  print((word) , ":" , (count))
