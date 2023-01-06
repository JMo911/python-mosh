try:
    age = int(input('Age: '))  # throws exception if user inputs a string
    income = 20000
    risk = income / age  # throws exception if divisor is 0
    print(age)
except ValueError:
    print('invalid value')
except ZeroDivisionError:
    print(f'{age} is an invalid age')

# use comments to explain hows and whys.. not whats.. only assumptions/nuance that's not defined clearly by your code
