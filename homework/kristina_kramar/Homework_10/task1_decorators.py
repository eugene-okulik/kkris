def decor_finished(func):
    def wrapper():
        func()
        print(f'function {func.__name__} finished')
    return wrapper


@decor_finished
def main_func():
    print('Main function')


main_func()
