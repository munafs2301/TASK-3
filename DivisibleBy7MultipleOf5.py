'''Program to find numbers between 1500 and 2700, divisible by 7 and a multiple 0f 5'''


print("This Program checks for numbers between 1500 and 2700, divisible by 7 and a multiple of 5 ")
valid_numbers = [i for i in range(1500, 2701) if i % 7 == 0 and i % 5 == 0]


def choice_of_action():
    '''Determine if user would like to check a number or get a list of numbers'''
    choice = input("\n What would you like to do? \n 1. Check a particular number \n 2. Get the list of valid numbers\n\n")

    if choice == "1":
        num = int(input("\nEnter a number: "))
        if num in valid_numbers:
            print(f"{num} is a valid number")
        else:
            print(f'{num} is an invalid number')

    elif choice == "2":
        print(f"\nNumbers between 1500 and 2700, divisible by 7 and is a multiple of 5 are:  \n {valid_numbers}")
    
    else:
        print("\nPlease provide a valid input!")
        choice_of_action()
    return

choice_of_action()