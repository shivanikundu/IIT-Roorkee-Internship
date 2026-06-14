#Temperature converter : Celsius to Fahrenheit and vice versa
print("Temperature Converter")
choice = int(input("enter your choice(1 for Celsius to Fahrenheit, 2 for Fahrenheit to Celsius): "))
if choice == 1:
    print("1. Celsius to Fahrenheit")
    celsius = float(input("enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32                            #Convert tempt celsius to fahrenheit
    print("temperature in Fahrenheit is: ", round(fahrenheit, 2))
elif choice == 2:
    print("2. Fahrenheit to Celsius")
    fahrenheit = float(input("enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9                         #Convert tempt fahrenheit to celsius
    print("temperature in Celsius is: ", round(celsius, 2))
else:
    print("Invalid choice")
