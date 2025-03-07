from unittest.mock import Mock


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


class Bookstore:
    def __init__(self, book):
        self.book = book

    def display_book_info(self):
        return f"Название: {self.book.title}, Автор: {self.book.author}, Цена: {self.book.price}"


def test_display_book_info():
    book_mock = Mock()
    # установи атрибуту мок-объекту book_mock
    book_mock.title = 'Моби Дик'
    book_mock.author = 'Герман Мелвилл'
    book_mock.price = 150


# Создали объект класса Bookstore и передали в него мок-объект
    bookstore = Bookstore(book_mock)

# Протестировали метод display_book_info()
    assert bookstore.display_book_info() == "Название: Моби Дик, Автор: Герман Мелвилл, Цена: 150"