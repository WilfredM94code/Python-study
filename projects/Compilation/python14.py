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
        print ('Input an useful value\n')

value_a = inp_covertor_a()
value_b = inp_covertor_a()
print (f'Sumed values = {value_a + value_b}')

title_124 = '''-----------------------------------------------------------------
------------------------- 124 th Excercise -----------------------
----------------------- Program to input and ---------------------
--------------------- displays a square root ---------------------
------------------------------------------------------------------'''

excercise_124 = '''Write a program that takes two numbers from the user, adds them together and shows the result to the user'''

print(title_124)
print(excercise_124)

value_a = inp_covertor_a()
print (f'Squared root of {value_a} is {value_a**(1/2)}')

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
triangle_area = (semi_perimeter * (semi_perimeter - value_a) * (semi_perimeter - value_b) * semi_perimeter - value_c) ** (1/2)

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
        print ('Input an useful value\n')

print ('Input quadratic constants')
print ('Input a:')
value_a = inp_covertor_b()
print ('Input b:')
value_b = inp_covertor_b()
print ('Input c:')
value_c = inp_covertor_b()

root_a = (- value_b - ((value_b**2)- 4 * value_a * value_c)**(1/2)) / (value_a * 2)
root_b = (- value_b - ((value_b**2)- 4 * value_a * value_c)**(1/2)) / (value_a * 2)
if type(root_a) is complex or type(root_b) is complex:
    print (f'No solution in the Real set')
print (f'Root 1 {root_a}\nRoot 2 {root_b}')

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
print (f'Value a {value_a}\nValue b {value_b}')

# 1
value_c = value_a
value_a = value_b
value_b = value_c
print (f'1st swap\nValue a {value_a}\nValue b {value_b}')

# 2
value_a, value_b =  value_b, value_a 
print (f'2nd swap\nValue a {value_a}\nValue b {value_b}')


title_128 = '''-----------------------------------------------------------------
------------------------- 128 th Excercise -----------------------
------------------- Program to generate random -------------------
----------------------------- numbers ----------------------------
------------------------------------------------------------------'''

excercise_128 = '''Write a program that generates reandom numbers between 1 and 100'''

print(title_128)
print(excercise_128)

import random

# 1st approach
print (f'Random number {int(random.random()*100)}')
# 2nd approach
print (f'Random number {random.randint(1,100)}')

title_129 = '''-----------------------------------------------------------------
------------------------- 129 th Excercise -----------------------
---------------------- Program to transform ----------------------
--------------------------- miles to km --------------------------
------------------------------------------------------------------'''

excercise_129 = '''Write a program takes an input from the user in miles, converts it to 
kilometers and displays it to the user'''

print(title_129)
print(excercise_129)

print ('Input miles')
value_a = inp_covertor_a() 
print (f'Miles {value_a}')
value_a = value_a / 0.621371
print (f'Kilometers')

title_130 = '''-----------------------------------------------------------------
------------------------- 130 th Excercise -----------------------
---------------------- Program to transform ----------------------
---------------------- farenheit to celcius ----------------------
------------------------------------------------------------------'''

excercise_130 = '''Write a program that takes an input from the user in farenheit, 
converts it to celcius and displays it to the user'''

print(title_130)
print(excercise_130)

print ('Input Farenheit degrees')
value_a = inp_covertor_a() 
print (f'Farenheit degrees {value_a}')
value_a = (value_a - 32) * 5/9
print (f'Celcius degrees {value_a}')

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
    print ('Positive value')
elif value_a == 0:
    print ('Value is zero')
else:
    print ('Negative value')

# 2nd approach
value_a = inp_covertor_a() 
if value_a != 0:
    if value_a > 0:
        print ('Positive value')
    else:
        print ('Negative value')
else:
    print ('Value is zero')

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
    print (f'{value_a} is an even number')
elif value_a == 0:
    print (f'Value is zero')
else:
    print (f'{value_a} is an odd number')

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
        print ('Input an useful value\n')

value_a = inp_covertor_c()
value_a = 1600
if value_a != 0 and value_a % 4 == 0 and (value_a % 100 == value_a and not (float(value_a % 100) - int(value_a % 100) != 0)):
    print (f'The year {value_a} is a leap year')
else:
    print (f'The year {value_a} is NOT a leap year')


if value_a > 0:
    print (f'The year is from the common era')
else:
    print (f'The year is before the common era')

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
print ('Input three numbers')
print ('Input 1st:')
list_a.append(inp_covertor_b())
print ('Input 2nd:')
list_a.append(inp_covertor_b())
print ('Input 3rd:')
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
if not value_a in range(0,2):
    for number in range(2,abs(value_a)):
        if value_a % number == 0:
            divisible = True
            break

if divisible is False:
    print (f'Value {value_a} is prime')
else:
    print (f'Value {value_a} is NOT prime')

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
for value_a in range (0,value_a + 1):
    print (value_a)
    divisible = False
    if not value_a in range(0,2):
        for number in range(2,abs(value_a)):
            if value_a % number == 0:
                divisible = True
                break
    if divisible is False:
        print (f'Value {value_a} is prime')

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
        print ('Input an useful value\n')

value_a = inp_covertor_d()
factorial = 1
if value_a != 1 or value_a != 0:
    for number in range (1,value_a + 1):
        factorial = factorial * number

print (f'The factorial of {value_a} is {factorial}')

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
for number in range (0,11):
    print (f'{number} x {value_a} = {number * value_a}')

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
x1, x2 = 0 , 1
if value_a == 1:
    print (x1)
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
    print (f'{value_a} in an Armstrong number')

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
for value_a in range (0,value_a + 1):
    digits = str(value_a)
    power = len(digits)
    armstrong_value = 0
    for number in digits:
        armstrong_value += int(number) ** power
    if armstrong_value == value_a:
        print (f'{value_a} in an Armstrong number')

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
for number in range(0,value_a):
    sumatory += number

print (f'From zero to {value_a} the sum is {sumatory}')

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
map_a = map(lambda x: (x,2**x),range(0,value_a + 1))
print (f'Power of 2 from 0 to {value_a}')
for item in map_a:
    print (f'The {item[0]}th power of 2 = {item[1]}')

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

print ('Input divisor')
value_a = inp_covertor_c()
print ('Input dividend upper limit')
value_b = inp_covertor_c()
print ('Input dividend lower limit')
value_c = inp_covertor_c()

list_a = []

if value_b > value_c:
    value_b, value_c = value_c, value_b
elif value_b != value_c:
    for number in range(value_b, value_c + 1):
        if number % value_a == 0 and number != 0:
            list_a.append(number)
    if len(list_a) > 0:
        print (f'Number of divisible terms {len(list_a)}:')
        for number in list_a:
            print (number)
    else:
        print (f'No dividend values between {value_b} - {value_c} for {value_a}')

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
print (f'The ASCII value for characters in string {value_a} are')
for character in value_a:
    if not character in list_a:
        print (f'Character {character}: {ord(character)}')
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
            if input_value.lower() == 'no' or arg != None: # If the value is meant to cancel the process of appending it return a false value which will be passed to break the cicle
                return arg
            else:
                print ('Input an useful value\n') # If the value is not a useful value it will print this message and the loop will restart
    def function_d():
        set_a = set()
        print ('Input several values to a list\nWhen done type NO')
        while True:
            value_a = inp_covertor_c()
            if value_a == None: # If returned a False value the loop will break
                return set_a
            else:
                set_a.add (value_a) # In case is recieved a value the loop will continue to ask values to append 
    set_a = function_d() # Here the append function starts
    return set_a

set_a = function_c()
hcf = {}

for number in set_a:
    div_dict = {}
    counter = 1
    while number != 1 and counter < 100:
        print (number,counter)
        if number % counter == 0 and number // counter != number:
            number = number // counter
            if str(counter) in div_dict:
                div_dict [str(counter)] += 1
            else:
                div_dict [str(counter)] = 1
            counter = 1
        counter += 1
    print (div_dict)
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
                div_dict [str(counter)] += 1
            else:
                div_dict [str(counter)] = 1
            counter = 1
        counter += 1
    print (div_dict)
    print (lcm)
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
            div_dict [str(counter)] += 1
        else:
            div_dict [str(counter)] = 1
        counter = 1
    counter += 1

print (div_dict)

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

string_a = input('Input the operation\n[0] - Addition\n[1] - Substraction\n[2] - Multiplication\n[3] - Division\n[4] - Floor\n[5] - Modulo')
print ('Input 1st factor')
value_a = inp_covertor_a()
print ('Input 2nd factor')
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

print (f'The {string_a} operation between {value_a} and {value_b} is : {result}')

title_150 = '''-----------------------------------------------------------------
------------------------ 150 th Excercise ------------------------
---------------------------- Program a ---------------------------
----------------------- simple calculator ------------------------
------------------------------------------------------------------'''

excercise_150 = '''Write a program that shuffles a deck of cards'''

print(title_150)
print(excercise_150)

import random

num_of_cards = [str(card) + ' ' if card != 1 else 'A' for card in range(1,14)]
suit_of_cards = ['Clubs','Diamond','Hearts','Spade']
deck_of_cards = [card + suit for card in num_of_cards for suit in suit_of_cards]
deck_of_cards.append ('Joker')
deck_of_cards.append ('Joker')
random.shuffle(deck_of_cards)
for card in deck_of_cards:
    print (f'Card : {card}')

title_151 = '''-----------------------------------------------------------------
------------------------ 151 th Excercise ------------------------
---------------------- Program that displays ---------------------
--------------------------- a calendar ---------------------------
------------------------------------------------------------------'''

excercise_151 = '''Write a program that displays a calendar'''

print(title_151)
print(excercise_151)

import datetime

date_a = input ('Input first date in dd/mm/yyyy format')
date_a = datetime.datetime.strptime(date_a,'%d/%m/%Y')
date_b = input ('Input last date in dd/mm/yyyy format')
date_b = datetime.datetime.strptime(date_b,'%d/%m/%Y')

days_of_week = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']