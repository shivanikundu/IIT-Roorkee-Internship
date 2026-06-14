#Write a program to remove duplicates from a list
list_num = [ 1 , 2 , 3 , 4 , 5 , 4 , 3 , 2 , 6 , 4 , 8 , 2 , 9 , 13 , 8 , 5 , 4 , 3 ]
unique_numbers = list(set(list_num))
print("Original List : " , (list_num))
print("List after removing duplicates : " , (unique_numbers))

list_leters = ["A" ,"B" , "C" , "A" , "C" , "B" , "B" , "B" , "C" , "A" , "C"]
unique_leters = list(set(list_leters))
print("Original List : " , (list_leters))
print("List after removing duplicates : " , (unique_leters))