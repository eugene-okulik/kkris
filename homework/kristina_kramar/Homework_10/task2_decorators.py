def decor_runcount(func):
    def wrapper(count=1):
        for i in range(count):
            func()
    return wrapper


@decor_runcount
def main_func():
    print('Hello')


main_func(5)
