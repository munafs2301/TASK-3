'''Program to find numbers between 1500 and 2700, divisible by 7 and a multiple 0f 5'''


valid_numbers = [i for i in range(1500, 2701) if i % 7 == 0 and i % 5 == 0]
print(f"Numbers between 1500 and 2700, divisible by 7 and is a multiple of 5 are:  \n {valid_numbers}")