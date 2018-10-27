from random import randint

rnd_number = randint(1, 100)
while True:
    try:
        user_number = int(input('Guess the number (range 1-100) :'))
    except ValueError:
        print('It\'s not a number')
    else:
        if user_number > rnd_number:
            print('To much')
        elif user_number < rnd_number:
            print('Not enough')
        else:
            print('Congratulations. You guessed the number!')
            break

