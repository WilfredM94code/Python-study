import re
import copy
import datetime
import random
from ntpath import join
title_123 = '''-----------------------------------------------------------------
------------------------- 123 th Excercise -----------------------
----------------------- Program to input and ---------------------
------------------------- sums two values ------------------------
------------------------------------------------------------------'''

excercise_123 = '''Write a program that takes two numbers from the user, adds them together and shows the result to the user'''

print(title_123)
print(excercise_123)


def inp_covertor_a():
    while True:
        arg = input('Please input a number\n')
        try:
            # If the value is zero or if the argument cannot be converted it will rise an exception
            # If the value float(arg) - int(float(arg)) == 0 it means that the input has no
            # decimal value
            if float(arg) - int(float(arg)) != 0:
                arg = float(arg)
            else:
                raise ValueError
        except:
            try:
                # If the ValueError exception was raised or if there's no difference between the transformation of the value
                # between a float or an interger it will try to convert it to a integer
                arg = int(float(arg))
            except:
                # If the value cannot be converten into a either a floar or a interger the input will be 'False'
                arg = None
        # If the value is False it means that the input cannot be converted into a numerical value
        if arg != None:
            return arg
        print('Input an useful value\n')


value_a = inp_covertor_a()
value_b = inp_covertor_a()
print(f'Sumed values = {value_a + value_b}')

title_124 = '''-----------------------------------------------------------------
------------------------- 124 th Excercise -----------------------
----------------------- Program to input and ---------------------
--------------------- displays a square root ---------------------
------------------------------------------------------------------'''

excercise_124 = '''Write a program that takes two numbers from the user, adds them together and shows the result to the user'''

print(title_124)
print(excercise_124)

value_a = inp_covertor_a()
print(f'Squared root of {value_a} is {value_a**(1/2)}')

title_125 = '''-----------------------------------------------------------------
------------------------- 125 th Excercise -----------------------
--------------------- Program to that displays -------------------
--------------------- the area of a triangle ---------------------
------------------------------------------------------------------'''

excercise_125 = '''That takes the dimentions of three sides of a triangle from the user, then using the Herons
formula, calculates the area of a triangle and displays the result to the user'''

print(title_125)
print(excercise_125)

value_a = inp_covertor_a()
value_b = inp_covertor_a()
value_c = inp_covertor_a()

semi_perimeter = (value_a + value_b + value_c) / 2
triangle_area = (semi_perimeter * (semi_perimeter - value_a) *
                 (semi_perimeter - value_b) * semi_perimeter - value_c) ** (1/2)

title_126 = '''-----------------------------------------------------------------
------------------------- 126 th Excercise -----------------------
------------------- Program to solve quadratic -------------------
---------------------------- equations ---------------------------
------------------------------------------------------------------'''

excercise_126 = '''Write a program that takes user inputs for three constants of a quadratic 
equation, solves the equation and displays the solutions'''

print(title_126)
print(excercise_126)


def inp_covertor_b():
    while True:
        arg = input('Please input a number\n')
        try:
            # If the value is zero or if the argument cannot be converted it will rise an exception
            # If the value float(arg) - int(float(arg)) == 0 it means that the input has no
            # decimal value
            if float(arg) - int(float(arg)) != 0:
                arg = float(arg)
            else:
                raise ValueError
        except:
            try:
                # If the ValueError exception was raised or if there's no difference between the transformation of the value
                # between a float or an interger it will try to convert it to a integer
                arg = int(float(arg))
            except:
                # If the value cannot be converten into a either a floar or a interger the input will be 'False'
                arg = None
        # If the value is False it means that the input cannot be converted into a numerical value
        if arg != None and arg != 0:
            return arg
        print('Input an useful value\n')


print('Input quadratic constants')
print('Input a:')
value_a = inp_covertor_b()
print('Input b:')
value_b = inp_covertor_b()
print('Input c:')
value_c = inp_covertor_b()

root_a = (- value_b - ((value_b**2) - 4 * value_a * value_c)
          ** (1/2)) / (value_a * 2)
root_b = (- value_b - ((value_b**2) - 4 * value_a * value_c)
          ** (1/2)) / (value_a * 2)
if type(root_a) is complex or type(root_b) is complex:
    print(f'No solution in the Real set')
print(f'Root 1 {root_a}\nRoot 2 {root_b}')

title_127 = '''-----------------------------------------------------------------
------------------------- 127 th Excercise -----------------------
--------------------------- Values swap --------------------------
------------------------------------------------------------------'''

excercise_127 = '''Write a program that takes two numbers from the user, stroes them inside varuables and then 
swaps the values in two ways
(1) by using a temporary variable
(2) by not using a temporary variable
At the end, display the results to the user'''

print(title_127)
print(excercise_127)

value_a = inp_covertor_a()
value_b = inp_covertor_a()
print(f'Value a {value_a}\nValue b {value_b}')

# 1
value_c = value_a
value_a = value_b
value_b = value_c
print(f'1st swap\nValue a {value_a}\nValue b {value_b}')

# 2
value_a, value_b = value_b, value_a
print(f'2nd swap\nValue a {value_a}\nValue b {value_b}')


title_128 = '''-----------------------------------------------------------------
------------------------- 128 th Excercise -----------------------
------------------- Program to generate random -------------------
----------------------------- numbers ----------------------------
------------------------------------------------------------------'''

excercise_128 = '''Write a program that generates reandom numbers between 1 and 100'''

print(title_128)
print(excercise_128)


# 1st approach
print(f'Random number {int(random.random()*100)}')
# 2nd approach
print(f'Random number {random.randint(1,100)}')

title_129 = '''-----------------------------------------------------------------
------------------------- 129 th Excercise -----------------------
---------------------- Program to transform ----------------------
--------------------------- miles to km --------------------------
------------------------------------------------------------------'''

excercise_129 = '''Write a program takes an input from the user in miles, converts it to 
kilometers and displays it to the user'''

print(title_129)
print(excercise_129)

print('Input miles')
value_a = inp_covertor_a()
print(f'Miles {value_a}')
value_a = value_a / 0.621371
print(f'Kilometers')

title_130 = '''-----------------------------------------------------------------
------------------------- 130 th Excercise -----------------------
---------------------- Program to transform ----------------------
---------------------- farenheit to celcius ----------------------
------------------------------------------------------------------'''

excercise_130 = '''Write a program that takes an input from the user in farenheit, 
converts it to celcius and displays it to the user'''

print(title_130)
print(excercise_130)

print('Input Farenheit degrees')
value_a = inp_covertor_a()
print(f'Farenheit degrees {value_a}')
value_a = (value_a - 32) * 5/9
print(f'Celcius degrees {value_a}')

title_131 = '''-----------------------------------------------------------------
------------------------- 131 th Excercise -----------------------
---------------------- Program to check if -----------------------
---------------------- a value is positive -----------------------
------------------------------------------------------------------'''

excercise_131 = '''Write a program that takes an input from the user and displays wether the input 
number is a positive number or not

Solve task in two ways
1- using if...elif...else
2- using nested conditionals'''

print(title_131)
print(excercise_131)

# 1st approach
value_a = inp_covertor_a()
if value_a > 0:
    print('Positive value')
elif value_a == 0:
    print('Value is zero')
else:
    print('Negative value')

# 2nd approach
value_a = inp_covertor_a()
if value_a != 0:
    if value_a > 0:
        print('Positive value')
    else:
        print('Negative value')
else:
    print('Value is zero')

title_132 = '''-----------------------------------------------------------------
------------------------- 132 th Excercise -----------------------
---------------------- Program to check if -----------------------
----------------------- a number is odd or -----------------------
------------------------------ even ------------------------------
------------------------------------------------------------------'''

excercise_132 = '''Write a program that takes an input from the user as a number and displays it to
the user wether is a even or odd number'''

print(title_132)
print(excercise_132)

value_a = inp_covertor_a()
if value_a % 2 == 0:
    print(f'{value_a} is an even number')
elif value_a == 0:
    print(f'Value is zero')
else:
    print(f'{value_a} is an odd number')

title_133 = '''-----------------------------------------------------------------
------------------------ 133 th Excercise ------------------------
---------------------- Program to check if -----------------------
---------------------- a year is a leap year ---------------------
------------------------------------------------------------------'''

excercise_133 = '''Write a program that takes an input from the user as a number and displays it to
the user wether is a even or odd number'''

print(title_133)
print(excercise_133)


def inp_covertor_c():
    while True:
        arg = input('Please input a number\n')
        try:
            # Try to convert value to integer
            arg = int(arg)
        except:
            # If the value cannot be converten into a either a floar or a interger the input will be 'False'
            arg = None
        # If the value is False it means that the input cannot be converted into a numerical value
        if arg != None:
            return arg
        print('Input an useful value\n')


value_a = inp_covertor_c()
value_a = 1600
if value_a != 0 and value_a % 4 == 0 and (value_a % 100 == value_a and not (float(value_a % 100) - int(value_a % 100) != 0)):
    print(f'The year {value_a} is a leap year')
else:
    print(f'The year {value_a} is NOT a leap year')


if value_a > 0:
    print(f'The year is from the common era')
else:
    print(f'The year is before the common era')

title_134 = '''-----------------------------------------------------------------
------------------------ 134 th Excercise ------------------------
----------------------- Program to return ------------------------
------------------------ the highest value -----------------------
------------------------------------------------------------------'''

excercise_134 = '''Write a program that takes three different numbers as inputs from the
user and displays the user the largest of the number'''

print(title_134)
print(excercise_134)

list_a = []
print('Input three numbers')
print('Input 1st:')
list_a.append(inp_covertor_b())
print('Input 2nd:')
list_a.append(inp_covertor_b())
print('Input 3rd:')
list_a.append(inp_covertor_b())
print(f'Highest value {list_a.sort()[-1]}')

title_135 = '''-----------------------------------------------------------------
------------------------ 135 th Excercise ------------------------
----------------------- Check if value is a ----------------------
-------------------------- prime number --------------------------
------------------------------------------------------------------'''

excercise_135 = '''Write a program that takes an input from the user and displays if the value
is a prime'''

print(title_135)
print(excercise_135)

value_a = inp_covertor_c()
divisible = False
if not value_a in range(0, 2):
    for number in range(2, abs(value_a)):
        if value_a % number == 0:
            divisible = True
            break

if divisible is False:
    print(f'Value {value_a} is prime')
else:
    print(f'Value {value_a} is NOT prime')

title_136 = '''-----------------------------------------------------------------
------------------------ 136 th Excercise ------------------------
--------------------- Check for prime numbers --------------------
--------------------- between zero and number --------------------
------------------------------------------------------------------'''

excercise_136 = '''Write a program that takes an input from the user and displays all the prime number 
from zero to that value'''

print(title_136)
print(excercise_136)

value_a = inp_covertor_c()
for value_a in range(0, value_a + 1):
    print(value_a)
    divisible = False
    if not value_a in range(0, 2):
        for number in range(2, abs(value_a)):
            if value_a % number == 0:
                divisible = True
                break
    if divisible is False:
        print(f'Value {value_a} is prime')

title_137 = '''-----------------------------------------------------------------
------------------------ 137 th Excercise ------------------------
------------------------ Program to return -----------------------
------------------------- factorial value ------------------------
------------------------------------------------------------------'''

excercise_137 = '''Write a program that takes an input from the user and returns 
the factoria of that number'''

print(title_137)
print(excercise_137)


def inp_covertor_d():
    while True:
        arg = input('Please input a number\n')
        try:
            # Try to convert value to integer
            arg = int(arg)
        except:
            # If the value cannot be converten into a either a floar or a interger the input will be 'False'
            arg = None
        # If the value is False it means that the input cannot be converted into a numerical value
        if arg != None and arg > 0:
            return arg
        print('Input an useful value\n')


value_a = inp_covertor_d()
factorial = 1
if value_a != 1 or value_a != 0:
    for number in range(1, value_a + 1):
        factorial = factorial * number

print(f'The factorial of {value_a} is {factorial}')

title_138 = '''-----------------------------------------------------------------
------------------------ 138 th Excercise ------------------------
------------------------ Program to return -----------------------
-------------------- the multiplication table --------------------
------------------------------------------------------------------'''

excercise_138 = '''Write a program that takes an input from the user and the multiplication 
table from 0 to 10'''

print(title_138)
print(excercise_138)

value_a = inp_covertor_d()
for number in range(0, 11):
    print(f'{number} x {value_a} = {number * value_a}')

title_139 = '''-----------------------------------------------------------------
------------------------ 139 th Excercise ------------------------
------------------------ Program to return -----------------------
--------------------- the Fibonacci sequence ---------------------
------------------------------------------------------------------'''

excercise_139 = '''Write a program that takes an input from the user and display the 
Fibonacci sequence to that number'''

print(title_139)
print(excercise_139)

value_a = inp_covertor_d()
x1, x2 = 0, 1
if value_a == 1:
    print(x1)
else:
    for _ in range(0, value_a + 1):
        print(f'{x1}')
        fibonacci = x1 + x2
        x1 = x2
        x2 = fibonacci

title_140 = '''-----------------------------------------------------------------
------------------------ 140 th Excercise ------------------------
------------------------ Program to check ------------------------
---------------------- the Armstrong number ----------------------
------------------------------------------------------------------'''

excercise_140 = '''Write a program that takes an input from the user and display if the value
is an Armstrong number'''

print(title_140)
print(excercise_140)

value_a = inp_covertor_d()
digits = str(value_a)
power = len(digits)
armstrong_value = 0
for number in digits:
    armstrong_value += int(number) ** power

if armstrong_value == value_a:
    print(f'{value_a} in an Armstrong number')

title_141 = '''-----------------------------------------------------------------
------------------------ 141 th Excercise ------------------------
------------------------ Program to find -------------------------
---------------------- the Armstrong number ----------------------
------------------------------------------------------------------'''

excercise_141 = '''Write a program that takes an input from the user and display the
Armstrong number from zero to that number'''

print(title_141)
print(excercise_141)

value_a = inp_covertor_d()
for value_a in range(0, value_a + 1):
    digits = str(value_a)
    power = len(digits)
    armstrong_value = 0
    for number in digits:
        armstrong_value += int(number) ** power
    if armstrong_value == value_a:
        print(f'{value_a} in an Armstrong number')

title_142 = '''-----------------------------------------------------------------
------------------------ 142 th Excercise ------------------------
------------------------- Program to sum -------------------------
------------------------ several integers ------------------------
-------------------- from zero to that number --------------------
------------------------------------------------------------------'''

excercise_142 = '''Write a program that takes an input from the user and display the
Armstrong number from zero to that number'''

print(title_142)
print(excercise_142)

value_a = inp_covertor_d()
sumatory = 0
for number in range(0, value_a):
    sumatory += number

print(f'From zero to {value_a} the sum is {sumatory}')

title_143 = '''-----------------------------------------------------------------
------------------------ 143 th Excercise ------------------------
------------------------- Program to sum -------------------------
------------------------ several integers ------------------------
-------------------- from zero to that number --------------------
------------------------------------------------------------------'''

excercise_143 = '''Write a program that takes an input from the user and display the
succesive powers of two up to that number'''

print(title_143)
print(excercise_143)

value_a = inp_covertor_d()
map_a = map(lambda x: (x, 2**x), range(0, value_a + 1))
print(f'Power of 2 from 0 to {value_a}')
for item in map_a:
    print(f'The {item[0]}th power of 2 = {item[1]}')

title_144 = '''-----------------------------------------------------------------
------------------------ 144 th Excercise ------------------------
-------------------------- Program check -------------------------
------------------------- divsible values ------------------------
------------------------- within a range -------------------------
------------------------------------------------------------------'''

excercise_144 = '''Write a program that takes a divisor and a range for a dividend and then
returns the numbers divisible by the divisor in the dividend range'''

print(title_144)
print(excercise_144)

print('Input divisor')
value_a = inp_covertor_c()
print('Input dividend upper limit')
value_b = inp_covertor_c()
print('Input dividend lower limit')
value_c = inp_covertor_c()

list_a = []

if value_b > value_c:
    value_b, value_c = value_c, value_b
elif value_b != value_c:
    for number in range(value_b, value_c + 1):
        if number % value_a == 0 and number != 0:
            list_a.append(number)
    if len(list_a) > 0:
        print(f'Number of divisible terms {len(list_a)}:')
        for number in list_a:
            print(number)
    else:
        print(
            f'No dividend values between {value_b} - {value_c} for {value_a}')

title_145 = '''-----------------------------------------------------------------
------------------------ 145 th Excercise ------------------------
-------------------------- Program check -------------------------
------------------------- the ASCII value ------------------------
-------------------------- for a string --------------------------
------------------------------------------------------------------'''

excercise_145 = '''Write a program that takes an input from the user as a charcater or a string 
and returns the ASCII value of it'''

print(title_145)
print(excercise_145)

value_a = input('Input string\n')
list_a = []
print(f'The ASCII value for characters in string {value_a} are')
for character in value_a:
    if not character in list_a:
        print(f'Character {character}: {ord(character)}')
        list_a.append(character)

title_146 = '''-----------------------------------------------------------------
------------------------ 146 th Excercise ------------------------
----------------------- Program calculates -----------------------
--------------------------- HCF and CGD --------------------------
---------------------------- of a set ----------------------------
------------------------------------------------------------------'''

excercise_146 = '''Write a program that takes an number as an input from the 
user and then returns the Highest Common Factor also called the Gretest Common Divisor from 
a set'''

print(title_146)
print(excercise_146)


def function_c():
    def inp_covertor_c():
        while True:
            input_value = input('Please input a number\n')
            try:
                # If the ValueError exception was raised or if there's no difference between the transformation of the value
                # between a float or an interger it will try to convert it to a integer
                arg = int(float(input_value))
            except:
                arg = None
            # If the value is False it means that the input cannot be converted into a numerical value
            # If the value is meant to cancel the process of appending it return a false value which will be passed to break the cicle
            if input_value.lower() == 'no' or arg != None:
                return arg
            else:
                # If the value is not a useful value it will print this message and the loop will restart
                print('Input an useful value\n')

    def function_d():
        set_a = set()
        print('Input several values to a list\nWhen done type NO')
        while True:
            value_a = inp_covertor_c()
            if value_a == None:  # If returned a False value the loop will break
                return set_a
            else:
                # In case is recieved a value the loop will continue to ask values to append
                set_a.add(value_a)
    set_a = function_d()  # Here the append function starts
    return set_a


set_a = function_c()
hcf = {}

for number in set_a:
    div_dict = {}
    counter = 1
    while number != 1 and counter < 100:
        print(number, counter)
        if number % counter == 0 and number // counter != number:
            number = number // counter
            if str(counter) in div_dict:
                div_dict[str(counter)] += 1
            else:
                div_dict[str(counter)] = 1
            counter = 1
        counter += 1
    print(div_dict)
    if len(hcf) == 0:
        hcf = div_dict.copy()
    else:
        set_b = set(div_dict.keys()).intersection(hcf.keys())
        for item in set_b:
            if div_dict[item] <= hcf[item]:
                hcf[item] = div_dict[item]

title_147 = '''-----------------------------------------------------------------
------------------------ 147 th Excercise ------------------------
----------------------- Program calculates -----------------------
------------------------------- LCM ------------------------------
---------------------------- of a set ----------------------------
------------------------------------------------------------------'''

excercise_147 = '''Write a program that takes an number as an input from the 
user and then returns the Least Common Multiple from a set'''

print(title_147)
print(excercise_147)

set_a = function_c()
lcm = {}

for number in set_a:
    div_dict = {}
    counter = 1
    while number != 1 and counter < 100:
        if number % counter == 0 and number // counter != number:
            number = number // counter
            if str(counter) in div_dict:
                div_dict[str(counter)] += 1
            else:
                div_dict[str(counter)] = 1
            counter = 1
        counter += 1
    print(div_dict)
    print(lcm)
    if len(lcm) == 0:
        lcm = div_dict.copy()
    else:
        set_b = set(lcm.keys()).union(set(div_dict.keys()))
        for item in set_b:
            if lcm.get(item) is None or (div_dict.get(item) is not None and div_dict.get(item) >= lcm.get(item)):
                lcm[item] = div_dict[item]

title_148 = '''-----------------------------------------------------------------
------------------------ 148 th Excercise ------------------------
----------------------- Program calculates -----------------------
--------------------- the factors of a number --------------------
------------------------------------------------------------------'''

excercise_148 = '''Write a program that takes a number as an input from the 
user and then returns the Least Common Multiple from a set'''

print(title_148)
print(excercise_148)

value_a = inp_covertor_c()
div_dict = {}
counter = 1
while value_a != 1 and counter < 100:
    if value_a % counter == 0 and value_a // counter != value_a:
        value_a = value_a // counter
        if str(counter) in div_dict:
            div_dict[str(counter)] += 1
        else:
            div_dict[str(counter)] = 1
        counter = 1
    counter += 1

print(div_dict)

title_149 = '''-----------------------------------------------------------------
------------------------ 149 th Excercise ------------------------
---------------------------- Program a ---------------------------
----------------------- simple calculator ------------------------
------------------------------------------------------------------'''

excercise_149 = '''Write a program that takes an operation as an input such as addition,
substraction, multiplication or division, then asks for two numbers and returns the result
of the operation'''

print(title_149)
print(excercise_149)

string_a = input(
    'Input the operation\n[0] - Addition\n[1] - Substraction\n[2] - Multiplication\n[3] - Division\n[4] - Floor\n[5] - Modulo')
print('Input 1st factor')
value_a = inp_covertor_a()
print('Input 2nd factor')
value_b = inp_covertor_a()
if string_a in '0 - Addition':
    result = value_a + value_b
elif string_a in '1 - Substraction':
    result = value_a - value_b
elif string_a in '2 - Multiplication':
    result = value_a * value_b
elif string_a in '3 - Division':
    result = value_a / value_b
elif string_a in '4 - Floor':
    result = value_a // value_b
elif string_a in '5 - Modulo':
    result = value_a % value_b

print(f'The {string_a} operation between {value_a} and {value_b} is : {result}')

title_150 = '''-----------------------------------------------------------------
------------------------ 150 th Excercise ------------------------
---------------------------- Program a ---------------------------
----------------------- simple calculator ------------------------
------------------------------------------------------------------'''

excercise_150 = '''Write a program that shuffles a deck of cards'''

print(title_150)
print(excercise_150)


num_of_cards = [str(card) + ' ' if card != 1 else 'A' for card in range(1, 14)]
suit_of_cards = ['Clubs', 'Diamond', 'Hearts', 'Spade']
deck_of_cards = [
    card + suit for card in num_of_cards for suit in suit_of_cards]
deck_of_cards.append('Joker')
deck_of_cards.append('Joker')
random.shuffle(deck_of_cards)
for card in deck_of_cards:
    print(f'Card : {card}')

title_151 = '''-----------------------------------------------------------------
------------------------ 151 th Excercise ------------------------
---------------------- Program that displays ---------------------
--------------------------- a calendar ---------------------------
------------------------------------------------------------------'''

excercise_151 = '''Write a program that displays a calendar'''

print(title_151)
print(excercise_151)


def week_day_from_sunday(number):  # Canon
    number += 1
    if number == 7:
        number = 0
    return number


date_a = input('Input first date in dd/mm/yyyy format\n')
date_a = datetime.datetime.strptime(date_a, '%d/%m/%Y')
date_b = input('Input last date in dd/mm/yyyy format\n')
date_b = datetime.datetime.strptime(date_b, '%d/%m/%Y')

mont_a = datetime.datetime(month=date_a.month, year=date_a.year, day=1)
mont_b = datetime.datetime(month=date_b.month, year=date_b.year, day=1)

curr_date = mont_a

days_of_week = [' Sun ', ' Mon ', ' Tue ', ' Wed ', ' Thu ', ' Fri ', ' Sat ']
empty_string = ' ' * len(days_of_week[0])
new_month = True

while curr_date.month <= date_b.month:
    if new_month:
        print('\n' * 2)
        week_days = ''.join(days_of_week) + '\n'
        month_year = curr_date.strftime('%B') + '  ' + curr_date.strftime('%Y')
        center = (len(week_days) - len(month_year)) // 2
        line = center * ' ' + month_year + center * ' ' + '\n' * 2
        line += week_days + '\n'
        line += week_day_from_sunday(curr_date.weekday()) * empty_string
        new_month = False
    if len(str(curr_date.day)) == 1:
        if curr_date == date_a or curr_date == date_b:
            line += f' -{curr_date.day}- '
        else:
            line += f'  {curr_date.day}  '
    else:
        if curr_date == date_a or curr_date == date_b:
            line += f'-{curr_date.day}- '
        else:
            line += f' {curr_date.day}  '
    if week_day_from_sunday(curr_date.weekday()) == 6:
        line += '\n'
        print(line)
        line = ''
    next_day = curr_date + datetime.timedelta(days=1)
    if next_day.month != curr_date.month:
        new_month = True
        print(line)
    curr_date = next_day

print(
    f'Between {date_a.date()} and {date_b.date()} there are {(date_b - date_a).days} days')

title_152 = '''-----------------------------------------------------------------
------------------------ 152 th Excercise ------------------------
----------------------- Program to display -----------------------
----------------------- Fibonacci sequence -----------------------
------------------------ through recursion -----------------------
------------------------------------------------------------------'''

excercise_152 = '''Write a program that displays the Fibonacci sequence 
using recursion'''

print(title_152)
print(excercise_152)


def Fib_rec(n):
    if n <= 1:
        return n
    else:
        result = Fib_rec(n - 1) + Fib_rec(n - 2)
        return result


value_a = inp_covertor_c()

for term in range(0, value_a):
    print(Fib_rec(term))

title_153 = '''-----------------------------------------------------------------
------------------------ 153 th Excercise ------------------------
----------------------- Program to display -----------------------
--------------------- sum of natural numbers ---------------------
------------------------ through recursion -----------------------
------------------------------------------------------------------'''

excercise_153 = '''Write a program that displays the sum of natural numbers 
using recursion'''

print(title_153)
print(excercise_153)


def nat_sum_rec(n):
    if n <= 1:
        return n
    else:
        return n + nat_sum_rec(n - 1)


value_a = inp_covertor_c()

print(nat_sum_rec(value_a))

title_154 = '''-----------------------------------------------------------------
------------------------ 154 th Excercise ------------------------
----------------------- Program to display -----------------------
--------------------------- factorial ---------------------------
------------------------ through recursion -----------------------
------------------------------------------------------------------'''

excercise_154 = '''Write a program that displays the factorial of a number 
using recursion'''

print(title_154)
print(excercise_154)


def fact_rec(n):
    if n <= 1:
        return 1
    else:
        return n * fact_rec(n - 1)


value_a = inp_covertor_c()

print(fact_rec(value_a))

title_155 = '''-----------------------------------------------------------------
------------------------ 155 th Excercise ------------------------
---------------------- Program to transpose ----------------------
---------------------------- a matrix ----------------------------
------------------------------------------------------------------'''

excercise_155 = '''Write a program to transpose a matrix in two ways
1 # Nested loop
2 # Using nested list comprenhension'''

print(title_155)
print(excercise_155)

matrix_a = [
    [1, 7],
    [4, 5],
    [7, 8]]

print('1st way: Nested loop')

print('1st Matrix')
matrix_b = []
row = []
for x in matrix_a:
    row.append(x[0])
matrix_b.append(row)
row = []
for y in matrix_a:
    row.append(y[1])
matrix_b.append(row)
print(f'matrix_b = {matrix_b}')

# Another approach

result = [[0, 0, 0],
          [0, 0, 0]]

for row in range(len(x)):
    # iterate over cols
    for col in range(len(x[0])):
        result[col][row] = x[row][col]

print(f'result = {result}')

print('2nd Matrix')
matrix_c = [[x[0] for x in matrix_a], [y[1] for y in matrix_a]]
print(f'matrix_c = {matrix_c}')

title_156 = '''-----------------------------------------------------------------
------------------------ 156 th Excercise ------------------------
----------------------- Program to sum two -----------------------
---------------------------- matrices ----------------------------
------------------------------------------------------------------'''

excercise_156 = '''Write a program to sum two marices in two ways
1 # Nested loop
2 # Using nested list comprenhension'''

print(title_156)
print(excercise_156)


matrix_a = [[1, 7, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix_b = [[1, 9, 1],
            [6, 7, 3],
            [4, 5, 9]]

print('1st approach')
matrix_c = copy.deepcopy(matrix_b)
for n in range(len(matrix_c)):
    for m in range(len(matrix_c[0])):
        matrix_c[n][m] = matrix_a[n][m] + matrix_b[n][m]

print(f'matrix_c {matrix_c}')

print('2nd approach')
matrix_d = [[matrix_a[n][m] + matrix_b[n][m]
             for m in range(len(matrix_a))] for n in range(len(matrix_a[0]))]
print(f'matrix_d {matrix_d}')

title_157 = '''-----------------------------------------------------------------
------------------------ 157 th Excercise ------------------------
----------------------- Program to sum two -----------------------
---------------------------- matrices ----------------------------
------------------------------------------------------------------'''

excercise_157 = '''Write a program to multiply two marices in two ways
1 # Nested loop
2 # Using nested list comprenhension'''

print(title_157)
print(excercise_157)

matrix_a = [[9, 5, 2],
            [4, 8, 6],
            [7, 3, 1]]

matrix_b = [[1, 9, 1, 11],
            [2, 6, 5, 7],
            [3, 4, 1, 5]]

matrix_dim = (len(matrix_a), len(matrix_b[0]), len(matrix_b))
matrix_c = [[0 for a in range(matrix_dim[0])] for b in range(matrix_dim[1])]
print(f'{len(matrix_c[0]),len(matrix_c[1])}\n{matrix_dim}')

print('1st approach')

for m in range(matrix_dim[0]):
    for n in range(matrix_dim[1]):
        for o in range(matrix_dim[2]):
            matrix_c[m][n] += matrix_a[m][o] * matrix_b[o][n]

print(f'{matrix_c}')

print('2nd approach')

matrix_d = [[sum(a * b for a, b in zip(x_row, y_col))
             for y_col in zip(*matrix_b)] for x_row in matrix_a]

print(matrix_d)

title_158 = '''-----------------------------------------------------------------
------------------------ 158 th Excercise ------------------------
----------------------- Program check for ------------------------
-------------------------- a palindrome --------------------------
------------------------------------------------------------------'''

excercise_158 = '''Write a program to check for palindrome'''

print(title_158)
print(excercise_158)

value_a = input('Input a string\n')
if value_a == value_a[::-1]:
    print(f'String {value_a} is a palindrome')
else:
    print(f'String {value_a} is NOT a palindrome')

title_159 = '''-----------------------------------------------------------------
------------------------ 159 th Excercise ------------------------
---------------------- Program to sort words ---------------------
------------------------- alphabetically -------------------------
------------------------------------------------------------------'''

excercise_159 = '''Write a program to sort words alphabetically'''

print(title_159)
print(excercise_159)

value_a = input('Input a string\n')
words = [word.lower() for word in value_a.split()]
words.sort()
words = ' '.join(words)
print(words)

title_160 = '''-----------------------------------------------------------------
------------------------ 160 th Excercise ------------------------
---------------------- Program to sort words ---------------------
------------------------- alphabetically -------------------------
------------------------------------------------------------------'''

excercise_160 = '''Write a program to make these set operations
1 - Union
2 - Intersection
3 - Difference
4 - Symmetric difference'''

print(title_160)
print(excercise_160)

set_a = {0, 1, 2, 3, 4, 6, 5, 7}
set_b = {2, 3, 4, 5, 6, 7, 8, 9}

set_c = set_a.union(set_b)
print(f'{set_c}')

set_d = set_a.intersection(set_b)
print(f'{set_d}')

set_e = set_a.difference(set_b)
print(f'{set_e}')

set_f = set_b.difference(set_a)
print(f'{set_f}')

set_g = set_a.symmetric_difference(set_b)
print(f'{set_g}')

title_160 = '''-----------------------------------------------------------------
------------------------ 160 th Excercise ------------------------
------------------------- Program remove -------------------------
-------------------------- punctuations --------------------------
------------------------------------------------------------------'''

excercise_160 = '''Write a program to remove punctuations from string'''

print(title_160)
print(excercise_160)


string = """
Hi!!!
welcome I guess, ?
2 > 1
[0-9]
{2,4}
\t
\n
my_email@my-email.com
"""

result_a = re.findall('[a-zA-Z]+', string, flags=re.IGNORECASE)
result_a = ' '.join(result_a)

print(f'{result_a}')

title_161 = '''-----------------------------------------------------------------
------------------------ 161 th Excercise ------------------------
------------------------ Program to count ------------------------
----------------------------- vowels -----------------------------
------------------------------------------------------------------'''

excercise_161 = '''Write a program to count vowels'''

print(title_161)
print(excercise_161)

string = """
Hi!!!
welcome I guess, ?
2 > 1
[0-9]
{2,4}
\t
\n
my_email@my-email.com
"""

result_a = re.findall('[aeiou]+', string, flags=re.IGNORECASE)
result_a = len(result_a)

print(f'{result_a}')
