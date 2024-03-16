import random
name = input("What is your name? ")
self = input('Hello '+name+', how are you? ')
print('That is good to know '+name+'!')
game = input("You will play this game  "+name+" !"+"Press ENTER to continue")
random_number = random.randint(0,5)
correct_answer = False
while not correct_answer:
    user_input = int(input('Enter a number between 0 and 5!'))
    if user_input == random_number:
        print('Good Guess! ')
    elif user_input > random_number:
        print('Too high of a number try again! ')
    else:
        print('Too Low try to go higher! ')
print('That is everything good job!')