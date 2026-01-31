person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person

str1 = 'результат операции: 42'
str2 = 'результат операции: 514'
str3 = 'результат работы программы: 9'
index_str1 = str1.index(':')
str1_number = int(str1[index_str1+1:].strip())
print(str1_number + 10)
index_str2 = str2.index(':')
str2_number = int(str2[index_str2+1:].strip())
print(str2_number + 10)
index_str3 = str3.index(':')
str3_number = int(str3[index_str3+1:].strip())
print(str3_number + 10)

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
text = 'Students {0}, study these subjects: {1}'
print(text.format(', '.join(students), ', '.join(subjects)))
