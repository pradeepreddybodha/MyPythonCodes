import random
li = range(1, 11)
play_game = 'y'
while play_game == 'y':
    rand_numb = random.sample(li, 1)
    user_guess = input("Guess a number between 1 and 10:")
    if rand_numb[0] == int(user_guess):
        print("You have guessed the number correctly")
        play_game = input("Do you want to continue y/n:")
    else:
        pass
