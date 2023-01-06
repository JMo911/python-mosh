customer = {
    'name': 'John Smith',
    'age': 30,
    'Phone': 1234,
    'is_verified': True
}

customer['name'] = 'Jack Smith'
customer['birthdate'] = 'jan 1 1980'
# print(customer.get('name'))
# print(customer)

word_nums = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four'
}

output = ''
for digit in str(customer.get('Phone')):
    output += f'{word_nums.get(int(digit))} '

# print(output)
