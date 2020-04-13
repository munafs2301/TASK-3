'''
A program that converts temperature from Celsuis to Farenheit and vice versa
'''

print("\n A TEMPERATURE CONVERTER\n")

def to_faren():
    ''' Converts to temperature to Farenheit'''
    temp = int(input("\n Please enter the temperature:  "))
    temperature = (temp * 1.8) + 32
    print(f"\n The temperature in Farenheit is {temperature}F")
    return

def to_cel():
    '''Converts temperature to Celsuis'''
    temp = int(input("\n Please enter the temperature:  "))
    temperature = (temp - 32) / 32
    print(f"\n The temperature in Celsuis is {temperature}C")
    return


def choose_option():
    '''Allows user to make choice on type of conversion'''
    choice = input("What would you like to do? \n 1. Celsuis to Farenheit conversion \n 2. Farenheit to Celsuis conversion\n\n")

    if choice == "1":
       to_faren()
        
    elif choice == "2":
        to_cel()

    else:
        print("\nInvalid input! Press either 1 or 2.\n")
        choose_option()
    return


choose_option()