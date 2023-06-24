import random
import string

def generate_password(length=8, include_digits=True, include_symbols=True):
    chars = string.ascii_letters
    if include_digits:
        chars += string.digits
    if include_symbols:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    length = int(input("Enter the length of the password: "))
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, include_digits, include_symbols)
    print("Your random password is:", password)

if __name__ == "__main__":
    main()
