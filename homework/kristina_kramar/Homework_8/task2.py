import sys
sys.set_int_max_str_digits(30000)


def gen_fibonacci(limit):
    n1 = 0
    n2 = 1
    count = 1
    while count <= limit:
        yield count, n1
        n = n1 + n2
        n1 = n2
        n2 = n
        count += 1


for index, number in gen_fibonacci(100000):
    if index in (5, 200, 1000, 100000):
        print(str(number)[0:45])
