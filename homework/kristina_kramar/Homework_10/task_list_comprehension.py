PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_price_list = [str.split() for str in PRICE_LIST.splitlines()]
dict_price_list = {key: int(value[:-1]) for key, value in new_price_list}
print(dict_price_list)
