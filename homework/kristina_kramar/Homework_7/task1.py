number = 135
while True:
    user_input = int(input('Guess the number:'))
    if user_input == number:
        print('Congratulations! You guessed right!')
        break
    else:
        print('Try again')
