# parameters are the placeholders we define in a function signature

def greet_user(first_name: str, last_name: str):
    print(f'Hi there {first_name} {last_name}!')
    print('Welcome aboard')


# arguments are the values you supply to the function when invoking
greet_user("James", 'Mosh')

# positional arguments -> the order matters
# keyword arguments -> order doesn't matter. Always come after positional arguments
# when you invoke, specify the name of the param you're targeting
greet_user(last_name="Mosh", first_name='James')
greet_user('James', last_name='Mosh')


# below is easier to read than calc_cost(50, 5, 0.1)
# calc_cost(total=50, shipping=5, discount=0.1)


# RETURN VALUES
# by default all python functions return the value 'None'
def square(number: int):
    print(number * number)


print(f'result is: {square(3)}')


# reusable emoji function exercise
def emojify_message(message: str) -> str:
    words = message.split(' ')
    output = ''
    emojis = {
        ':)': '😀',
        ':(': '☹️'
    }
    for word in words:
        output += f'{emojis.get(word, word)} '
    return output


print(emojify_message(input(">")))
