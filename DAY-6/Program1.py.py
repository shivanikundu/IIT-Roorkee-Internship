# Read a text file and count lines, words, and characters
f = open("program.text" , "w+")    # open file in write and read mode
#write data in f
f.write("IIt Roorkee. \nSaharanpur Campus. \nSummer Internship.")
#move the cursor to the beginning of the file f
f.seek(0)
data = f.read()   #read file f
lines = data.splitlines()  #split file into lines
words = data.split()       #split file into words
characters = len(data)

print("Number of lines in file:", len(lines))
print("Number of words in file:", len(words))
print("Number of characters in file:", characters)
f.close()