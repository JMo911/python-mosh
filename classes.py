numbers = [1, 2, 3]


# point.move, draw, get_distance...
# CLASSES ARE PASCAL CASE
class Point:
    def move(self):
        print("move")

    @staticmethod
    def draw():
        print("draw")


# object is an instance of a class.
# class is just the blueprint/template to create an object
point1 = Point()
# point1.move()
point1.x = 90
point1.y = 100
# print(point1.x)
# different instance of the point class
point2 = Point()
point2.x = 1


# print(point2.x)


# CONSTRUCTORS
# points should be initialized with x and y coordinates
class ProperPoint:
    # gets called when we initialize. This is the constructor
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print(f"I sit at X: {self.x}, Y: {self.y}")


proper_point = ProperPoint(10, 20)


# proper_point.draw()


class Person:
    def __init__(self, name: str):
        self.name = name

    def talk(self):
        print(f'{self.name} is speaking')


nancy = Person('Nancy')
# nancy.talk()
drew = Person('Drew')
# drew.talk()


# INHERITANCE
# mechanism for reusing code
#
class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f'{self.name} is barking')
    # def walk(self):
    #     print('walk')


# BAD - REPEATED WALK FUNCTION,
# abstract into Mammal class, and have Dog and Cat inherit it
class Cat(Mammal):
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f'{self.name} is meowing')
    # def walk(self):
    #     print('walk')


dog1 = Dog('sam')
dog1.walk()
dog1.bark()