import random

for i in range(0,6):
    print(random.randint(1,6))

list = ['Yousef', "Ahmad", "Mohammad", 'Lama']

print(random.choice(list))

class GameLogic:
    def __init__(self):
        pass

    @staticmethod
    def role_dic(num):
        return [random.randint(1,6) for i in range(0,num)]

print(GameLogic.role_dic(6))
