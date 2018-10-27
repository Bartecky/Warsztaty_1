def guess(min, max):
    return int((max - min) / 2) + min


def input_validate(message):
    while True:
        answer = input(message)
        if answer.lower() == 'y' or answer.lower() == 'n':
            break
        else:
            print('Wrong input')
    return answer


def game():
    print('Think a number of range 1 - 1000 and I\'ll guess it!')
    min_value = 1
    max_value = 1000
    while True:
        bet = guess(min_value, max_value)
        print('Guess: {}'.format(bet))
        answer = input_validate('Am i right?  [y/n] :')
        if answer.lower() == 'y':
            print('I knew it!')
            break
        else:
            answer = input_validate('To much?   [y/n] :')
            if answer.lower() == 'y':
                max_value = bet
            else:
                answer = input_validate('Not enough?    [y/n] :')
                if answer.lower() == 'y':
                    min_value = bet
                else:
                    print('Don\'t cheat')


if __name__ == '__main__':
    game()
