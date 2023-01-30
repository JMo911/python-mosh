# https://youtu.be/kqtD5dpn9C8
# https://youtu.be/_uQrJ0TkZlc
# age = 20
# price = 19.95
# first_name = "Mosh"
# is_online = True
import math
from ecommerce import shipping
# shipping.calc_shipping()

# patient_first_name = "John"
# patient_last_name = "Smith"
# patient_age = 20
# is_new_patient = True
# not_statement = "" if is_new_patient else "not "
# print(patient_first_name + " " + patient_last_name + " is " + str(patient_age) + " years old. He is " + not_statement + "a new patient")

# USER INPUT
# name = input("What is your name? ")
# print("Hello " + name)

# TYPE CONVERSION
# birth_year = input("Enter your birth year: ")
# age = 2022 - int(birth_year)
# print(age)
# the conversion functions:
# int()
# float()
# bool()
# str()

# calculator exercise -> enter 2 numbers, program prints the sum
# first_num = float(input("First: "))
# second_num = input("Second: ")
# print("Sum: " + str(first_num + float(second_num)))

# STRINGS - technically objects in python
course = 'Python for Beginners'
# print(course.upper()) # creates a new string, does not mutate course
# print(course)
# print(course.find('for')) # returns first index of the string it found, or -1 if nothing found
# print(course.replace('for', '4'))
# print('Python' in course)

# ARITHMETIC OPERATIONS
# print(10 / 3)
# print(10 // 3) #gives a whole number
# print(10 % 3)
# print(10**3) #exponent
# x = 10
# x = x + 3 # or x+=3
# OPERATOR PRECEDENCE.. order of operations
# y = 10 + 3 * 2 #16
# z = (10 + 3) * 2 #26
# COMPARISON OPERATORS
# op_1 = 3 > 2 # True
# print(op_1)
# ==
# >=
# <=
# >
# <
# !=
# LOGICAL OPERATORS
# price = 5
# print(price > 10 and price < 30)
# print(price > 10 or price < 30)
# print(not price > 10)

# IF STATEMENTS
# temperature = 15
# if temperature > 30:
#     print("it's a hot day at " + str(temperature) + " degrees")
#     print('drink h20')
# elif temperature > 20: # (20, 30]
#     print("it's a nice day")
# else:
#     print("it's cooollldddd")
#
# print("Done")


# Weight converter program
# weight = float(input("Weight: "))
# kg_or_lb = input("(K)g or (L)bs: ")
# if kg_or_lb.lower() == "l":
#     print("Weight in Kg: " + str(weight * .453592))
# else:
#     print("Weight in Lbs: " + str(weight * 2.20462))

# WHILE LOOPS
# i = 1
# while i <= 1_000:
#     print(i)
#     i+=1
# i = 1
# while i <= 10:
#     print(i * '*') #multiply a number by a string, it will repeat that string based on the value of the number
#     i+=1

# LISTS - a complex type
# primitive types
#     1 - int
#     1.1 - float
#     True - boolean
#     'a' - string
# names = ["John", "Bob", "Mosh", "Sam", "Mary"] #List
# # print(names)
# # print(names[0])
# # print(names[-1])
# names[0] = "Jon"
# print(names[0:3]) # last index is not inclusive
# LIST METHODS
# numbers = [1,2,3,4]
# numbers.append(5)
# print(numbers)
# numbers.insert(3, 3.5)
# print(numbers)
# numbers.remove(3)
# print(numbers)
# numbers.clear()
# print(numbers)
# print(1 in numbers)
# print(len(numbers))


# FOR LOOPS
# numbers = [1,2,3,4,5]
# print(numbers)
# for num in numbers:
#     print(num)
#
# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i+=1

# THE RANGE FUNCTION
# used to generate a sequence of numbers
# numbers = range(5)
# print(numbers)
# for num in numbers:
#     print(num)

# numbers_2 = range(5,10)
# for num2 in numbers_2:
#     print(num2)

# numbers_3 = range(5, 10, 2)
# for num3 in numbers_3:
#     print(num3)


# TUPLES -> immutable
numbers = (1, 2, 3, 3)
# numbers[0] = 3 # this errors because it's immutable
numbers.count(3) # returns number of occurrences of an element.. 2
numbers.index(2) #returns index of first occurence of an element
# numbers.__add__() #double underscores are magic methods

#for loops
# for item in 'Python':
    # print(item)

# for name in ['Mosh', 'John', 'Sarah']:
#     print(name)

# for num in range(10,20, 2):
#     print(num)
price_sum = 0
prices = [10, 20, 30]
for price in prices:
    price_sum += price

# print(price_sum)

# NESTED LOOPS
# for x in range(4):
#     for y in range(3):
        # print(f'({x}, {y})')

# numbers_x = [5, 2, 5, 2, 2]
# for num in numbers_x:
#     my_string = ''
#     for x in range(num):
#         my_string += 'x'
#     print(my_string)

# LISTS
# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# names[0] = 'Jon'
# print(names[0:-2])  # prints ['John', 'Bob', 'Mosh']
# print(names[2:])    # ['Mosh', 'Sarah', 'Mary']
# print(names[:2])    # ['John', 'Bob']

# numbers = [0, 5, -3, 12, -6, 10]
#
# if len(numbers) == 0:
#     print("invalid list")
# else:
#     max_number = numbers[0]
#     for num in numbers:
#         if num > max_number:
#             max_number = num
#     print(max_number)

# 2D Lists.. two dimensional
# [
#   1 2 3
#   4 5 6
#   7 8 9
# ]
# 3x3 matrix in math ^^
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# matrix[0][2] = 10
# # print(matrix[0][2])
# for row in matrix:
#     for num in row:
#         print(num)

# LIST METHODS
# numbers = [5, 2, 1, 7, 1, 4]
# numbers_2 = numbers.copy()
# numbers.insert(0, 10)
# numbers.remove(5)
# print(numbers.pop())
# print(numbers.index(1))
# print(numbers.count(1))
# print(numbers)
# numbers.clear()
# print(numbers_2)

# remove dupes
# numbers = [5, 2, 1, 7, 1, 4, 4, 4]
# numbers_without_dupes = []
# numbers_dict = {}
# for num in numbers:
#     if not numbers_dict.get(num):
#         numbers_without_dupes.append(num)
#         numbers_dict.setdefault(num, 1)
#
# print(numbers_dict)
# print(numbers_without_dupes)
# INSTRUCTOR ANSWER
# numbers = [5, 2, 1, 7, 1, 4, 4, 4]
# uniques = []
# for num in numbers:
#     if num not in uniques:
#         uniques.append(num)
#
# print(uniques)


# UNPACKING
# coordinates = (1, 2, 3)
# x, y, z = coordinates
#
# print(f'x: {x}, y: {y}, z: {z}')
#
# numbers = [1, 2, 3]
# a, b, c = numbers
# print(f'a: {a}, b: {b}, c: {c}')

message = input(">")
words = message.split(' ')
emojis = {
    ':)': '😀',
    ':(': '☹️'
}

output = ''
for word in words:
    output += f'{emojis.get(word, word)} '
    # if emojis.get(word):
    #     output += f'{emojis.get(word)} '
    # else:
    #     output += f'{word} '
print(output)



