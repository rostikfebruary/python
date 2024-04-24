# FIRST TASK

class Rectangle:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = self.x * self.y

    def __add__(self, other):
        return self.area + other.area

    def __sub__(self, other):
        return self.area - other.area

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __gt__(self, other):
        return self.area > other.area

    def __lt__(self, other):
        return self.area < other.area

    def __len__(self):
        return self.x + self.y


rectangle1 = Rectangle(3, 3)

rectangle2 = Rectangle(1, 5)

print(rectangle1.__add__(rectangle2))
print(rectangle1.__sub__(rectangle2))
print(rectangle1.__eq__(rectangle2))
print(rectangle1.__ne__(rectangle2))
print(rectangle1.__gt__(rectangle2))
print(rectangle1.__lt__(rectangle2))
print(rectangle1.__len__())


# SECOND TASK


class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):
    count = 0

    def __init__(self, name, age, foot):
        super().__init__(name, age)
        self.foot = foot
        Cinderella.count += 1

    def __str__(self):
        return str(self.__dict__)

    @classmethod
    def to_count(cls):
        return cls.count


class Prince(Human):

    def __init__(self, name, age, found):
        super().__init__(name, age)
        self.found = found

    def found_size(self, cinderellas: list[Cinderella]) -> None:
        for cinderella in cinderellas:
            if cinderella.foot == self.found:
                print(cinderella)
                return

    def __str__(self):
        return str(self.__dict__)


cinderella_dict: list[Cinderella] = [
    Cinderella('Liza', 20, 35),
    Cinderella('Marta', 15, 45),
    Cinderella('Anya', 23, 36),
    Cinderella('Olivia', 18, 34),
    Cinderella('Alina', 30, 34),
    Cinderella('Baiden', 60, 40)
]

prince = Prince('Jo', 37, 40)
print(prince)
prince.found_size(cinderella_dict)
print(Cinderella.to_count())

# TASK 3


# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()

from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self):
        print(self)


# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable


class Book(Printable):

    def __init__(self, name):
        self.name = name


class Magazine(Printable):

    def __init__(self, name):
        self.name = name
