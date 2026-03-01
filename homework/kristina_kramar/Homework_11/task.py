# task1
class Book:
    book_material = "paper"
    text = True

    def __init__(self, book_name, author, page_num, isbn, reserved):
        self.book_name = book_name
        self.author = author
        self.page_num = page_num
        self.isbn = isbn
        self.reserved = reserved


book1 = Book(
    book_name="Война и мир",
    author="Лев Толстой",
    page_num=1225,
    isbn="978-5-17-118366-3",
    reserved=False
)

book2 = Book(
    book_name="Преступление и наказание",
    author="Фёдор Достоевский",
    page_num=671,
    isbn="978-5-389-07421-7",
    reserved=False
)

book3 = Book(
    book_name="Мастер и Маргарита",
    author="Михаил Булгаков",
    page_num=480,
    isbn="978-5-17-118367-0",
    reserved=False
)

book4 = Book(
    book_name="Евгений Онегин",
    author="Александр Пушкин",
    page_num=224,
    isbn="978-5-17-090355-2",
    reserved=False
)

book5 = Book(
    book_name="Отцы и дети",
    author="Иван Тургенев",
    page_num=288,
    isbn="978-5-17-070435-7",
    reserved=False
)
book5.reserved = True

library = [book1, book2, book3, book4, book5]
for book in library:
    info = (f"Название: {book.book_name}, "
            f"Автор: {book.author}, "
            f"страниц: {book.page_num}, "
            f"материал: {book.book_material}"
    )
    if book.reserved is True:
        print(f"{info}, зарезервирована")
    else:
        print(info)


# task2
class SchoolBook(Book):

    def __init__(self, book_name, author, page_num, isbn, reserved, subject, group, tasks):
        super().__init__(book_name, author, page_num, isbn, reserved)
        self.subject = subject
        self.group = group
        self.tasks = tasks


school_book1 = SchoolBook(
    book_name="Математика. 10 класс",
    author="И.И. Зубарева",
    page_num=320,
    isbn="978-5-09-032113-0",
    reserved=False,
    subject="Математика",
    group="10А",
    tasks=120
)
school_book1.reserved = True

school_book2 = SchoolBook(
    book_name="Физика. 9 класс",
    author="Л.Д. Ландау",
    page_num=400,
    isbn="978-5-04-091451-2",
    reserved=False,
    subject="Физика",
    group="9Б",
    tasks=90
)

school_book3 = SchoolBook(
    book_name="Химия. 11 класс",
    author="А.В. Петров",
    page_num=350,
    isbn="978-5-17-070435-8",
    reserved=False,
    subject="Химия",
    group="11В",
    tasks=100
)

school_library = [school_book1, school_book2, school_book3]
for book in school_library:
    info = (f"Название: {book.book_name}, "
            f"Автор: {book.author}, "
            f"страниц: {book.page_num}, "
            f"предмет: {book.subject}, "
            f"класс: {book.group}"
    )
    if book.reserved is True:
        print(f"{info}, зарезервирована")
    else:
        print(info)
