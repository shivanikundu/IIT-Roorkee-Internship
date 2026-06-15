#Caesar cipher encoder/decoder
def caesar_cipher(text , shift , mode) :
    result = ""
    if mode =="decode" :
        shift = -shift
    for char in text :
         if char.isalpha() :
            if char.isupper() :
               result += chr((ord(char) - ord('a') + shift) % 26 +ord('a'))
            else : 
               result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
         else :
            result += char
    return result
text = input("Enter message :")
shift = int(input("Enter shift value : "))
mode = input("Enter mode (encode/decode) : ")
mode = mode.lower()
output = caesar_cipher(text , shift , mode)
print("Result : " , output)
