import random


def draw():
    drawn = random.sample(range(1, 50), 6)
    return sorted(drawn)


def validation(num, array):
    try:
        num = int(num)
    except ValueError:
        return False
    else:
        if num not in array and 0 < num < 50:
            return num


def predict():
    bet = []
    i = 1
    while i < 7:
        number = input('Predict {} number: '.format(i))
        if validation(number, bet):
            bet.append(int(number))
            i += 1
        else:
            print('Wrong input, try again')
    return sorted(bet)


def check_win(bet_numbers, win_numbers):
    rv = 0
    for i in range(6):
        if bet_numbers[i] in win_numbers:
            rv += 1
    if rv > 2:
        print('$$$ Congratulations! You guessed {} numbers! $$$'.format(rv))
    else:
        print('Try again... You guessed {} numbers'.format(rv))


if __name__ == '__main__':
    user_nums = predict()
    drawn_nums = draw()
    print('Your numbers: ' + ' '.join(map(str, user_nums)))
    print('Drawn_numbers: ' + ' '.join(map(str, drawn_nums)))
    check_win(user_nums, drawn_nums)
