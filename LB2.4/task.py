class Animal:
    """
    Базовый класс "Животное"
    """

    def __init__(self, name: str, species: str):
        """
        Создание объекта "Animal".
        Args:
            name (str): Имя животного.
            species (str): Вид животного.
        """
        self.name = name
        self._species = species  # Protected тк не должно изменяться

    def make_sound(self) -> str:
        """
        Издать звук.
        Returns:
            str: Строка, передающая звук, издаваемый животным.
        """
        return "Звук животного"

    def move(self) -> str:
        """
        Начать движение.
        Returns:
            str: Строка, описывающая движение животного.
        """
        return f"{self._species} движется"

    def __str__(self) -> str:
        """
        Вернуть строку, представляющую животное.
        Returns:
            str: Строка представляющая животное.
        """
        return f"{self.name} - {self._species}"

    def __repr__(self) -> str:
        """
        Вернуть строку, представляющую объект класса "Animal".
        Returns:
            str: Строка, представляющая объект класса "Animal".
        """
        return f"Animal(name={self.name}, species={self._species})"


class Dog(Animal):
    """
    Дочерний класс "Dog", наследуемый от "Animal"
    """

    def __init__(self, name: str, breed: str):
        """
        Создание объекта класс "Dog"
        Args:
            name (str): Имя собаки.
            breed (str): Порода собаки.
        """
        super().__init__(name, species="Dog")
        self._breed = breed  # Protected тк не должно изменяться

    def make_sound(self) -> str:
        """
        Издать звук
        Перегруженный метод для издания звука "Гав"
        Returns:
            str: Строка звука, издаваемого собакой.
        """
        return "Гав!"

    def wag_tail(self) -> str:
        """
        Повилять хвостом.
        Returns:
            str: Строка, описывающая виляние хвостом.
        """
        return f"{self.name} виляет хвостом"

    def __str__(self) -> str:
        """
        Вернуть строку, представляющую собаку.
        Перегруженный метод для предоставления более детальной информации о собаке, включая имя, вид и породу.
        Returns:
            str: Строка, представляющая собаку.
        """
        return f"{self.name} - {self._species} ({self._breed})"

    def __repr__(self) -> str:
        """
        Вернуть строку, представляющую объект класса "Dog".
        Перегруженный метод для предоставления более информативного представления объекта класса "Dog".
        Returns:
            str: Строка, представляющая объект класса "Dog".
        """
        return f"Dog(name={self.name}, breed={self._breed})"

if __name__ == "__main__":
    dog = Dog("Кейси", "Овчарка")
    print(dog.move())