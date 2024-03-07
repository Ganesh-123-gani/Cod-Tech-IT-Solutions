import random
import string

def generate_password(length, include_lowercase=True, include_uppercase=True, include_digits=True, include_symbols=True):
    characters = ""
    
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: You must include at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_input():
    length = int(input("Enter the desired length of the password: "))
    
    include_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    include_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    return length, include_lowercase, include_uppercase, include_digits, include_symbols

def main():
    print("Welcome to the Secure Password Generator!")

    length, include_lowercase, include_uppercase, include_digits, include_symbols = get_user_input()

    password = generate_password(length, include_lowercase, include_uppercase, include_digits, include_symbols)

    if password:
        print(f"Your secure password is: {password}")

if __name__ == "__main__":
    main()
