#Find the 2nd largest and 2nd smallest number in a list
list_num = [1 , 2 , 3 , 5 , 3 , 7 , 8 , 9 , 4 , 2 , 6 , 8 , 5 , 6 , 3]
sort_list_num = list.sort(list_num)
unique_num = list(set(list_num))
if len(unique_num) <= 1 :
    print("List must contain atleast two distinct numbers. ")
else :
    second_smallest = unique_num[1]
    second_largest = unique_num[-2]
    print("List of numbers : " , list_num)
    print("2nd Smallest Number is : " , second_smallest)
    print("2nd Largest Number is : " , second_largest)