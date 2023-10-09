from random import sample
from string import ascii_letters, digits, punctuation
from pyperclip import copy

printables = ascii_letters + digits + punctuation


def main():
    while True:

        # Catch error when converting input to integer
        try:
            password_length = int(input("Please enter your desired password length: "))
        except Exception as e:
            print("Please enter a valid password length.")
            continue

        if password_length <= 0 or password_length > 65535:
            print("Please enter a valid password length.")
            continue

        password = sample(printables, password_length)

        print("Your generated password is: %s" % password)
        copy(password)
        print("Password copied to your clipboard.")

if __name__ == '__main__':
    main()
