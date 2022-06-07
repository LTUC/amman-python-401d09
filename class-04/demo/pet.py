from abc import ABC, abstractmethod

class Pet(ABC):
    count = 0
    def __init__(self, name):
        self.name = name
        Pet.count += 1
        # self.speak = speak

    def greet(self):
        print(f"Hi, my name is {self.name}")

    @abstractmethod
    def speak(self):
        pass

    @classmethod
    def get_count(cls):
        return cls.count

class Dog(Pet):
    def speak(self):
        print("Whoooof")

    @staticmethod
    def get_char():
        print("Likes to jump")

    def __str__(self):
        return self.name


class Cat(Pet):
    def speak(self):
        print("Meoow")

    @staticmethod
    def get_char():
        print("Likes to sleep")

class Hamaster(Pet):
    def speak(self):
        pass


# oscar = Pet('Oscar')
# sherry = Pet('Sherry')

alex = Dog('Alex')
print(alex.greet())
boxer = Dog('Boxer')
print(boxer)
# print(boxer.count)
# print(oscar.name)

# oscar.greet()
#
# print(alex.name)
# alex.greet()

# alex.speak()
#
# alex.age = 12
#
# print(alex.age)
# print(boxer.age)

# shelly = Hamaster("Shelly")
# shelly.speak()

# alex.get_char()
# Dog.get_char()
# Cat.get_char()

# print(Pet.get_count())
#
# sherry = Cat('Sherry')
#
# print(Pet.get_count())


# def test_shift_arr(arr):
#     actual = shift(arr)
#
#
# def test_binary_search(arr):
#     actual = binary_search(arr)
#
#
# @pytest.fixture
# def arr():
#     return [1,2,3,4,5,6,7,8,9,10]
