import random

random_number = random.randint(0,5)
correct_answer = False
while not correct_answer:
    user_input = int(input("Enter a random number between 0 and 5:"))
    if user_input == random_number:
        print('Congrats you guessed it! ')
    elif user_input > random_number:
        print('Too high, Try again! ')
    else:
        print('Too low, try again! ')
print('Thanks for playing! ')