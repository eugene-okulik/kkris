import os
import mysql.connector as mysql
import dotenv
import csv

homework_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(file_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    data = []
    for row in file_data:
        data.append(row)

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

cursor.execute('''
select
students.name as name,
students.second_name as second_name,
`groups`.title as group_title,
books.title as book_title,
subjects.title as subject_title,
lessons.title as lesson_title,
marks.value as mark_value
from students 
join `groups`on students.group_id=`groups`.id
join books on students.id=books.taken_by_student_id 
join marks on students.id=marks.student_id
join lessons on marks.lesson_id=lessons.id 
join subjects on lessons.subject_id=subjects.id
GROUP BY students.id, marks.id, books.title
'''
)

db_data = cursor.fetchall()

for row in data:
    if row not in db_data:
        print('This row is not found in db:')
        print(row)

db.close()
