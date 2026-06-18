import random
import string

print("===== ADVANCED PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

characters = string.ascii_lowercase

uppercase = input("Include uppercase letters? (y/n): ").lower()
numbers = input("Include numbers? (y/n): ").lower()
symbols = input("Include special characters? (y/n): ").lower()

if uppercase == 'y':
    characters += string.ascii_uppercase

if numbers == 'y':
    characters += string.digits

if symbols == 'y':
    characters += string.punctuation

password = ''.join(random.choice(characters) for _ in range(length))

print("\nGenerated Password:")
print(password)
