class InvalidOperationError(Exception):
    pass


class Stream:
    def __itin__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open.")
        self.opened = True

    def open(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")

    # class Flyer():
    #     pass

    # class Swimmer():
    #     pass

    # class FlyingFish(Flyer, Swimmer):
    #     pass

    # class Employee():
    #     def greet(self):
    #         print("Employee Greet")

    # class Person():
    #     def greet(self):
    #         print("Person Greet")

    # class Manager(Employee, Person):
    #     pass

    # manager = Manager()
    # manager.greet()

    # class Animal:
    #     def __init__(self):
    #         self.age = 1

    #     def eat(self):
    #         print("eat")

    # class Mammal(Animal):
    #     def __init__(self):
    #         super().__init__()
    #         self.weight = 2

    #     def walk(self):
    #         print("walk")

    # class Fish(Animal):
    #     def swim(self):
    #         print("swim")

    # class Bird(Animal):
    #     def fly(self):
    #         print("fly")

    # m = Mammal()
    # print(m.age)
    # print(m.weight)

    # class Product:
    #     def __init__(self, price):
    #         self.price = price

    #     @property
    #     def price(self):
    #         return self.__price

    #     @price.setter
    #     def price(self, value):
    #         if value < 0:
    #             raise ValueError("Price cannot be negative.")
    #         self.__price = value

    # product = Product(10)
    # print(product.price)

    # class TagCloud:
    #     def __init__(self):
    #         self.__tags = {}

    #     def add(self, tag):
    #         self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    #     def __getitem__(self, tag):
    #         return self.__tags.get(tag.lower(), 0)

    #     def __setitem__(self, tag, count):
    #         self.__tags[tag.lower()] = count

    #     def __len__(self):
    #         return len(self.__tags)

    #     def __iter__(self):
    #         return iter(self.__tags)

    # cloud = TagCloud()
    # print(cloud._TagCloud__tags)

    # class Point:
    #     default_color = "red"

    #     def __init__(self, x, y):
    #         self.x = x
    #         self.y = y

    #     def __str__(self):
    #         return f"({self.x}, {self.y})"

    #     def __eq__(self, other):
    #         return self.x == other.x and self.y == other.y

    #     def __gt__(self, other):
    #         return self.x > other.x and self.y > other.y

    #     def __add__(self, other):
    #         return Point(self.x + other.x, self.y + other.y)

    #     @classmethod
    #     def zero(cls):
    #         return cls(0, 0)

    #     def draw(self):
    #         print(f"Point ({self.x}, {self.y})")

    # point1 = Point(10, 20)
    # point2 = Point(1, 2)
    # combined = point1 + point2
    # print(combined.x)

    # Point.default_color = "yellow"
    # point = Point(1, 2)
    # print(point.default_color)
    # print(Point.default_color)
    # point.draw()

    # another = Point(3, 4)
    # print(another.default_color)
    # another.draw()
