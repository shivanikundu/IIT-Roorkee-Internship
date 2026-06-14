#FizzBuzz : print Fizz , Buzzz , FizzBuzz for multiples of 3 , 5 , both
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:     #Check multiple of both 3 and 5
        print("FizzBuzz")
    elif i % 3 == 0:                  #Check multiple of 3
        print("Fizz")
    elif i % 5 == 0:                  #Check multiple of 5
        print("Buzz")                  
    else:
        print(i)