import random
import string

char = " " + string.punctuation + string.digits + string.ascii_letters 
char = list(char)

key = char.copy()
random.shuffle(key)

# Encryption
plain_text = input("Enter a message to decrypt: ")
cipher_text = " "

for letter in plain_text:
    index = char.index(letter)
    cipher_text += key[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

# Decryption
cipher_text = input("Enter a message to encrypt: ")
plain_text = " "

for letter in cipher_text:
    index = key.index(letter)
    plain_text += char[index]

print(f"Encrypted message: {cipher_text}")
print(f"Original message: {plain_text}")
