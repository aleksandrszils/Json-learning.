import random
from unicodedata import numeric

guessed_numbers = []

number = random.randint(1, 1000)

while True:
    guessed_number = int(input(f"Uzmini skaitli no 1 līdz 1000: "))
    guessed_numbers.append(guessed_number)
    
    if guessed_number > number:
        print("Try lower")
    elif guessed_number < number:
        print("Try higher")
    else:
        print("You win!")
        print(f"Number of tries: {len(guessed_numbers)}")
        sum_of_difference = 0
        for n in guessed_numbers:
            sum_of_difference += abs(n - number)
        print(f"Averga edifference: {sum_of_difference /  len(guessed_numbers)}")
        exit()