import random
random_number = random.randint(1,10)

correct_guess = False

while not correct_guess:
    user_guess = int(input("Guess a number between 1 and 10!: "))

    if user_guess == random_number:
        print("You got it congratulations! ")
    elif user_guess > random_number:
        print('Your guess is too high! ')
    else:
        print('Your guess is too low! ')
print('Game Over good Job! ')