import doctest


class Person:
    def __init__(self, name: str, age: int, gender: str):
        """
        Создание и подготовка к работе объекта "Человек".
        :param name: Имя человека
        :param age: Возраст человека
        :param gender: Пол человека ('Male', 'Female', "N/A")
        Примеры:
        >>> person = Person("Taylor Swift", 25, "Female")
        """
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Имя должно быть строкой")
        self.name = name

        if not isinstance(age, int) or age < 0:
            raise ValueError("Возраст должен быть положительным целым числом")
        self.age = age

        if gender not in ['Male', 'Female', 'N/A']:
            raise ValueError("Пол должен быть 'Male', 'Female' или 'N/A'")
        self.gender = gender

    def celebrate_birthday(self) -> None:
        """
        Празднование дня рождения человека.
        Примеры:
        >>> person = Person("Taylor Swift", 25, "Female")
        >>> person.celebrate_birthday()
        """
        ...

    def change_name(self, new_name: str) -> None:
        """
        Изменение имени человека.
        :param new_name: Новое имя человека
        :raise ValueError: Если имя не строка или пустое
        Примеры:
        >>> person = Person("Taylor Swift", 25, "Female")
        >>> person.change_name("Jane Doe")
        """
        ...

    def introduce(self) -> None:
        """
        Представление человека.
        :return: Имя человека
        Примеры:
        >>> person = Person("Taylor Swift", 25, "Female")
        >>> person.introduce()
        """
        ...

class Book:
    def __init__(self, title: str, author: str, genre: str):
        """
        Создание и подготовка к работе объекта "Книга".
        :param title: Название книги
        :param author: Автор книги
        :param genre: Жанр книги
        :raise ValueError: Если название, автор или жанр не являются строкой
        Примеры:
        >>> book = Book("War and Peace", "Lev Tolstoy", "Epic Novel")
        """
        if not isinstance(title, str) or not isinstance(author, str) or not isinstance(genre, str):
            raise ValueError("Название, автор и жанр книги должны быть строками")
        self.title = title
        self.author = author
        self.genre = genre

    def read_book(self) -> None:
        """
        Чтение книги.
        Примеры:
        >>> book = Book("War and Peace", "Lev Tolstoy", "Epic Novel")
        >>> book.read_book()
        """
        ...

    def recommend_book(self) -> None:
        """
        Рекомендация книги.
        Примеры:
        >>> book = Book("War and Peace", "Lev Tolstoy", "Epic Novel")
        >>> book.recommend_book()
        """
        ...

class Smartphone:
    def __init__(self, brand: str, model: str, os: str):
        """
        Создание и подготовка к работе объекта "Смартфон".
        :param brand: Марка смартфона
        :param model: Модель смартфона
        :param os: Операционная система смартфона
        :raise ValueError: Если марка, модель или операционная система не являются строкой
        Примеры:
        >>> iphone = Smartphone("Apple", "iPhone 13", "iOS")
        """
        if not isinstance(brand, str) or not isinstance(model, str) or not isinstance(os, str):
            raise ValueError("Марка, модель и операционная система смартфона должны быть строками")
        self.brand = brand
        self.model = model
        self.os = os

    def make_call(self) -> None:
        """
        Совершение звонка со смартфона.
        Примеры:
        >>> iphone = Smartphone("Apple", "iPhone 13", "iOS")
        >>> iphone.make_call()
        """
        ...

    def install_app(self, app_name: str) -> None:
        """
        Установка приложения на смартфон.
        :param app_name: Название приложения для установки
        :raise ValueError: Если название приложения не является строкой
        Примеры:
        >>> iphone = Smartphone("Apple", "iPhone 13", "iOS")
        >>> iphone.install_app("Messenger")
        """
        ...

if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest