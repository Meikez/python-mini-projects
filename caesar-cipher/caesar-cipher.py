alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(plain_text, shift_amount):
    cipher_text=""
    for letter in plain_text:
        position=alphabet.index(letter)
        new_position= position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text+=new_letter
    print(f"The encoded text is {cipher_text}")

def decrypt(encrypt_text, shift_amount):
    decrypt_text=""
    for letter in encrypt_text:
        position = alphabet.index(letter)
        new_position= position-shift_amount
        new_letter = alphabet[new_position]
        decrypt_text+=new_letter
    print(f"The dec oded text is {decrypt_text}")

if direction=="encode":
    encrypt(plain_text=text,shift_amount=shift)
elif direction == "decode":
    decrypt(encrypt_text=text,shift_amount=shift)
    
    
# Add Logo and repeate 