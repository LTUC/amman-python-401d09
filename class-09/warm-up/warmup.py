

class Duck:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __eq__(self, other):

        """some dreamy method that "magically" returns True if ducks are "equal"
        """

    # equality logic goes here
        return self.name == other.name and self.category == other.category


obj1 = Duck('alex', 'wild')
obj2 = Duck('alex', 'wild')

print(obj1 != obj2)