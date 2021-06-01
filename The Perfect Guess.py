import random

guess_count = 0

print('''############################
Welcome to the Perfect Guess
############################''')

num = random.randint(1, 10)
print('\nThe number is between 1-10(both included).\n')
game_choice = input('Do you want to continiue, [y/n]: \n')

while game_choice == 'y':
    guess_count += 1
    user = int(input('\nGuess the number:\n'))

    if user > num:
        print('A small number please.')

    elif user < num:
        print('A large number please.')

    elif user == num:
        print(''''BINGO!!!
Your answer is right!
You are awesome!\n''')
        print(f'Number of gusses took: {guess_count}\n')
        break

print("Thank you for playing our game.")
print('Have a nice day!')