results = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]


def sumstrnum(str, num=10):
    return int(str.split()[-1]) + num


for str in results:
    print(sumstrnum(str))
