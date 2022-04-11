title_20 = '''-----------------------------------------------------------------
-------------------------- 20 th Excercise ----------------------
-------------------------- Print 10 natural ---------------------
------------------------ numbers using while --------------------
-------------------------------- loop ---------------------------
-----------------------------------------------------------------'''

excercise_20 = '''Print the first 10 natural numbers using a while loop'''

print(title_20)
print(excercise_20)

count = 0
while count <= 10:
    print (f'Natural number {count}')
    count += 1

title_21 = '''-----------------------------------------------------------------
-------------------------- 21 th Excercise ----------------------
-------------------------- Print a triangle ---------------------
----------------------- pattern using a while -------------------
-------------------------------- loop ---------------------------
-----------------------------------------------------------------'''

excercise_21 = '''Print a pyramid uf consecutive numbers'''

print(title_21)
print(excercise_21)

def inp_covertor_a():
    while True:
        arg = input('Please input a number\n')
        try:
            arg = int(arg)
        except:
            # If the value cannot be converten into a either a floar or a interger the input will be 'False'
            arg = None
        # If the value is False it means that the input cannot be converted into a numerical value
        if arg != None and arg >= 1:
            return arg
        print ('Input an useful value\n')

number_a = inp_covertor_a()
count_a = 1
while number_a >= count_a:
    count_b = 1
    string = ''
    while count_a >= count_b:
        string = string + str (count_b) + ' '
        count_b += 1
    print (string)
    count_a += 1

title_22 = '''-----------------------------------------------------------------
-------------------------- 22 th Excercise ----------------------
--------------------------- Input integer -----------------------
---------------------- Sum all previous numbers -----------------
-------------------------- from 0 to number ---------------------
-----------------------------------------------------------------'''

excercise_22 = '''Accept a natural number from user then calculate the sum of every previuos one until 0'''

print(title_22)
print(excercise_22)

def inp_covertor_b():
    while True:
        arg = input('Please input a number\n')
        try:
            arg = int(arg)
        except:
            # If the value cannot be converten into a either a floar or a interger the input will be 'False'
            arg = None
        # If the value is False it means that the input cannot be converted into a numerical value
        if arg != None and arg >= 0:
            return arg
        print ('Input an useful value\n')

number_a = inp_covertor_b()
value = 0
while number_a > 0:
    value += number_a
    number_a -= 1

print (f'Sum of values {value}')

title_23 = '''-----------------------------------------------------------------
-------------------------- 23 th Excercise ----------------------
--------------------- Print the multiplication ------------------
------------------- table for n terms of a value ----------------
-----------------------------------------------------------------'''

excercise_23 = '''Accept a natural number and a number, the print the n terms multiplication table'''

print(title_23)
print(excercise_23)

def inp_covertor_c():
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


print ('Introduce a number')
number_a = inp_covertor_c()
print ('Introduce n terms')
number_b = inp_covertor_b()
print ('Multiplication table')
for product in range(0,number_b + 1):
    print (f'{number_a} x {product} = {product*number_a}')

title_24 = '''-----------------------------------------------------------------
-------------------------- 24 th Excercise ----------------------
----------------------- Given a list display --------------------
------------------- divisible terms by 5 until a ----------------
--------------------- value is greater than 100 -----------------
-----------------------------------------------------------------'''

excercise_24 = '''Given a list, iterate and show any value divisible by 5 and stop when reaching a number greater than 100'''

print(title_24)
print(excercise_24)

list_a = [12,15,32,42,55,75,122,132,150,180,200]

for number in list_a:
    if number <= 100:
        if number % 5 == 0:
            print (f'Value divisible by 5 = {number}')
    else:
        break

title_25 = '''-----------------------------------------------------------------
-------------------------- 25 th Excercise ----------------------
----------------------- Count digits in number ------------------
-----------------------------------------------------------------'''

excercise_25 = '''Count the total digits in a given number'''

print(title_25)
print(excercise_25)

number_a = inp_covertor_c()
number_a = str(number_a)
digits = len (number_a)
if number_a.find('.') != -1 :
    digits -= 1

print (f'Digits {digits}')

title_26 = '''-----------------------------------------------------------------
-------------------------- 26 th Excercise ----------------------
-------------------------- Print a pattern ----------------------
-----------------------------------------------------------------'''

excercise_26 = '''Print a pattern'''

print(title_26)
print(excercise_26)

number_a = inp_covertor_a()

count_a = number_a
while count_a >= 1:
    count_b = count_a
    string = ''
    while count_b >= 1:
        string = string + str(count_b) + ' '
        count_b -=1
    print (string)
    count_a -= 1

title_26 = '''-----------------------------------------------------------------
-------------------------- 26 th Excercise ----------------------
----------------------- Reverse a list using a ------------------
----------------------------- for loop --------------------------
-----------------------------------------------------------------'''

excercise_26 = '''Reverse the following list using a for loop'''

print(title_26)
print(excercise_26)

list_a = [10,20,30,40,50]
list_b = list_a[:]
for index, item in enumerate (list_a):
    list_b [- (index + 1)] = item

print (list_b)

title_27 = '''-----------------------------------------------------------------
-------------------------- 27 th Excercise ----------------------
---------------------- Display integer numbers ------------------
-------------------------------- from ---------------------------
----------------------------- -10 to -1 --------------------------
-----------------------------------------------------------------'''

excercise_27 = '''Display integer numbers from -10 to -1'''

print(title_27)
print(excercise_27)

for item in range(-10,0,1):
    print (f'Item = {item}')

title_28 = '''-----------------------------------------------------------------
-------------------------- 28 th Excercise ----------------------
---------------------- Display a 'Done' message -----------------
----------------------- when ending a for loop ------------------
-----------------------------------------------------------------'''

excercise_28 = '''Display a done message when ending a for loop'''

print(title_28)
print(excercise_28)

for item in range(-10,0,1):
    print (f'Item = {item}')
else:
    print ('Done')

title_29 = '''-----------------------------------------------------------------
-------------------------- 29 th Excercise ----------------------
--------------------- Display all prime numbers -----------------
--------------------------- within a range ----------------------
-----------------------------------------------------------------'''

excercise_29 = '''Display a done message when ending a for loop'''

print(title_29)
print(excercise_29)

number_a = inp_covertor_b()

for number in range (0,number_a + 1):
    count = 0
    for value in range(1,number):
        if number % value == 0:
            count += 1
    if count <= 1:
        print (f'Prime number {number}')

title_30 = '''-----------------------------------------------------------------
-------------------------- 30 th Excercise ----------------------
------------------------ Reverse an integer ---------------------
-----------------------------------------------------------------'''

excercise_30 = '''Reverse an integer'''

print(title_30)
print(excercise_30)

def inp_covertor_d():
    while True:
        arg = input('Please input a number\n')
        try:
            arg = int(arg)
        except:
            # If the value cannot be converten into a either a floar or a interger the input will be 'False'
            arg = None
        # If the value is False it means that the input cannot be converted into a numerical value
        if arg != None and arg:
            return arg
        print ('Input an useful value\n')

number_a = inp_covertor_d()
number_a = str(number_a)
number_b = ''
for character in number_a:
    number_b = character + number_b

number_b = int(number_b)
print (number_b)

title_31 = '''-----------------------------------------------------------------
-------------------------- 31 th Excercise ----------------------
--------------------- Display element on a even -----------------
--------------------- index positions of a list -----------------
-----------------------------------------------------------------'''

excercise_31 = '''Display element on a even index positions of a list'''

print(title_31)
print(excercise_31)

def list_creator():
    n_items = inp_covertor_b()
    count = 0
    list_a = []
    while count <= n_items:
        print (f'Items {count}/{n_items}')
        item = input ('Add an item\n')
        list_a.append (item)
        count += 1
    return list_a

list_a = list_creator()
for index,item in enumerate(list_a):
    if index % 2 == 0:
        print (f'item = {item}')

title_32 = '''-----------------------------------------------------------------
-------------------------- 32 th Excercise ----------------------
------------------- Display the cube of a number ----------------
----------------------- Up to a given integer -------------------
-----------------------------------------------------------------'''

excercise_32 = '''Display the cube of a number up to a given integer'''

print(title_32)
print(excercise_32)

print ('Introduce the beginning of range')
number_a = inp_covertor_b()
print ('Introduce the end of range')
number_b = inp_covertor_b()
if number_a > number_b:
    number_a,number_b = (number_b, number_a)
terms = number_b - number_a
for index, number in enumerate(range(number_a,number_b)):
    value = number ** 3
    print (f'Terms {index}/{terms}\nCube value of {number} = {value}')

title_33 = '''-----------------------------------------------------------------
-------------------------- 33 th Excercise ----------------------
-------------------------- Print a pattern ----------------------
-----------------------------------------------------------------'''

excercise_33 = '''Print a pattern'''

print(title_33)
print(excercise_33)

number_a = inp_covertor_a()
count = 1
while count <= number_a:
    print ('* ' * count)
    count += 1
count = number_a
while count > 0:
    print ('* ' * count)
    count -= 1
