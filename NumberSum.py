'''
 A Python program to sum two given integers.
 If the sum is between 15 to 20 it will return 20.
'''
def number_sum():
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


number_sum()