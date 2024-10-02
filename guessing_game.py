import random

print("Welcome to the guessing game")

lowest_number = 0
highest_number = 20

answer = random.randint(lowest_number,highest_number)
#print(answer)
isrunning = True
while isrunning == True:
    guess = int(input("Please enter your guess: "))
    if guess > answer:
        print("You've guessed too high, please guess lower")
    elif guess < answer:
        print("You've guessed too low, please guess higher")
    else:
        print(f"You've guessed it correct, the answer was {answer}")
        break
print("Thank you for playing!")

