#Password generator using random & string modules
import random 
import string
#password generator
def generate_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password
#Input password length from user
password_length = int(input("Enter the length of the password: "))
# Generate and display the password
password = generate_password(password_length)
print("Generated Password:", password)