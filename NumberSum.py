'''
 A program that adds up numbers
 '''
 
def number_sum():
    '''Sums up two integers and returns the output. Prints the output of 20 only if the sum is between 15 and 20.'''
    try:
        num1 = int(input("\nEnter a number: "))
        num2 = int(input("\nEnter another number: "))

        num_sum = num1 + num2

        if num_sum in range(15, 21):
            print("\nSum of the two numbers is 20")
        else:
            print(f"\nSum of the two numbers is {num_sum}")
    except ValueError:
        print("Invalid input! Please enter a number")
        number_sum()
    return

number_sum()