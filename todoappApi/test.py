# cost_price = 500
# selling_price = 500

# profit = selling_price - cost_price
# print('your profit is ' + str(profit))

# loss = cost_price - selling_price
# print('your loss is ' + str(loss))

# data manipulation in python
# strings
from typing import Counter


first_name = "joseph"
second_name = "Alex"
age = 100

# adding strings together
full_name = first_name + ' ' + second_name
print(full_name)

# formatted strings in python
full_name = f'{first_name} {second_name}'
statement = 'My name is ' + full_name + ', i am ' + str(age) + ' years old.'
fstatement =  f'My name is {full_name}, i am {age} years old.'
print(full_name)
print(statement)
print(fstatement)

# strings repetition

name = 'joseph'
print(name * 4)

# string modification
# title cassing with strings
titled_name = name.title()
print(titled_name)
print(fstatement.title())

# upper case
caps_name = name.upper()
print(caps_name)
print(fstatement.upper())
print(fstatement)

# lower case
low_name = fstatement.lower()
print(low_name)

# center a string
# name.center

# count the number char in a string 
name_length = len(name)
print(name_length)

# count the number of occurance of a char in a string
name_count = name.count('o')
print(name_count)

# indexing in python
statement = 'my name is sarah'
print(statement[0])
print(statement[1])
print(statement[2])
print(statement[3])
print(statement[4])
print(statement[5])
print(len(statement))

# slicing of an iterable
# variable_name[start_index:end_index + 1]  forward slicing
# varaiable_name[-start_index-1: -end_index] backward slicing

print(statement[-3:])

# operators in python
# arithmetic operators: +, -, *, /, **, % 
# relational operators: <, >, <=, >=, ==, !=
# logical operators: is, in, and, or, not
# bitwise operators: ^, !^, ||, !||, 
# assignment operators: =, +=, -=, /=, *=, %=

bool = True
bool = False
value = None
