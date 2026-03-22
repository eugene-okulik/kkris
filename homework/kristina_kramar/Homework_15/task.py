import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)
cursor = db.cursor(dictionary=True)

# создание студента
cursor.execute("INSERT INTO students (name, second_name) VALUES (%s, %s)", ('Lukas', 'Karn'))
student_id = cursor.lastrowid

# создание книг
cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)", ('BookNmb1', student_id))
cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)", ('BookNmb2', student_id))

# создание группы
cursor.execute("INSERT INTO `groups` (title) VALUES ('A777')")
group_id = cursor.lastrowid
cursor.execute("UPDATE students SET group_id=%s where id=%s", (group_id, student_id))

# создание предметов
cursor.execute("INSERT INTO subjects (title) VALUES ('Matan')")
subject1_id = cursor.lastrowid
cursor.execute("INSERT INTO subjects (title) VALUES ('Biophysics')")
subject2_id = cursor.lastrowid

# создание уроков
lesson_ids = []

for lesson in [
    ('Lesson1', subject1_id),
    ('Lesson2', subject1_id),
    ('Lesson1', subject2_id),
    ('Lesson2', subject2_id)
]:
    cursor.execute(
        "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", lesson
    )
    lesson_ids.append(cursor.lastrowid)

# проставление оценок
insert_query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
data = [
    ('5', lesson_ids[0], student_id),
    ('4', lesson_ids[1], student_id),
    ('4', lesson_ids[2], student_id),
    ('5', lesson_ids[3], student_id)
]
cursor.executemany(insert_query, data)

db.commit()

cursor.execute("SELECT * FROM marks where student_id=%s", (student_id))
print(cursor.fetchall())

cursor.execute("SELECT * FROM books where taken_by_student_id=%s", (student_id))
print(cursor.fetchall())

cursor.execute('''
    select students.name, students.second_name, group_concat(books.title) as book_title,
    `groups`.id as group_id, marks.value, lessons.title, subjects.title
    from students
    join `groups`on students.group_id=`groups`.id
    join books on students.id=books.taken_by_student_id
    join marks on students.id=marks.student_id
    join lessons on marks.lesson_id=lessons.id
    join subjects on lessons.subject_id=subjects.id
    where students.id=%s group by students.id, marks.id;
    ''',
    (student_id)
)
print(cursor.fetchall())

db.close()
