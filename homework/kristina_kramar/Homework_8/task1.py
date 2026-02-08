import random

salary = int(input('Enter your salary in USD: '))
bonus = random.choice([True, False])
if bonus is True:
    bonus_amount = random.randint(100, 1000)
    print(f'You will get a bonus! Your salary + bonus: ${salary + bonus_amount}')
else:
    print(f'No bonuses this quarter:( Your salary: ${salary}')
