class AnimalShelter:
    def __init__(self):
        self.cats = Queue()
        self.dogs = Queue()

    ## Enqueue

    def enqueue(self, animal):
        if animal.type == 'cat':
            self.cats.enqueue(animal)
            return
    # if isinstance(animal, Cat):
    #         self.cats.enqueue(animal)
    #         return
        if animal.type == 'dog':
            self.dogs.enqueue(animal)
            return
        # if isinstance(animal, Dog):
        #     self.dogs.enqueue(animal)
        #     return

        raise Exception('Only Dogs or Cats')


    ## Dequeue


class Dog:
    def __init__(self):
        self.type = 'dog'


class Cat:
    def __init__(self):
        self.type = 'cat'

class Animal:
    def __init__(self, type):
        self.type = type

animal = Dog()

animal_shelter = AnimalShelter()

animal_shelter.enqueue(animal)