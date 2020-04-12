'''
A program that checks for password validity
'''

import re

numbers = "[0 1 2 3 4 5 6 7 8 9 ]"
cap_letters = '[A B C D E F G H I J K L M N O P Q R S T U V W X Y Z]'
print("PASSWORD CREATION RULES \n 1. It must be more than than 8 characters \n 2. It must contain a capital letter \n 3. It must a contain number")


def password_validator():
    password = input("\nPlease enter a password: ")

    if len(password) > 8:
        if re.search(numbers, password):
            if re.search(cap_letters, password,):
                    print("\nYou have succefully created your password")
            else:
                print("There is no capital letter")
                password_validator()
        else:
            print("\nPlease include a number")
            password_validator()
    else:
        print("\nYour password is less than or equal to 8 characters")
        password_validator()


password_validator()
