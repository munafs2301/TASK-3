'''
Program to guess a number between 1 and 9
''' 

print("-*-" * 51)
def number_guess():
    '''Gives an output of 'Well guessed' if user is able to guess a number between 1 and 9'''
    try:
        number = int(input("\nGuess a number: "))
        random_number = range(1, 10)

        if number in random_number:
            print(f"\nWell guessed. The number is {number}\n")
        
        else:
            print("\nWrong!")
            number_guess()
    except:
        print("Invalid input! Try again.")
        number_guess()
    return

number_guess()
print("-*-" * 51)