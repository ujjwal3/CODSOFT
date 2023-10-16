import random
import string

print("Welcome to the Password Generator!")

pass_len = int(input("Please enter the desired password length: "))

up_letters = input("Do you want to include uppercase letters? (y/n): ")
low_letters = input("Do you want to include lowercase letters? (y/n): ")
num = input("Do you want to include numbers? (y/n): ")
special_char = input("Do you want to include special characters? (y/n): ")


if up_letters == "y" and low_letters == "y" and num == "y" and special_char == "y":
    Generated_Password = (
        string.ascii_uppercase
        + string.ascii_lowercase
        + string.punctuation
        + string.digits
    )
    password = "".join(random.choice(Generated_Password) for i in range(pass_len))
    print(f"Generated Password: {password}")
else:
 exit()
