import random
import string

def generate_password(password_length, include_symbols=True, include_numbers=True):
    characters = string.ascii_letters
    special_characters = "!@#$%^&*()-_=+[]{};:,.<>?/"
    numeric_characters = string.digits

    if include_symbols:
        characters += special_characters
    if include_numbers:
        characters += numeric_characters
    if password_length < 1:
        return "Invalid length"
    return ''.join(random.choice(characters) for _ in range(password_length))

password_length = int(input("Enter the desired password length: "))
use_special_characters = input("Include symbols (y/n)? ").strip().lower() == 'y'
use_numeric_characters = input("Include numbers (y/n)? ").strip().lower() == 'y'

generated_password = generate_password(password_length, use_special_characters, use_numeric_characters)
print(f"Generated password: {generated_password}")
