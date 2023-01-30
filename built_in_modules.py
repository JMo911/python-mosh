# all the modules built into python: https://docs.python.org/3/py-modindex.html
import random
# for i in range(3):
#     print(random.random())
#     print(random.randint(10,20))

# members = ['John', 'Mary', 'Bob', 'Mosh']
# leader = random.choice(members)
# print(leader)

# roll a dice
# dice_values = [1,2,3,4,5,6]
# dice class, with method 'roll' that outputs a tuple (1,1).. (3,1).. read only list

class Dice:
    def roll(self) -> tuple:
        return (random.randint(1,6), random.randint(1,6))


my_dice = Dice()
print(my_dice.roll())