import os
import datetime

homework_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')
print(file_path)

with open(file_path, 'r', encoding='utf-8') as data:
    only_dates = []
    for line in data:
        date = line.split(' - ')[0]
        date = date.split('. ')[1]
        date = datetime.datetime.fromisoformat(date)
        only_dates.append(date)

print(only_dates[0] + datetime.timedelta(weeks=1))
print(only_dates[1].strftime("%A"))
print((datetime.datetime.now() - only_dates[2]).days)
