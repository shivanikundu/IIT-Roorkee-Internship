#Number guessing game using a while loop
secret_number = 42       #Number to guess
while True:
    guess = int(input("Guess the number: "))
    if guess == secret_number:
        print("Found the secret number!")
        break
    elif guess != secret_number:
        print("Try again.")