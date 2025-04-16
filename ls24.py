# class Square:  # назву класу пишемо через CamelCase або CapWords
#     def __init__(self, side_length: int | float):
#         self.side_length = side_length
#
#     def area(self):
#         areas = self.side_length ** 2
#
#         return areas
#
#     def perimetr(self):
#         perimetr = self.side_length * 4
#         return perimetr
#
#
# kvadrat = Square(5)
#
# print(kvadrat.area())
# print(kvadrat.perimetr())

class Library:
    def __init__(self):
        self.books = {}  # автор: [книга, книга]

    def add_book(self, autor, title):
        if autor not in self.books:
            self.books[autor] = [title]
        else:
            self.books[autor].append(title)

    def find_book_by_title(self, title):
        for autr_name, autor_list in self.books.items():
            if title in autor_list:
                print(f'Книгу було знайдено у автора {autr_name}')
                return

        print(f'Книги у бібліотеці немає!')

    def print_all_books(self):
        for autr_name, autor_list in self.books.items():
            print(f'-----Автор: {autr_name}-----')
            print('\n'.join(autor_list))

# square_1 = Square(10)
# square_2 = Square(25)
#
# print(square_1.area())
# print(square_2.perimetr())

my_library = Library()

my_library.add_book('С. Кінг', "Сяйво")
my_library.add_book("Д. Браун", "Джерело")
my_library.add_book('С. Кінг', "Воно")
my_library.add_book('Й. Гетте', "Фауст")
my_library.add_book("Д. Браун", "Код Да Вінчі")

my_library.print_all_books()

my_library.find_book_by_title('Фауст')
my_library.find_book_by_title('Кобзар')