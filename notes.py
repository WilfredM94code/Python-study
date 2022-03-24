# -----------------------------------------------------------------
# --------------------------- Variables ---------------------------
# -----------------------------------------------------------------



### Variables

# String
'Cactus'
fun_plant = 'Cactus'

# Integer
4
fun_number = 4

# Float
1.1
fun_float = 1.1

# Boolean
True
fun_boolean = True

False
funnier_boolean = False

# Pro tip, use nmotic variable names
# Spacing is not allowed in variable name, instead is used undescore
# Lower case is used by default
# Variables should start with a letter or a underscore
# Under pep8 there should be a space between a variable name and it's value

### Data types

# Every data type can be revealed by using 'type(VARIABLENAME)'

# String
fun_plant = 'Cactus'
type(fun_plant)

# Integer
fun_number = 4
type(fun_number)

# Float
fun_float = 1.1
type(fun_float)

# Boolean
fun_boolean = True
type(fun_boolean)

funnier_boolean = False
type(funnier_boolean)

# New data types

# List
list = [1, 'dog', [2]]
type(list)

# Dictionary
dic = {
    'one':1,
    'two':2,
    'three':3
    }
type (dic)

# Tuple
tup = (1, 2, 3, 'cat')
type (tup)

# Set
set = {1, 2, 1.3}
type(set)

### String methods
a = 'Number '
b = 'eight is a number'

# len()
print ('len a = ', len (a))
print ('len b = ', len (b))

# [] 
# We can select characters:
# Placing integer number from -len(str) to len(str)
# Placing 2 integers separated by ':'
# Ignoring either of the integers separated by ':' like a [:] or a [1:] or a [:-2]
print (a [0])
print (a [1])
print (a [2])
print (a [3])
print (a [4])
print (a [5])
print (a [6])

print (b [-len(b)])
print (b [1-len(b)])
print (b [2-len(b)])
print (b [3-len(b)])
print (b [4-len(b)])
print (b [5-len(b)])
print (b [6-len(b)])
print (b [7-len(b)])

print (b [8 - len(b) : 10 - len(b)], b [11 : len (b)])

# +
# Is used to join/concat several integers
print (a + b)

# f "{}"
# Is a metrod that will help to place several strings within a string
print (f"{a},{b}")

# *
# Is used with a string and a integer. It repeats a string as many times as the integer indicates
print (a * 3)

# .upper() and .lower()
# Changes string content to uppercase or lowercase
print (a.upper())
print (b.lower())

# .title()
# Places a starting capital letter for every word from the string
print (b.title())

# .strip()
# Removes every space at the end or begginig of a string
print (a.strip() + b.strip())

# .find()
# Returns the index of a string 
print (a.find('u'))
print (b.find('u'))

# .replace()
# It takes a tuple on which: first string stands for the one we want to change and the second is the one replacing it
print(b.replace('eight','nine'))

# in operator
# Indicates if a string has a string in it
print (a in b)

# not in operator
# Indicates if a string has not a string in it
print (a not in b)

### None special variable type
# None stands for the absence of a value
# Is used as a default value for variables
print (None)
print (type(None))

### Scape sequences
# Are used to compensate the exclusivity some characters have on python syntax such as """ which should be a string composed by a double quotation mark
print ("He said \"it's the cactus")
print ('He said \'it\'s the cactus')
print ('I want a entry level\\Jr developmer job')
print ('Your cat\njust\njumped')


# -----------------------------------------------------------------
# ---------------------- Arithmetic operatios ---------------------
# -----------------------------------------------------------------

x = 47
y = 6

# Add
print (x+y) 

# Subsrtac
print (x-y) 

# Multiply
print (x*y) 

# Power
print (x**y) 

# Divide
print (x/y)

# Floor division 
# Returns the integer value of a division
print (x//y)

# Modulus 
# Returns the remain of a division
print (x%y) 

# Augmentes assignment
# This operator stores any arithmetic operation in a variable previously deffined
x = 3
y = 4
x += y
print (x) # x stores x + y

x -= y
print (x) # x stores current x - y

# Round
# Returns a rounded integer value from a floating point variable
print (round(3.14))
print (round(0.0666))

# Abs
# Returns a always positive value
print (abs(-5.74))
print (abs(-999))

# Note
# For more complex math operations run 
import math
from msilib.schema import Class


# -----------------------------------------------------------------
# ------------------------- Type conversion -----------------------
# -----------------------------------------------------------------

# Note: Every 'input()' sentence returns a <class'str'>. 'input()' recieves a 
# To check variable type: pass it as an argument to type()
# string value and has to be stored in a variable

# Conversions change the data type of a object into another

inp = input ('Type a number')

# float ()
# Will recieve a numerical string or a integer and return a <class'float'> type
print (float (inp))

# int ()
# Will recieve a numerical string or a float and return a <class'int'> type
print (int (inp))

# str()
# Will recieve a int or a float and return a <class'str'> type

# Note: redundancy won't give errors. A unconvertable value will result in a error

# bool ()
# Will recieve: "" , 0 or None and return a value False <class 'bool'> type
# Every other value will return a value True <class 'bool'> type

print (bool(""))
print (bool("False"))

# -----------------------------------------------------------------
# --------------------------- Name space --------------------------
# -----------------------------------------------------------------

# Note: Every value processed by python has a space on our RAM.
# A variable name can be updated with differnt values, so we can raclicate them along our code. 
# Note how x has been used along this guide

x = 123456

print (id(x))
print (id(123456))
# Same ID for x and 123456

x += 2
print (id(x))
# Different ID for current x

# There's a hierachy in Python for namespace or variable names. 
# Overall we have BUIT-IN NAMESPACE - Namspaces declared and reserved for Python itself like print or float
# Beneath we have Module: GLOBAL NAMESPACE - Namspaces declared on our current Python script
# At the bottom we have Function: LOCAL NAMESPACE - Namspaces declared on a function

# Scope: is the focus on where we can acces to namespaces. 
# If a namespace in a nested function is not declared, Python will get the namespace value from a higher hierarchy

gb = 9
print ('gb declared globally')
def fun():
    loc = 1
    print ('loc declared locally')
    def nes_fun():
        nes_loc = 2
        print ('nes_loc nested declared locally')
        print ('loc reference in nes_fun = ',loc,' ',id(loc))
        print ('gb reference in nes_fun = ',gb,' ',id(gb))
    nes_fun()
    print ('gb reference in fun = ',gb,' ',id(gb))

fun()

# OUTPUT
# gb declared globally
# loc declared locally
# nes_loc nested declared locally
# loc reference in nes_fun =  1   140722078562080
# gb reference in nes_fun =  9   140722078562336
# gb reference in fun =  9   140722078562336

# To manipulate variables from a local scope we have to call it using the prefix global

gb = 9
print ('gb declared globally = ', gb,' ',id(gb))
def new_func():
    global gb
    print ('gb called globally')
    gb = 'Mike'
    print ('gb updated globally = ', gb,' ',id(gb))

new_func()

# OUTPUT
# gb declared globally =  9   140722078562336
# gb called globally
# gb updated globally =  Mike   1833147488688

# To manually pass local scope variable to a function, we have to define it as a varaiable 
# that can be recived by the function at the time 

def a_new_fun (x):
    print ('Here\'s the x = ', x)
    print ('id = ', id(x))

a_new_fun('x')

# OUTPUT
# Here's the x =  x
# id =  1833108653232

# If is declared a function that updates a another namespace, previous namespace value will be lost

#def print (a):
#    a

# print ('a')
# NEVER DO THIS

# To have a disposition of a variable or namespace from a higher hierarchy level on a nested function we call it using the
# non local statement

def fun ():
    x = 'outer x'
    print ('x = ',x, ' ', id(x))
    def nes_fun():
        nonlocal x
        print ('x = ',x, ' ', id(x))
        x = 'nested x'
        print ('x updated in nes_fun')
        print ('x = ',x, ' ', id(x))
    nes_fun()

fun()

# -----------------------------------------------------------------
# ----------------------- Comparison Operators --------------------
# -----------------------------------------------------------------

# Every comparison operation will result on a True or False output

# Greater than
print (9 > 6)
print (5 > 6)
print ('Cactus' == 'Cactus')
print ('Cactus' == 'Cats')

# Equal or greater than
print (9 >= 6)
print (6 >= 6)
print ('Cactus' == 'Cactus')
print ('Cactus' == 'Cats')

# Lesser than
print (9 < 6)
print (5 < 6)
print ('Cactus' == 'Cactus')
print ('Cactus' == 'Cats')

# Equal or lesser than
print (9 <= 6)
print (6 <= 6)
print ('Cactus' == 'Cactus')
print ('Cactus' == 'Cats')

# Equal to
print (9 == 6)
print (6 == 6)
print ('Cactus' == 'Cactus')
print ('Cactus' == 'Cats')

# Inequality
print (9 != 6)
print (6 != 6)
print ('Cactus' == 'Cactus')
print ('Cactus' == 'Cats')

# There's a value related to every character which can be seen using the built in function ord()


# -----------------------------------------------------------------
# ---------------------- Conditional Statements -------------------
# -----------------------------------------------------------------

# Every conditional statement has it's own syntaxis. All of them stars with "if" and ends with colon ":"
# Every conditional statement can compile a set of conditions and will proceed only when the set of 
# conditions ends up in a True statement
# This controls the flow of an application

a = 1
b = 0
c = 2
if a > b:
    print ('Eureka!')


# If a condition is not satisfied we can use the 'else:' complement to offer an alternative to the flow process

if a < b:
    print ('Not eureka!')
else:
    print ('Eureka!')

# In case is required to add another logical gate to another process we can add the 'elif' followed 
# by a set of conditions and end it with a colon ':'

if a < b:
    print ('Not eureka!')
elif b < c:
    print ('Some eureka!')
else:
    print ('Eureka!')

# There can be used parenthesis to gather boolean statements
if a > b or b > c:
    print ('Eureka!')


# Note: for every conditional statement we must consider that the execution is in cascade which gives a hierachical
# order meant to be respected starting from the firsit condition on the first statement, following through until 
# it reaches the end. Every statement should consider this

# Nested conditionals can be use to discriminate between several other conditions if one is satisfied

a = 88
b = 1
c = 8

if a > b:
    if c < a:
        print ('Eureka!')


# -----------------------------------------------------------------
# ------------------------ Logical operators ----------------------
# -----------------------------------------------------------------

# The and argument consider if several conditions are True

if a > b and b < c:
    print ('Eureka!')

# The or argument consider if at leat one condition is True

if a > b or b > c:
    print ('Eureka!')

# The not argument consider if a operation is False, then it returns True

if not a < b:
    print ('Eureka!')

# -----------------------------------------------------------------
# ------------------------ Ternary Operator -----------------------
# -----------------------------------------------------------------

# In case a value is dictated by a set of conditions we can use a ternary operator to asign the value

a = 33
b = 44

value = 'Eureka!' if a > b else 'Not Eureka!'

print ('value = ',value)

# -----------------------------------------------------------------
# --------------------------- For loops ---------------------------
# -----------------------------------------------------------------

# For operators are used to make a recursive process for every position in a set. Every element will have a 
# temporary namespace, and wi will asing a value name to it. In regards of this we will use 'i' but it can be any
# valid variable name

list_1 = [0,1,2,3,4,5,6]
string_1 = 'Eureka'
range_1 = range (5,15,2)

# Note : Range is used to create a <class 'range'> object and is used to make a set of values starting from a number
# to another number and skippinkg many other numbers in the process. we declare a range by using the range sentence
# range (starting_number,ending_number,jump)

for i in list_1:
    print (i)

for i in string_1:
    print (i)

for i in range_1:
    print (i)

# All these statements will return a print of every value on each set

# To end a for statement we nest the 'break' sentence whick breaks the loop

list_1 = [0,1,2,3,4,5,6]

for i in list_1:
    if i == 2:
        print ('Hey, you 2!')
        break


# We can nest loops within loops like

list_1 = [0,1,2,3,4,5,6]

for x in list_1:
    if x == 2:
        print ('Hey, you 2!')
        for n in list_1:
            if n == 3:
                print ('Hey, you 3!')
                break
        break


x_range = range(3)
y_range = range(3)
z_range = range(3)

for x in x_range:
    for y in y_range:
        for z in z_range:
            print ('Actual iteration (x=', x ,', y=', y , ', z=', z ,')')



# -----------------------------------------------------------------
# ------------------------- While loops ---------------------------
# -----------------------------------------------------------------

# While loops are loops that make recursive activities while a boolean variable is True
# These loops are better controled by a condition first declared True that can be switched to
# result False given a condition related to the loop. This control can also be achieved by a 
# break statement

a = 0
while a <= 2:
    print (a)
    a += 1


a = 0
while True:
    print (a)
    a += 1
    if a > 2:
        break

# A no controlled loop will run for ever (we can press on our interpreter ctrl + c and it will stop)

# -----------------------------------------------------------------
# -------------------------- Functions ----------------------------
# -----------------------------------------------------------------

# To declare a function we start with the isntruction 'def' followed by the name we want for the function
# and followed by a tuple containing every variable that we will use within the function then, nested 
# we can place our process

# Note: We can nest functions within functions

def pretty ():
    print ('Pretty fun, uh?')

pretty ()


def not_fun (x):
    if x:
        print ('Not so fun, uh?')

a = True
not_fun (a)

# Note that the variable name employed while defining a function can be different that the variable name
# of the argument passed when calling the function

# Note: The whole point of having functions is to re-use our code. This will help us to build projects and
# with our maintenance activities

# Example

name_list = ['Wil','Zoe','Lou']

def cool_guy (a_name):
    print (a_name, ' is a cool guy!')

for a_name in name_list:
    cool_guy (a_name)

# This function offesr a output which prints, but if we cannot save the string value

# Functions can return values that we can either store it in a veriable or not

name_list = ['Wil','Zoe','Lou']

def cool_guy_fun (a_name):
    cool_statement = a_name + ' is a cool guy!'
    return cool_statement

for a_name in name_list:
    cool_statement = cool_guy_fun (a_name)
    print (cool_statement)

# -----------------------------------------------------------------
# ----------------- Default and optional parameters ---------------
# -----------------------------------------------------------------

# A function can be made to recieve parameters, but these might not be paseed, thats why we can define default values
# for optional parameter. Every required variable has to be declared within the variable tuple of a function
# first than the optional parameters with a equal sign followed by the defautl value we offer

def optional_function (required,optional = 'fun stuff'):
    print ('Required is very important ',required)
    print ('Optional can be ',optional)


optional_function ('right?')
optional_function ('right?', 'also important')


# -----------------------------------------------------------------
# ----------------------- Non keyword arguments -------------------
# -----------------------------------------------------------------

# A undefined number of values can be passed to a function if it has a '*' next to the argument
# name when defined.

def nums (*numbers):
    return numbers

number = nums (0,1,2,3,4,5)

# Another example

def sub_nums (*numbers):
    number = 100
    for n in numbers:
        number -= n
    return number


number = nums (0,1,2,3,4,5)


# -----------------------------------------------------------------
# --------------------- Keyword arguments **kwargs ----------------
# -----------------------------------------------------------------

# At the moment of declaring a function the **kwargs stands for every keywords and value 
# allowed by the function itself

def info_process (**info):
    print ('info = ',info, ' ', type(info))
    return info

info = info_process (name = 'Walter', nick_name = 'Danger', age = 44, speed = 'full speed')

#  This set of values are processed as a dict by Python

# -----------------------------------------------------------------
# ----------------------------- Scope -----------------------------
# -----------------------------------------------------------------

# A variable has a scope, which restricts the acces the variable has and its permanece
# A variable can be blobal which means that it can be accessed from the module and only readed from functions or other objects
# A variable can be local which means that it can be accessed from the object that declared it is erased once the object ends its process
# A variable can be nonlocal which means that it can be accessed from different parts of thethe object that declared it is erased 
# once the object ends its process

name = 'Walter' # global variable

def cool_people (not_a_name):
    number = 44 # Local variable of cool_people
    text = 'Yes'
    thing = '6'
    def not_so_cool (number):
        nonlocal text # Nonlocal variable 'text'
        global name # A global variable is called on a object
        print ('name = ',name)
        name = 'White' # The global variable has been changed
        another_number = 4 # Local variable of not_so_cool
        data = text # A local variable copies the value the nonlocal variable
        text = '66' # A nonlocal variable is modified
        print (data)
        return number,data,name # Number gets a upper level on its hierarchy
    number,data,name = not_so_cool (6)
    return number,data,name

number,data,name = cool_people ('t')
print (number,data,name)

# print (thing) - thing is a local variable called from the module, and since the object has ended its process it cannot be called

# -----------------------------------------------------------------
# ----------------------------- Lists -----------------------------
# -----------------------------------------------------------------

# A list is a set of objects separated by a comma arranged between '[]' or usig the 'list ()' function

example_1 = ['item 0' , 'item 1' , 'item 2' , 'item 3'] 
# basic example of how to declare a list

example_2 = ['item 0' , example_1 , 3 ] 
# another basic example of several different type of elements on a list - lists can be nested

list ('Dinosaur') 
# basic example of how to declare a list using a function, in this case, this list take a string and take every letter as a individual item

# We can merge lists
list_a = [0, 2, 4, 6, 8, 10]
list_b = [1, 3, 5, 7, 9]
list_c = list_a + list_b

# A item in a list can be accessed  with its index number
number_10 = list_a [5]

# A list can be created from another list
copycat = list_a [:]

# A list can be created from a slice of another list
copycat = list_a [ 2 : ]

# Note: index can make different slices and call every other value
sliced_list = list_c [::3]

# A list can be reversed by using '[::-1]'
reversed_list = list_c [::-1]

# There can be taken every other value from a slice
sliced_every_other_list = list_c [1:6:2]

# Python allows to store values from a list in several variables but it must match the number items in the list
list_d = [0, 1, 2, 3, 4, 5, 6]
v0, v1, v2, v3, v4, v5, v6 = list_d

# To store the rest of the values from the list on a variable we use '*' before this new variable name
v1, v2, v3 ,*new_list = list_d

# To store the n first and last m values of the list and storig the rest on another list we place the
# last m variables after the new list
v1, v2, v3 ,*new_list, vx, vxx = list_d

# Lists can pass through a 'for' loop. it can be called the value index while iterating
list_e = list('Funny Plant')
for item in list_e:
    print ('item = ', item, '\n')

# Note: the 'enumerate()' function returns a <class 'enumerate'> object that has 2 iterable items: index and item
for index, item in enumerate(list_e):
    print ('index = ', index, '\nitem = ', item, '\n')

# There are several methods that can be applied to lists
list_f = list ('GoodXXHTimes')

len (list_f)
# It returns the number of items on the list

list_f.append ('!')
# Adds a value to the list at the end of it

list_f.insert (4, ' ')
# Inserts a value at a given index

list_f.pop()
# Deletes the last value of the list

list_f.pop(5)
# Deletes the value of the list at a given index

list_f.remove ('X')
# Removes any given value from a list

del list_f [5]
# Deletes the value of the list at a given index

list_f.reverse()
# Reverses the values of the list

' '.join(list_f)
# Returns every value from the list separated by any given value 

list_f.index('T')
# Returns the index number of for any given value if it is in the list

list_f.count('o')
# Returns the number of time any given value appears on the list

list_g = [644, 789, 357, 40, 1, 0]
list_g.sort()
# Modifies a list ordered in a ascending way

list_g.sort(reverse = True)
# Modifies a list ordered in a descending way

sorted_list_g = sorted(list_g, reverse = False)
# Resturns a new list sorted

list_h = [
    ('Artorias',99),
    ('Pate',15),
    ('Gwyn',100),
    ('Lucatiel',88),
    ('Siff',10),
    ('Aslatiel',50),
]

sorted_list_h = sorted(list_h)
print (sorted_list_h)

# This list has been sorted by the first sub item of every tuple


# For composed items like the tuples in this list, we can sort the items providing 
# the index the sub item that will be the reference to sort with a function

def sort_list (list):
    return list[1]

list_h.sort(key=sort_list)
print (list_h)

# This list has been sorted by it's second sub argument

# -----------------------------------------------------------------
# ----------------------- List Comprenhension ---------------------
# -----------------------------------------------------------------

# List comprenhension allow us to build lists from iterable objects

list_i = [1,55,87,65,12,8]
list_j = ['Cactus','Funny','Dinosaur','Life','Enjoyment','Peace','Love']
list_k = [
    ('Artorias',99),
    ('Pate',15),
    ('Gwyn',100),
    ('Lucatiel',88),
    ('Siff',10),
    ('Aslatiel',50),
]


list_l = [it for it in list_i]
# This syntax allows to build a new list on which every item is the same item as the iterable object on the for loop

list_m = [it*2 for it in list_j]
# This syntax allows to build a new list on which every item is the modded item from the iterable object on the for loop

list_n = [it[0] for it in list_k]
# This syntax allows to build a new list on which every item is a subitem from the iterable object on the for loop

list_o = [it[1] for it in list_k]
# This syntax allows to build a new list on which every item is a subitem from the iterable object on the for loop

# To control the flow of the list comprenhesion we can add 'if' statements to condition the addition of every item to
# this new list

list_p = [it[1] for it in list_k if it[1] > 20]
# A simple if statement can be place both at the beginnig and at the end of the "for" statement

list_q = [it[1] if it[1] > 20 else 'no' for it in list_k]
# A  simple if/else statement can be place both at the beginnig and at the end of the "for" statement
# This else statement offers a alternate value for the item if the first "if" statement 
# fails to be satisfied

# Items in lists can be sorted
list_r = [0,1,2,3,4,5,6,7,8,9]

list_r[0], list_r[9] = list_r[9], list_r[0]

print (list_r)

# -----------------------------------------------------------------
# --------------------------- Dictionaries ------------------------
# -----------------------------------------------------------------

# Dictionaries are a type of object that stores values related to a names
# that can be accesed by the dictionary variable and values name
# Dict can be created by declaring a set of '{}'

client = {}
print ('client = ',client,'\ntype = ',type(client)) 

# To declare a new field on this dictionary we place the keyword as a values 
# index and then the value

client ['reference'] = '2dsfs3'
print (client)

# A value can be updated by declaring once more the value stored on the dictionary
client ['reference'] = 'wow, new value'
print (client)

# Values from a dictionary can be accessed by indexing a name from the dictionary
print ("client ['reference'] = ", client ['reference'])

# To declare several values on a dictionary it can be done at the time of declaring
# a dictionary

provider = {
    'name':'Nic CO',
    'number': '+59884111542',
    'address':'Paper St. 33',
}
print (provider)
print ("provider ['number'] = ",provider ['number'])

# The dict function allows to create a dictionary employing several **kwargs 
# and its values

deals = dict(id = 112151, date = '14/22/99')
print (deals)
print ("deals['id'] = ",deals['id'])

# If for a key is provided more than one value it stores a tuple

product = {}
product ['id'] = '122215','554863'
print ("type(product ['id']) = ",type(product ['id']))

# A dictionary can store any type of object as value
product ['color'] = ['blue','red']

print ("product ['color'] = ", product ['color'])
print ("type(product ['color']) = ", type(product ['color']))

# To avoid error while calling a value from a dictionary if it doesn't 
# exists, the 'get ()' method will return 'None' if key is not in the dict

print("product.get ('Last shipped to') = ",product.get ('Last shipped to'))

# In case is required to offer a default value different from 'None' the get
# method allows to recieve a such value

print("product.get ('Last shipped to','Value not defined') = ",product.get ('Last shipped to','Value not defined'))

# There are several methods that can be used in dictionaries

dict_a = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}

dict_b = dict_a.copy()
# Returns a copy of a dict

dict_a.clear()
# To clear values from a dictionary 

# A dict can be declared by providing a set to the 'dict.fromkey()' method to place the keys of a dict from a set
set_a = {'reference', 'name'}
print (set_a)

dict_c = dict.fromkeys(set_a)
print (dict_c)

# If provided a plain value, every key will have it as a value
palin_value = 115

dict_d = dict.fromkeys(set_a,palin_value)
print (dict_d)
# A new dictionary has been made

dict_e = {
    'main': 'Courier',
    'companion1': 'Boone',
    'companion2': 'ED-DE',
}

item_view = dict_e.items()
print ('Original dict = ', item_view)

dict_e ['main'] = 'Price'
print ('Modified dict = ', item_view)
# Will return a <class 'dict_items'>. This type of object is cathegorized as a view object and is used to have a better view
# on changes made to dictionaries

dict_f = {
    'main': 'Cursed',
    'companion1': 'Lucatiel',
}

key_view = dict_f.keys()
print ('Original dict = ', key_view)

del dict_f ['companion1']
print ('Modified dict = ', key_view)
# Will return a <class 'dict_keys'>. This type of object is cathegorized as a view object and is used to have a better view
# on the keys of the dict

dict_g = {
    'main': 'Mario',
    'companion1': 'Luigi',
}

value_view = dict_g.values()
print ('Original dict = ', value_view)

del dict_g ['companion1']
print ('Modified dict = ', value_view)
# Will return a <class 'dict_values'>. This type of object is cathegorized as a view object and is used to have a better view
# on the values of the dict

dict_h = {
    'main': 'Soap',
    'companion1': 'Price',
}

dict_i = dict_h.popitem()

print ('dict_h = \n',dict_h)
print ('dict_i = \n',dict_i)
# Will return the last item which will be deleted from the dictionary and
# modifies the provided dictionary 
dict_j = {
    'main': 'Cursed',
    'companion1': 'Lucatiel',
}

dict_j.setdefault('companion2', 'Pate') 
print ('dict_j = \n',dict_j)
dict_j.setdefault('companion3') 
print ('dict_j = \n',dict_j)
dict_j.setdefault('companion1', 'Aslatiel') 
print ('dict_j = \n',dict_j)
# Will return a new default value for a key, and if it doesn't exist will add
# this new key with "None" value. If passed an existant value it wont make any change

dict_k = {
    'main': 'Solid Snake',
    'companion1': 'D-dog',
}

companion1 = dict_k.pop('companion1')

print ('companion1 = ',companion1)
print ('dict_k = ',dict_k)

companion2 = dict_k.pop('companion2', 'Quiet')
print ('companion2 = ',companion2)
print ('dict_k = ',dict_k)

main = dict_k.pop('main', 'Sahelanthropous')
print ('main = ',main)
print ('dict_k = ',dict_k)
# The 'pop()' method, when given a key from a dictionary, will return the last value on the list and 
# will eliminate the value as well as the key from the dictionary.
# If the is key not in the dictionary it will return a KeyError.
# If given the key and value to the 'pop()' method, and it is not on the dictionary
# it will return the value and let the  rest intact.
# If given the key and value to the 'pop()' method, and the value doesn't match
# it will return the original value of the dictionary and delete the key from the dictionary

dict_l = {
    'main': 'Big Daddy',
    'companion1': 'Little sister',
}

dict_m = {
    'plasmids':'All of them',
}
dict_l.update(dict_m)
print ('Updated1 dict_l = ',dict_l)

dict_n = {
    'plasmids':'Half of them',
}
dict_l.update(dict_n)
print ('Updated2 dict_l = ',dict_l)

dict_l.update(weapon = 'Of choice', map = '1st')
print ('Updated3 dict_l = ',dict_l)
# The 'update()' method, given a new dictionary, will return 'None' and will modify
# the dictionary. If such key already exists, it will update it's value.
# The 'update()' method can recieve a tuple of keywords arguments and update
#  the dictionary

# -----------------------------------------------------------------
# --------------------- Dictionary comprenhension -----------------
# -----------------------------------------------------------------

# Comprenhension expresion allow un to declare and build data for a dictionary
# with less lines of code adding the constructor of the dictionary within its 
# declaration

list_dict = [0,1,2,3,4,5,6]
dict_o = {x: str((x*2)+1) for x in list_dict}

print ('dict_o = ',dict_o)
# This syntax will return a dictionary

dict_p = {
    'bank acc 1': 2255,
    'bank acc 2': 855,
    'bank acc 3': 781,
    'bank acc 4': 22,
}

currency_equivalent = 7.5

dict_q = {item: value * currency_equivalent for (item,value) in dict_p.items()}
print ('dict_q = ',dict_q)
# This syntax allows to build a dictionary modified from another dictionary

dict_r ={
    'warrior1 level': 55,
    'warrior2 level': 45,
    'warrior3 level': 75,
    'warrior4 level': 788,
}

dict_s = {item: value for (item,value) in dict_r.items() if value > 50}
print ('dict_s = ',dict_s)
# This syntax allows to build a dictionary using  a "if" statement on the items and keys of 
# another dictionary

dict_t = {item: value if value > 55 and value < 1000 else 'no' for (item,value) in dict_r.items()}
print ('dict_t = ',dict_t)
# This syntax allows to build a dictionary using a little more complex "if" statements on the items and keys of 
# another dictionary

dict_v = {
    x1 : {item1: x1 for item1 in range (0,5)} for x1 in range (0,3)
}

print ('dict_v = ',dict_v)
# Dictionary comprenhension can be achieved with nested elements

for i in dict_r:
    print ('i = ',i)
    print ('dict_r ['+i+'] = ',dict_r[i])
# A for loop over a dictionary will take as the iterative variable the keys of the dictionary

# -----------------------------------------------------------------
# ------------------------------ Tuples ---------------------------
# -----------------------------------------------------------------

# Tuples are a type of variable inmutable, which means that once declared cannot be changed
# Tuples are decared with "()" and can store any type of values and are comma separated, but also
# can be declared by separating values with commas

tup_a = ()
print ('tup_a = ',tup_a)
print ('type(tup_a) = ',type(tup_a))
# Empty tuple declared

tup_b = ('Cactus',123, [{'no'},True],(1.558))
print ('tup_b = ',tup_b)
# Tuple with different data types in it

tup_c = [{'no'},True],(1.558),'Cactus',123
print ('tup_c = ',tup_c)
# Tuple declaed without parenthesis

# Unpacking can be declaed by setting the ammount of variables we want from a tuple
tup_d = ('Homer', 'Marge', 'Lisa', 'Bart', 'Maggie')

dad, mom, mid, older, younger = tup_d
print ('dad, mom, mid, older, younger = ',dad, mom, mid, older, younger)
# For every tuple item there's a variable that stores tuples values

dad, *dads_family = tup_d
print ('dad = ',dad)
print ('dads_family = ', dads_family)
# For the first theres a variable and the rest of the tuple theres a list that stores tuples values

*youger_siblings_family, younger = tup_d
print ('youger_siblings_family = ', youger_siblings_family)
print ('younger = ',younger)
# For the last there's a variable and the rest of the tuple theres a list that stores tuples values

tup_f = (0,1,2,3,4)
print ('tup_f[0] = ',tup_f[0])
print ('tup_f[1] = ',tup_f[1])
print ('tup_f[-1] = ',tup_f[-1])
print ('tup_f[1:-1] = ',tup_f[1:-1])
# A tuple can be sliced as a list

# Mutable objects can be updated on a tuple

tup_g = (0,1,2,3,[0,1,2,3,4])
tup_g[4][0] = 'Muted'
print (tup_g)
# Mutable object within tuple is muted

tup_h = (0,1,2,3,4)
tup_i = (6,6,7,8,9)
tup_h + tup_i

print ('tup_h =',tup_h)
print ('tup_i =',tup_i)
print ('tup_h + tup_i = ',tup_h + tup_i)
# Tuples can be concatenated

# There are a few methods that can be used on tuples

tup_j = ('Fun','No fun','Not so fun')

print ("tup_j.count('Fun') = ",tup_j.count('Fun'))
# The 'count ()' method for tuples recieves a string and returns the ammount of times a value is this tuple

print ("tup_j.index('Not so fun') = ",tup_j.index('Not so fun'))
# The 'count ()' method for tuples recieves a string and returns the index of the value in this tuple

print ("'No fun' in tup_j = ",'No fun' in tup_j)
# Returns a boolean variable for the 'in' operator

for item in tup_j:
    print ('item in tup_j', item)

# -----------------------------------------------------------------
# ------------------------------ Sets -----------------------------
# -----------------------------------------------------------------

# Sets are a object taht allows to store mutable and inmutable data types. These objects
# dont store duplicated values.
# Sets are declared using '{}' including every value meant to be stored in a set separated by a comma
# Sets only allows hashable/inmutable types. 
# Sets are mutable themselves and un indexable

set_a = {'The providence: which is generous and brings everything whic is good'}
print ('set_a = ',set_a)
print ('type(set_a) = ',type(set_a))

# Sets can store any data types
# set_b = {['Either:', 'victory,'],'or',('lessons'), 411}

set_b = {0,1,2,3,4,'Corndog'}
print ('set_b = ',set_b)

set_c = {(0,1,2,3,4),'Corndog',3.14159,'Corndog','Corndog'}
print ('set_c = ',set_c)
# All datatypes are unmutable 

list_set = ['All','my','favourite','colors']
tup_set = ('My','sisters','and','my','brothers')
dict_set = {
    'they': None,
    'seem': None,
    'like': None,
    'no-other': None,
}

set_d = set(list_set)
print ('set_d = ',set_d)

set_e = set(tup_set)
print ('set_e = ',set_e)

set_f = set(dict_set)
print ('set_f = ',set_f)
# Sadly every set is  unordered

set_g = set()
print ('set_g = ',set_g)
# Empty sets are declared with the 'set()' function

# There are several methods that can be used on sets
set_h = set ([0,1,2,3])

print ('Original set_h = ',set_h)

set_h.add(4)
print ('Modified set_h = ',set_h)
# The'add()' method places a new value on the set

set_h.update([1,2,3],(2,3,4),{3,4,5})
print ('Updated set_h = ',set_h)
# The'add()' method places a every iterable item on the set avoiding duplicated

set_h.discard(5)
print ('Discarded 5 from set_h = ',set_h)
# The'discard()' method erased a item from the set. This method allows to
# attempt to erase values, either are o not in a set

set_h.remove(0)
print ('Removed 0 from set_h = ',set_h)
# The'remove()' method removes an item from the set
# set_h.remove(0) again will return a 'KeyError' because remove doesn't  have exceptions

set_h.pop()
print ('Poped a value from set_h = ',set_h)
# The'pop()' method removes an item from the set.

set_h.clear()
print ('Cleared set_h = ',set_h)
# The'pop()' method every an item from the set.

set_h.union({4,5})
print ('Unified set {4,5} with set_h = ',set_h)
# The 'union()' method modifies a set joining 2 sets together. This method
# is commutative

set_h.union({4,5})
print ('Unified set {4,5} with set_h = ',set_h)

set_h.intersection({4,5})
print ('Intersection {4,5} with set_h = ',set_h)
# The 'intersection()' method modifies a set only keeping 
# the common value of 2 sets together. This method is commutative

set_h.difference({4,5})
print ('Differnece set {4,5} with set_h = ',set_h)
# The 'differene()' method keep the valies that are only available on the set and not in the argument

set_h.symetric_difference({1,2,3,4,5})
print ('Symetric difference between  {1,2,3,4,5} and set_h = ',set_h.symetric_difference ({1,2,3,4,5}))
# The 'symetric_difference()' method modifies a set by keeping the uncommon values between 2 sets. 

set_o = {'Zero','One','Two','Three'}
set_p = set_o.copy()

print ('set_o = ',set_o)
print ('set_p = ',set_p)
# The 'copy()' method returns a copy of a set

set_k = {0,1,2,3,4}
set_l = {5,6,7,8,9}
set_m = {3,4,5}
set_n = {1}

print ('set_k.isdisjoint(set_l) = ',set_k.isdisjoint(set_l))
print ('set_l.isdisjoint(set_m) = ',set_l.isdisjoint(set_m))
print ('set_m.isdisjoint(set_n) = ',set_m.isdisjoint(set_n))
# The 'isdisjoint()' method returns boolean variable. It checks if there are not common values between sets

print ('set_n.issubset(set_k) = ',set_n.issubset(set_k))
print ('set_m.issubset(set_k) = ',set_m.issubset(set_k))
# The 'issubset()' method returns boolean variable. It checks if a set is contained within another set

print ('set_k.issuperset(set_n) = ',set_k.issuperset(set_n))
print ('set_m.issuperset(set_k) = ',set_m.issuperset(set_k))
# The 'issubset()' method returns boolean variable. It checks if a set contains another set

# There are several operators that can be used on sets
set_o = {'a','b','c','d'}
set_p = {'c','d','e','f'}

print ('set_o | set_p = ', set_o | set_p)
print ('set_p | set_o = ', set_p | set_o)
# The '|' operator returns the the union of 2 sets


print ('set_o & set_p = ', set_o & set_p)
print ('set_p & set_o = ', set_p & set_o)
# The '&' operator returns the common values of 2 sets

print ('set_o - set_p = ', set_o - set_p)
print ('set_p - set_o = ', set_p - set_o)
# The '-' operator returns the values that are only in the 1st set

print ('set_o ^ set_p = ', set_o ^ set_p)
print ('set_p ^ set_o = ', set_p ^ set_o)
# The '^' operator returns the values that are uncommon between sets

print ('1 in set_o = ', 1 in set_o)
print ('"c" in set_p = ', "c" in set_p)
# The 'in' operator returns a boolean if a value is in the set

for value in set_p:
        print ('Value from set_p = ', value)

# A set is iterable for every value within

# -----------------------------------------------------------------
# --------------------------- Frozen Sets -------------------------
# -----------------------------------------------------------------

# As tuples can be seen as unmutable lists, frozen sets can be seen as unmutable sets
# To create a frozen set is required to use the 'frozenset()' function and pass an 
# iterable argument. Frozen sets can be declared using the 'frozenset()' method.

list_forzen_set = [0,1,2,3,4,5,6]
frozen_set_a = frozenset(list_forzen_set)
print ('frozen_set_a = ',frozen_set_a)
print ('type(frozen_set_a) = ',type(frozen_set_a))
# This function returns a <class 'frozenset'> object

# To declare a frozen set empty we use the 'frozenset()' function without arguments
frozen_set_b = frozenset()
print ('frozen_set_b = ',frozen_set_b)
print ('type(frozen_set_b) = ',type(frozen_set_b))

# -----------------------------------------------------------------
# ------------------------- Set comprehension ---------------------
# -----------------------------------------------------------------

# Sets can have their items values declared by comprehensive statements

set_q = {value * 3 for value in range(0,55,10)}
print ('set_q = ',set_q)
# Returns a set

# -----------------------------------------------------------------
# --------------------------- Filter function ---------------------
# -----------------------------------------------------------------

# A filter function applies a filter to a given iterable using the 'filter()' fucntion and passing
# a function that discriminates a value 

list_to_filter = [0,1,2,3,4,5,6,7,8,9]

def filter_funct_a (item):
    if item > 3:
        return True
    else:
        return False

filtered_list = filter(filter_funct_a,list_to_filter)
print ('filtered_list = ',filtered_list)
print ('type(filtered_list) = ',type(filtered_list))
# The 'filter()' function returns a iterable <class 'filter'> object

filtered_list = list (filtered_list)
print ('Modified filtered_list = ',filtered_list)
print ('Modified type(filtered_list) = ',type(filtered_list))
# <class 'filter'> objects can be converted to lists using the 'list()' function

for item in filtered_list:
    print ('Filtered item = ', item)
    print ('Filtered type(item) = ', type(item))
# The filter object is iterable and all items remain the same from the unfiltered
# iterable object

random_list_to_filter = ['Yes', 'No', 223.5, True, False]

filtered_random_list = filter(None,random_list_to_filter)

for item in filtered_random_list:
    print ('Filtered item = ', item)
    print ('Filtered type(item) = ', type(item))

# Since there was only one 'Flase' value on the first list, there was only one item that missing

# -----------------------------------------------------------------
# ---------------------- Anonymous/Lambda function ----------------
# -----------------------------------------------------------------

# The Lambda Function allows to develop a small function specifying arguments and expresions

lambda_function_a = lambda x: x * 2

print ('lambda_function_a = ',lambda_function_a)
print ('type(lambda_function_a) = ',type (lambda_function_a))
print ('lambda_function_a (3) = ',lambda_function_a (3))
# The syntax of the lambda function can be stored on a variable which can recieve several arguments
# and return a tuple with its output variable

lambda_function_b = lambda x , y : ( x * 2, y + 3 )

print ('lambda_function_b (3,5) = ',lambda_function_b (3,4))
print ('type(lambda_function_b (3,4)) = ',type(lambda_function_b (3,4)))
# To declare multiple input variables, there has to be a comma that separates them right 
# after the lambda instruction is declared. For several output variables, a tuple is declared
# with as many items as variables we want as return

lambda_list_a = [
    ('p1',1255),
    ('p2',1547),
    ('p3',1000),
    ('p4',1745),
    ('p5',5000),
    ('p6',10000),
]

lambda_list_a.sort(key = lambda product_price: product_price [1], reverse=True)
# The 'sort()' method can recieve a 'lambda' function as a kwarg. In this case is used to
# return the index every nested iterable item which will dictate the agent to sort

lambda_tuple_a = (0,1,2,3,4,5,6)
filtered_lambda_a = filter (lambda x: x if (x <= 3) else (False), lambda_tuple_a)

for item in filtered_lambda_a:
    print ('item = ',item)
# Note that in this case there's no '0' item on the filtered iterable because Python interpretes 0 as 'False' or 0 == False (try it)

filtered_lambda_b = filter (lambda x: x if (x >= 3) else (False), lambda_tuple_a)

for item in filtered_lambda_b:
    print ('item = ',item)
# The lambda function returns a True value for every number equal or greater than 3, in such case the item value will be the itself

lambda_list_b = [0,1,2,3]
lambda_mapped_list = map(lambda x: x * 6 , lambda_list_b)

print ('lambda_mapped_list = ',lambda_mapped_list)
print ('type(lambda_mapped_list) = ',type(lambda_mapped_list))

for item in lambda_mapped_list:
    print ('item = ',item)
# This lambda function returns a value which will be 6 times the iterable item on the list

# -----------------------------------------------------------------
# ---------------------------- Map function -----------------------
# -----------------------------------------------------------------

# The 'map()' function will return a iterable which type is <class 'map'>. It stores values for each
# iterable instead of 'True' or 'False' output from the 'filter()' function. It's 

map_list_a = ['a','b','c','d','e']

def map_func (item):
    return 2*item

map_a = map (map_func,map_list_a)
print ('map_a = ',map_a)
print ('type(map_a) = ',type(map_a))
# The 'map()' function process, given rules dictated by a function, a iterator

set_map_a = set(map_a)
print ('set_map_a = ',set_map_a)
print ('type(set_map_a) = ',type(set_map_a))
# <class 'map'> can be converted on iterables using 'list()', 'tuple()', 'set()', or else to build iterables
# from the built-in functions
# Note: once iterated over a <class 'map'> it becomes empty since it's a packaged 'for' loop

map_tuple_a = (0,1,2,3,4,5,6)
map_b = map (lambda x: x*3 if (x <= 3) else (x - 3), map_tuple_a)

for item in map_b:
    print ('item = ',item)
# A lambda function can work to build a map

# Several iterables can be passed to the 'map()' function
map_tuple_b = (0,1,2,3,4,5,6)
map_tuple_c = (7,8,9,4,5,6,1,11111111111)
map_c = map (lambda x,y: ([x + y, x - y]) , map_tuple_b,map_tuple_c)

for item in map_c:
    print ('item = ',item)
# For several iterables the iteration process will last as long as the shortest iterable

# -----------------------------------------------------------------
# ---------------------------- Zip function -----------------------
# -----------------------------------------------------------------

# 'zip()' functions iterate several iterables at the same time returning each item of every iterator one step at a time.
# There are declarated by simply using the sentence 'zip()'

zip_a = zip()

print ('zip_a = ',zip_a)
print ('type(zip_a) = ',type(zip_a))

# It can recieve a tuple of iterators
zip_list_a = ['0 item list','1st item list','2nd item list','3rd item list', '4th item list']
zip_tuple_a = ('0 item tuple','1st item tuple','2nd item tuple','3rd item tuple')

zip_b = zip (zip_list_a,zip_tuple_a)
print ('zip_b = ',zip_b)
print ('type(zip_b) = ',type(zip_b))
# This <class 'zip'> objects are instrutions, that once employed cannot be accessed once again

for list_item,tuple_item in zip_b:
    print ('list_item = ',list_item)
    print ('tuple_item = ',tuple_item,'\n')
# For several iterables the iteration process will last as long as the shortest iterable

zip_c = zip (zip_list_a,zip_tuple_a)
zip_set_b = set (zip_c)

for item in zip_set_b:
    print ('item = ',item)

# Note: once iterated over a <class 'zip'> it becomes empty since it's a packaged 'for' loop
# <class 'zip'> can be converted on iterables using 'list()', 'tuple()', 'set()', or else to build iterables

# -----------------------------------------------------------------
# ------------------------ Array Data Structure -------------------
# -----------------------------------------------------------------

# Arrays are a data structure used to store large ammounts of data or numbers. Arrays are recommended if there are 
# perfomance issues over other data structures.
# To use the Array Data Structure we have to import the array class from the array module

from array import array

# An array is defined recieving a 'type code' which is the data type it will store
# Every 'type code' is described on Pythons array documentation https://docs.python.org/3/library/array.html
list_array_a = [0,1,2,3,4,5,6,7,8,9]
array_a = array('i', list_array_a)

print ('array_a = ',array_a)
print ('type(array_a) = ',type(array_a))
# An array will only recieve the data type declared

array_a.append (10)
print ('Modified array_a = ',array_a)
# The append instruction will place a value at the end of the array

# Try array_a.append (10.1)
# print ('Error array_a = ',array_a)
# TypeError: integer argument expected, got float

# -----------------------------------------------------------------
# ---------------------------- Generators -------------------------
# -----------------------------------------------------------------

# Generators are a instruction to build a logic ensemble with less resource consumption
upper_threshold = 1000
generator_a = (((x +5) / 2) for x in range(0,upper_threshold,2) )
print ('generator_a = ',generator_a) 
print ('type(generator_a) = ',type(generator_a))

comprehensive_list = [((x +5) / 2) for x in range(0,upper_threshold,2)]
print ('comprehensive_list = ',comprehensive_list) 
print ('type(comprehensive_list) = ',type(comprehensive_list))

# To know if a process is more resource efficien we'll use a function called 
# 'getsizeof()' from the sys module

from sys import getsizeof

print ('Size of generator = ',getsizeof (generator_a))
print ('Size of comprehensive list = ',getsizeof (comprehensive_list))


# -----------------------------------------------------------------
# ------------------------ Unpacking Operators --------------------
# -----------------------------------------------------------------

# Un-packing operators unpack the values of a iterable without the actual syntax
# To unpack a set of values there has to be a '*' before the iterable's variable name

unp_operators_1 = [0,1,2,3]
print ('*unp_operators_1 = ',*unp_operators_1)
# The values are printed one next to another

unp_operators_2 = tuple (range(0,50,2))
print ('*unp_operators_2 = ',*unp_operators_2)
# There can be unpacked values from avary iterable

unp_operators_3 = [0,1,2,3,4]
unp_operators_4 = [5,6,7,8,9]

unp_operators_5 = [*unp_operators_3, *unp_operators_4]
print ('unp_operators_3 = ',unp_operators_3)
print ('unp_operators_4 = ',unp_operators_4)
print ('unp_operators_5 = ',unp_operators_5)
# Unpacking operators is a useful tool to merge lists

unp_operators_6 = {
    'name':'Richard',
    'last name':'Sanchez',
}

unp_operators_7 = {
    'reality':'C-136',
    'threat':'high',
}

unp_operators_8 = {
    'response':'capture',
    'crimes':'all'
}

unp_operators_9 = {**unp_operators_6,**unp_operators_7,**unp_operators_8,'location':'earth'}
print ('unp_operators_9 = ',unp_operators_9)
# The '**' implies that there will be any numbers of keywords and values
# meant to be unpacked

# -----------------------------------------------------------------
# ------------------------ Recursive functions --------------------
# -----------------------------------------------------------------

# A recursive function is a function that calls itself on its definition

def rec_func_a(x):
    if x == 0 or x == 1:
        return 1
    else:
        return (x * rec_func_a(x-1))

# This function calls itself several times


n = 10
factorial_value = rec_func_a (n)
print ('Factorial of', n,'= ', factorial_value)
# The values is, in fact 3.628.800

# Note that x, which has to be an integer, will be multiplied by the 
# return value of the function when passed the value x-1 until it reaches 1 or 0.

# If a recursive function enters on a infonite loop it will be terminated under the
# RecursionError

def rec_func_b ():
    rec_func_b ()

rec_func_b ()

# To get the systems recursion limit it has to be consulted using the 'sys' module

from sys import getrecursionlimit

print (getrecursionlimit())
# This limit avoids the infinite recursion of a function

# -----------------------------------------------------------------
# --------------------------- Error handling ----------------------
# -----------------------------------------------------------------

# Python have 2 types of error:
# 1 - Syntax Errors: These surge from not following Python's ways of writing code
# 2 - Logical Errors (Exceptions): These surge from the occurance of a logical missprocedure

# https://docs.python.org/3/library/exceptions.html

# Syntax error example:
# if 1 < 2
# There will be a syntax error because the statement requires to end with a ':'

# Logical error
# a = 4 / 0
# There's a logical error due to the impossibility to divide by 0

# Syntax error can be eliminated by: 
# 1 - Writing the code correctly according the Python's version
# 2 - Having the right dependencies installed

# Logic Errors can be handled is a ilogical condition can occur at a given statement of the code
# and an example of this can be the input of a value

# Note: Logic errors are called 'Exceptions'

# The exceptions can be administrated with several path that the program can use in case of facing a exception

exceptions_a = input ('Introduce a number\n')

try:
    print ('Half input = ',float(exceptions_a)/2) # First path
except:
    print ('Input is not a number') # Secondary path 
# The 'try/except' statements creates a two paths to handle exceptions that doesn't crash if a error rises

# For a paticular type error an exception can arise

exceptions_b = input ('Introduce a number\n')

try:
    print ('Half input = ',float(exceptions_b)*3) # First path
except ValueError:
    print ('Input is not a number') # Secondary path 
else:
    print ('No errors here') # Third path 

# An 'else' statement works as a third path which works if no exception arises

# For a particular type of error several data can be shown

exceptions_c = input ('Introduce a number\n')

try:
    print ('Half input = ',float(exceptions_c)*3) # First path
except ValueError as val_error:
    print ('Input is not a number') # Secondary path 
    print ('Except = ',val_error)
    print ('Type of except = ',type(val_error))
else:
    print ('No errors here') # Third path 
# For this particular type of exception shere's a associate object type <class 'ValueError'> whith an explination on how
# or why this exception has arised

# In case there's no expected type of exception there can be use a system instruction from the 'sys' module

from sys import exc_info

exceptions_list_a = ['a','Dog', ['asdasd'] ,9,]

for item in exceptions_list_a:
    try:
        print ('Item = ', item)
        value = 1 / int(item)
        break
    except:
        print ('Exception arised')
        exception = exc_info()
        print ('Exception object =',exception)
        print ('Exception type =',type(exception))
        for except_item in exception:
            print ('Except item info = ',except_item)
        print ('\nNext entry\n')

print ('\n')
print ('The inverse of ',item,' is ',value)
# The 'exc_info()' returns a tuple that has several values related
# 1 - Type of error
# 2 - Description of the error
# 3 - The traceback object

# The ZeroDivisionError occurs every time a value is divided by zero
exceptions_list_b = [2,1,0]
for item in exceptions_list_b:
    try:
        print ('9/',item,' = ',9/item)
    except ZeroDivisionError as zde:
        print ('ZeroDivisionError = ',zde)
        print ('ZeroDivisionError type = ',type(zde))
    else:
        print ('Next item')
# As previous exceptions this can return valuable information about the type of error

# In case several type of errors are expected there can be plced several error excepts
exceptions_list_c = ['a',2,1,0]
for item in exceptions_list_c:
    try:
        print ('9/',item,' = ',9/item)
    except ZeroDivisionError as zde:
        print ('ZeroDivisionError = ',zde)
        print ('ZeroDivisionError type = ',type(zde))
    except TypeError as te:
        print ('ValueError = ',te)
        print ('ValueError type = ',type(te))
    else:
        print ('Next item')

# A more practical way of handling exceptions are error tuple

exceptions_list_d = ['a',2,1,0]
for item in exceptions_list_d:
    try:
        print ('9/',item,' = ',9/item)
    except (ZeroDivisionError, TypeError):
        print ('Invalid value ')
    else:
        print ('Next item')
# This Error tuple handles the arrors located at the tuple

# There's an even more practical ways of handling errors using the 'finally' clause

exceptions_list_e = ['a',2,1,0]
for item in exceptions_list_e:
    try:
        print ('9/',item,' = ',9/item)
    except (ZeroDivisionError, TypeError):
        print ('Invalid value ')
    else:
        print ('Next item')
    finally:
        print ('Item = ', item)

# The 'finally:' statement is used to place instructions whichever is the 
# actual path that the algorithm pasees by

# -----------------------------------------------------------------
# --------------------------- With statement ----------------------
# -----------------------------------------------------------------

# The with statement is used in exception handling to simplify the management of resources
# This allows to automatically call methods over files. In the case of error
# handling, this with statement will aoutomatically use the 'close()' method

# file_name = input ('Input your file name\n')
file_name = '''C:\Users\Wilfred M PRO\Desktop\portfolio\study\python\notes.txt'''

try:
    with open (file_name,'w') as rand_file:
        print ('Wisdom acquired')
        print ('File object = ', rand_file)
        print ('File object type = ', type(rand_file))
        if 'Our all good providence' not in rand_file:
            rand_file.write ('\nOur all good providence')
        else:
            print ('All wisdom within')
except FileNotFoundError:
    print ('Input file does not exist')
finally:
    print ('This is the course of action')

# The 'with' statement calls several methods embeded on the object. In this case, the 'open()' object
# recieves a file address and creates a <class '_io.TextIOWrapper'> object which has methods such as:
# __init__()
# __enter__()
# __exit__()
# These methods are executed along with the 'with' statement

# -----------------------------------------------------------------
# ------------------------ Raising Exceptions ---------------------
# -----------------------------------------------------------------

# There can be raised type of exceptions if any given circumstance by using the 'rise'
# statement

def exception_a (n):
    if n < 0:
        raise ValueError ('Natural number cannot be less than zero')
    else:
        print ('Natural value')
    return n

print ('exception_a (1) = ',exception_a (1))
print ('exception_a (-1) = ',exception_a (-1))

# This function if n < 0 will return a 'ValueError: Natural number cannot be less than zero'

# For functions that rises errors there can be handled as done before

try:
    print ('exception_a (-1) = ',exception_a (-1))
except ValueError as error:
    print ('Error =\n',error)

# In this case there are several paths to sort the rised exceptions

# To evaluate the exception handlig we'll use the 'timeit' function from the 'timeit' module

from timeit import timeit

time_run_a = '''
def exception_a (n):
    if n < 0:
        raise ValueError ('Natural number cannot be less than zero')
    else:
        print ('Natural value')
    return n

try:
    # print ('exception_a (-1) = ',exception_a (-1))
    pass
except ValueError as error:
    pass
'''

time_run_b = '''
def exception_b (n):
    if n < 0:
        return None
    else:
        return n

try:
    # print ('exception_b (-1) = ',exception_b (-1))
    pass
except ValueError as error:
    pass
'''




print ('Test 1 WITH EXCEPTIONS:', timeit(time_run_a, number = 10000))
print ('Test 2 WITHOUT EXCEPTIONS:', timeit(time_run_b, number = 10000))
# These tests shows how much time does the raising exceptions consume compared to the 
# Alternative to only handling them

# -----------------------------------------------------------------
# ----------------------------- Classes ---------------------------
# -----------------------------------------------------------------

# Object oriented programming, also known as OOP, is a programming pradigm 
# Objects have 2 main characteristics:
# 1 - Attributes: Consists on what composes an object
# 2 - Behaviour: Consists on what a object can do and how it can do it

# To make an object we have to build a blue print of itself. Such a blueprint is called:
# Class. Every new functionallity has to be built within this blue print.
# To name a class is required to star a capital letter according to the Pascal's convention.

class Class_a:
    pass

print ('Class_a = ',Class_a)
print ('type(Class_a) = ',type(Class_a))
# This process builds a Class

# An instance of a object suposes the creation of a object from the blueprint made. The objects are
# created calling a class. The syntaxis to 

obj_a = Class_a()

print ('obj_a = ',obj_a)
print ('type(obj_a) = ',type(obj_a))
# Every Class seen, previous to this one, has been defined by Python as default. Every object seen is an instace of such Class

# Every Class defined can have nested functions called 'methods'. Every method is meant either to be applied to an object which has to be passed as an
# argument or to itself using the 'self' as a parameter.

class Class_b:
    def method_b(self):
        print ('This class has a method called "method_b"')

obj_b = Class_b()
obj_b.method_b()

# To check if a object is a instance of a Class is used the 'isinstance()' function, passing the object and the class itself

print (isinstance (obj_b,Class_b))
# This function returns a boolean object and allows us to see if a value is an instace of a Class

# Every object that shares a Class is an instance of such object

# -----------------------------------------------------------------
# --------------------------- Constructors ------------------------
# -----------------------------------------------------------------

# A constructor is a special method called when creatind a new object. It will recieve every variable used
#  within a Class.

# There's a particular method used by Python to initilize a object once declared which is __init__()
x_a = 1
y_a = 2

class Class_c:
    def __init__(self,x,y):
        self.x = x
        self.y = y

obj_c = Class_c(x,y)
# Class_c was constructed to accept 'x' and 'y' variables, even though it does nothing with them
# The 'x' and 'y' variables are atributes of the 'Class_c' which can be accessed like a method 
# but without adding the '()' at the end

print ('obj_c.x = ',obj_c.x)
print ('obj_c.y = ',obj_c.y)

print ('type(obj_c.x) = ',type(obj_c.x))
print ('type(obj_c.y) = ',type(obj_c.y))

# A 'self.' atribute can be accessed throughout the whole class

class Class_d:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def method_d(self):
        print (f'self.x = {self.x}')
        print (f'self.y = {self.y}')

obj_d = Class_d (1,2)
obj_d.method_d()

print ('obj_d.x = ', obj_d.x)
print ('obj_d.y = ', obj_d.y)

# -----------------------------------------------------------------
# ------------- Instance attribute & Class attribute --------------
# -----------------------------------------------------------------

# Class attributes: These variables are used to be embeded on the class itself
# These values can be accessed by every instance of the class.

# Instance attributes: These are declared while declaring a instance from a Class.
# In the prev 'obj_d' those attributes were declared when declaring 'obj_d' as an 
# instance of 'Class_d'.

class Class_f:
    z = 'Class attribute z'
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
    def method_f (self):
        print (f'self.x = {self.x}')
        print (f'self.y = {self.y}')

# Simple variable declared with generic value
x_f1 = 33
y_f1 = 44

obj_f1 = Class_f(x_f1,y_f1) # Once these 2 simple variables are passed to the object definition they will
# give its value to the instance 'x' and 'y' attributes of this instance

x_f2 = 11
y_f2 = 22

obj_f2 = Class_f(x_f2,y_f2)
# This instance has its own instance attributes declared

obj_f1.method_f()
print ('obj_f1.z = ',obj_f1.z )
obj_f2.method_f()
print ('obj_f2.z = ',obj_f2.z )
# These 2 instance have their own instances attributes and  a common class attribute

# -----------------------------------------------------------------
# ---------------- Instance method & Class method -----------------
# -----------------------------------------------------------------

# Class methods: Are the type of class that defined on the Class employing a decorator and the 'cls' as a argument while being
# defined. These methods are employed when we want to access a method without declaring an overall instance. But just an 
# instace of a method
# Instance method: Are the methods copied while creating a new instace from a class. Instance methods behave as their
# Class instance dictates


class Class_g:
    z = 'Class attribute z'
    def __init__(self,x,y): # This is an instance method
        self.x = x 
        self.y = y 
    @classmethod
    def class_method_g(cls): # This is a Class method
        return 'class_method_g'
    def method_g (self): # This is an instance method
        return 'self.x = {self.x} \nself.y = {self.y}'

obj_g1 = Class_g(66,22)
print ('type(obj_g1) = ',type(obj_g1))
# Instance

obj_g2 = Class_g(11,99).method_g
print ('type(obj_g2) = ',type(obj_g2))
# Instance method

obj_g3 = Class_g(44,88).class_method_g
print ('type(obj_g3) = ',obj_g3)
# Class method

# To functionally call each instance, method and class method it is required to include the '()' expression at the 
# end of the declaration

obj_g4 = Class_g(44,88)
print ('type(obj_g4) = ',type(obj_g4))
# Instance

obj_g5 = Class_g (66,22).method_g()
print ('type(obj_g5) = ',type(obj_g5))
# Instance method

obj_g6 = Class_g(55,55).class_method_g()
print ('type(obj_g6) = ',obj_g6)
# Class method's return

# -----------------------------------------------------------------
# ------------------------ Magic Methods --------------------------
# -----------------------------------------------------------------

# Magic methods is a category of methods used build a class and are characterized by employing
# double underscore at the beginning and at the end of its names definition '__'. 
# Example: __init__
# These methods are meant to be employed by Python's interpreter instead of being used by user as a 
# available method to use. These are made to manipulate main Python's functionallity within the 
# declared Class

# For instance, when using the '+' operator, Python will call the '__add__()' method commonly used 
# by Python when dealing with 'float' or 'int' objects, but, if within a Class is declared a '__add__()'
# method, the behaviour of the '+' will change accordingly

magic_num_a = 5
magic_num_b = 10

print ('magic_num_a.__add__(10) = ',magic_num_a.__add__(10))
print ('magic_num_b.__add__(5) = ',magic_num_b.__add__(5))

print ('magic_num_a + magic_num_b = ',magic_num_a + magic_num_b)
print ('magic_num_b + magic_num_a = ',magic_num_b + magic_num_a)
# Every built-in object has its own set of magic methods

class Magic_a:
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
    def __str__(self):
        return '__str__ magic method for the Magic_a object return output'
    def method_f (self):
        print (f'self.x = {self.x}')
        print (f'self.y = {self.y}')

mag_inst_a = Magic_a (1,2)

print ('mag_inst_a.__str__() = ',mag_inst_a.__str__())
print ('str(mag_inst_a) = ',str(mag_inst_a))

print ('mag_inst_a.__str__() == str(mag_inst_a) ',mag_inst_a.__str__() == str(mag_inst_a))
# With the definition of the magic '__str__()' method of the Magic_a Class 
# the str() function calls for the 'Magic_a.__str__()' and returns  whatever this method returns

# Every object is independet from another, even though they share the same Class and defining arguments...

class Comp_a:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def method_a(self):
        print (f'self.x = {self.x}')
        print (f'self.y = {self.y}')

comp_inst_a = Comp_a (1,2)
comp_inst_b = Comp_a (1,2)

print ('comp_inst_a == comp_inst_b ',comp_inst_a == comp_inst_b)
# This conditional ends up being a 'False' statement

# (... unless) This conditional disposition can be modified changing the behaviour of the
# '__eq__()' method

class Comp_b:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y # The 'other' object is a reference to (you guessed) other object
    def method_b(self):
        print (f'self.x = {self.x}')
        print (f'self.y = {self.y}')

comp_inst_c = Comp_b(8,7)
comp_inst_d = Comp_b(8,7)

print ('comp_inst_c == comp_inst_d ',comp_inst_c == comp_inst_d)
# This conditional ends up being a 'True' statement

class Comp_c:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y 
    def __gt__(self, other): # 'gt' stands for 'greather than'
        return self.x > other.x and self.y > other.y # The 'other' object is a reference to (you guessed) other object
    def method_c(self):
        print (f'self.x = {self.x}')
        print (f'self.y = {self.y}')

# The '__gt__()' method analyzes the response of the '>' operator, in this case, this Class offers a compound response
# for two instances related
x1 = 3
x2 = 1

y1 = 4
y2 = 2

comp_inst_e = Comp_c(x1,y1)
comp_inst_f = Comp_c(x2,y2)

print ('comp_inst_e > comp_inst_f = ',comp_inst_e > comp_inst_f)
# In this particular case x1>x2 and y1>y2, which is the statement that guarantees the condition for a 'True' value
# of this statement

class Comp_f:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y 
    def __gt__(self, other): # 'gt' stands for 'greather than'
        return self.x > other.x and self.y > other.y # The 'other' object is a reference to (you guessed) other object
    def __lt__(self, other): # 'lt' stands for 'less than'
        return self.x < other.x and self.y < other.y # The 'other' object is a reference to (you guessed) other object
    def method_f(self):
        print (f'self.x = {self.x}')
        print (f'self.y = {self.y}')

# The '__gt__()' method analyzes the response of the '>' operator, in this case, this Class offers a compound response
# for two instances related
x1 = 1
x2 = 3

y1 = 2
y2 = 4

comp_inst_g = Comp_c(x1,y1)
comp_inst_h = Comp_c(x2,y2)

print ('comp_inst_h < comp_inst_g = ',comp_inst_g < comp_inst_h)
# The '__lt__()' method analyzes the response of the '<' operator, in this case, this Class offers a compound response
# for two instances related

# Note: The return statement can be subjected to any other conditional statement

# This same principle can be applied to these magic methods for comparison
# __ne__() 'Not equal'
# __ge__() 'Greater or equal'
# __le__() 'Less or equal'

# There are several magic methods related to the arithmetical operators

class Arith_a:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return (self.x + other.x,self.y + other.y) # Addition returns a tuple
    def __sub__(self, other):
        return (self.x - other.x,self.y - other.y) # Substraction returns a tuple
    def __mul__(self, other):
        return (self.x * other.x,self.y * other.y) # Multiplication returns a tuple
    def __floordiv__(self, other):
        return (self.x // other.x,self.y // other.y) # Floor division returns a tuple

arith_inst_a = Arith_a (100,200)
arith_inst_b = Arith_a (200,100)

print ('arith_inst_a + arith_inst_b = ',arith_inst_a + arith_inst_b)
print ('arith_inst_a - arith_inst_b = ',arith_inst_a - arith_inst_b)
print ('arith_inst_a * arith_inst_b = ',arith_inst_a * arith_inst_b)
print ('arith_inst_a // arith_inst_b = ',arith_inst_a // arith_inst_b)
# Since every return value is a tuple composed of the of two 

# -----------------------------------------------------------------
# ---------------------- Custom Containers ------------------------
# -----------------------------------------------------------------

class Container:
    def __init__(self): # This magic method initializes a dictionary
        self.bookmarks = {}
    def add (self, bookmark): # This method counts 1 to a key
        self.bookmarks[bookmark.lower()] = self.bookmarks.get(bookmark.lower(),0) + 1
    def __getitem__(self,bookmark):# This magic method sets a value for a non existing key
        return self.bookmarks.get(bookmark.lower(), 0)
    def __setitem__(self,bookmark,count): # This magic method sets a particular value for a key
        self.bookmarks[bookmark.lower()] = count
    def __len__ (self): # This magic method returns the overall len of the object
        return len (self.bookmarks)
    def __iter__(self): # This magic method for containers makes iterable object
        return iter(self.bookmarks)


container = Container ()
container_list = ['dog','cat','hamster','fish']
for animal in container_list:
    for i in range (0,10):
        container.add (animal)

# The add method adds a new value to a dictionary and updates its value adding 1 to itself


print ("container.get ('parrot') = ",container.get ('parrot'))
# The 'get()' methods behaviour is dictated by the '__getitem__' magic method

container ['parrot'] = 6
print ("container['parrot'] = " , container ['parrot'])
# This value assingment is dictated by the '__setitem__' magic method

print ("len(container) = ",len(container))
# The 'len()' methods behaviour is dictated by the '__len__' magic method

for items in container:
    print ('items = ',items)
# The iterable behaviour of this object is dictated by the ' __iter__' magic method

# To access the dictionary of the 'Container' Class can be accessed calling its defined name as a attribute

print ('container.bookmarks = ',container.bookmarks)

# In case is required to keep this dictionary unaccessible it has to be defined by adding double underscore
# '__' before the variable name


class ContainerForbidden:
    def __init__(self): # This magic method initializes a dictionary
        self.__bookmarks = {}
    def add (self, bookmark): # This method counts 1 to a key
        self.__bookmarks[bookmark.lower()] = self.__bookmarks.get(bookmark.lower(),0) + 1
    def __getitem__(self,bookmark):# This magic method sets a value for a non existing key
        return self.__bookmarks.get(bookmark.lower(), 0)
    def __setitem__(self,bookmark,count): # This magic method sets a particular value for a key
        self.__bookmarks[bookmark.lower()] = count
    def __len__ (self): # This magic method returns the overall len of the object
        return len (self.__bookmarks)
    def __iter__(self): # This magic method for containers makes iterable object
        return iter(self.__bookmarks)

containerforbidden = ContainerForbidden
try:
    containerforbidden.__bookmarks
except AttributeError:
    print ('containerforbidden.__bookmarks = AttributeError')

# Even though is not directly accesible it can be accessed using the '__dict__' method

print ('containerforbidden.__dict__', containerforbidden.__dict__)

# Simple excercise

class Containter_a:
    def inp_covertor(arg):
        # This function converts a string output into either a float if the posibility is given
        # or into a integer
        try:
            if float (arg) != int (arg):
                arg = float (arg)
                return arg
        except:
            try:
                arg = int(arg)
                return arg
            except:
                return arg
    def value_input_check (value):
        while value is None or value == '':
            value = input ('Introduce a value\n')
            if value is None or value == '':
                print ('Input a useful value')
        return value
    def key_input_check (key):
        while key is None or key == '':
            key = input ('Introduce a key\n')
            if key is None or key == '':
                print ('Input a useful key')
        return key.lower()
    def __init__(self):
        self.dictionary = {}
        self.list = []
        self.tuple = ()
        self.container_types = ['dictionary','list','tuple']
    def __len__(self):
        return (('Dict','List','Tuple'),(len(self.dictionary),len(self.list),len(self.tuple)))
    def __iter__ (self):
        return (iter(self.dictionary),iter(self.list),iter(self.tuple))
    def __getitem__(self, key):
        return self.dictionary.get(key.lower(),'No value')
    def __setitem__(self,key,value):
        self.dictionary[key.lower()] = value
    def add (self, key = None, value = None, container = None):
        # Let's have fun
        loop = True
        while (container is None or container == '' or container not in self.container_types):
            container = input ('Introduce container type (to quit type "NO")\n')
            if (container == '' or container not in self.container_types) and (container.lower() != 'no'):
                print ('Input a useful container type')
            elif container.lower() == 'no':
                loop = False
                break
        while loop:
            value = Containter_a.value_input_check (value)
            value = Containter_a.inp_covertor(value)
            if container == 'list':
                self.list.append (value)
                print ('Entry registered\n',self.list)
                loop = False
            elif container == 'tuple':
                self.tuple += (value)
                print ('Entry registered\n',self.tuple)
                loop = False
            elif container in 'dictionary':
                key = Containter_a.key_input_check (key)
                if key in self.dictionary:
                    print ('Name "{key}" taken\nadd a new key')
                    key = None
                elif value in self.dictionary:
                    print ('Value ',value,' registered\nadd new value')
                    value = None
                else:
                    self.dictionary [key] = value
                    print ('Entry registered\n',self.dictionary)
                    loop = False
    def containers(self):
        return (self.dictionary,self.list,self.tuple)

container_a = Containter_a()
container_a.add()

# This past Class, called 'Containter_a', has 5 main methods, appart of the constructor method, which declares 3 types of 
# containers:
# 1 - def inp_covertor(arg): This method tries to check if a input can be converted into float (if it can be converted) or into a int
# otherwise it returns the argument called 'arg' as a string
# 2 - def value_input_check (value): This method checks if we provide a value that is different to the 'None' or the '""'  (empty) value.
# If so, this method will be requested until such value is different to a null one.
# 3 - def key_input_check (value): This method checks if we provide a key that is different to the 'None' or the '""'  (empty) value.
# If so, this method will be requested until such key is different to a null one.
# 4 - def add (self, key = None, value = None, container = None): This method will take the containers declared on the '__init__(self)' method
# and check if such container is either ['dictionary','list','tuple'], if so, it will store any value or key acordingly. If the container type 
# doesn't exists within this list of bojects, it will request to input a valid one. If so, it will the add to the object specified such value.
# if such value/key exists it will require to define a new one
# 5 - def containers(self): This method will retun every container of this object. The return will be a tuple

# -----------------------------------------------------------------
# --------------------------- Property ----------------------------
# -----------------------------------------------------------------

# Property is a function used while defining a Class used to get and set values/ attributez in a formal way.
# The 'property()' function returns the managed attribute
# It recieves 4 functions:
# fget: Function that returns the value of the managed attribute
# fset: Function that returns the value of the managed attribute
# fdel: Function to define how the managed attribute handles deletion
# doc: String representing the property’s docstring

class PropertyA:
    def __init__(self):
        self.__name = '' # The name variable is a empty string as default
    def setname(self, name): # The 'setname(self, name)' method is used to set up a value, which is passed, to the 'self.__name' variable
        print('setname() called')
        self.__name=name
    def getname(self): # The 'getname(self)' method returns the 'self.__name'
        print('getname() called')
        return self.__name
    name = property (getname, setname) # This attribute is accesed under the 'getname(self)' and modified under the 'setname(self, name)' method. This conditioned behaviour is stablished by the 'property()' function


propert_a = PropertyA()

print ('propert_a.name = ',propert_a.name)
propert_a.name = 'Walter'
print ('propert_a.name = ',propert_a.name)

# Each Class can employ it's own set of methods to get and set values

class PropertyB:
    def __init__(self, value):
        self.set_value(value)
    def get_value (self):
        return self.__value
    def set_value (self,value):
        if value < 0:
            raise ValueError('Value cannot be less than zero')
        self.__value = value
    property_value = property (get_value,set_value)


propert_b = PropertyB (1)
print ('propert_b.property_value = ',propert_b.property_value)
try:
    propert_b = PropertyB (-1)
except ValueError:
    print ('Negative value')

# To make these methods private for intern use of the Class the '@property'
# This syntax requires to declare the '@property' declarator at the 'getter' method and make a sub decorator with the 
# name of the 'setter' method

class PropertyC:
    def __init__(self, value):
        self.value = value
    @property
    def value (self):
        return self.__value
    @value.setter
    def value (self,value):
        if value < 0:
            raise ValueError('Value cannot be less than zero')
        self.__value = value


propert_c = PropertyC (1)
print ('propert_c.value = ',propert_c.value)
try:
    propert_c.value = -99
except ValueError:
    print ('You probabli got a ValueError')


print ('propert_c.value = ',propert_c.value)
# This syntax allows us to build a a 'getter' and a 'setter' with the same name, using the respective decorator
# or allowing a function to have several methods/behaviours asociated to its name

# -----------------------------------------------------------------
# -------------------------- Inheritance --------------------------
# -----------------------------------------------------------------

# Inheritance is a feature that allows to build a new Class by copiying features from another classes
# Every Class that inherits a method is called sub/child/derived class
# The Class that provides a method to a sub/child/derived class is called parent/base class

class ClassA: # Parent/base
    def methoda(self):
        print ('method a')


class ClassB: # Parent/base
    def methodb(self):
        print ('method b')


class ClassC: # Parent/base
    def methodc(self):
        print ('method c')

class ClassD(ClassA,ClassB,ClassC): # Sub/child/derived
    def methodd (self):
        print ('method d')

d_object = ClassD()
d_object.methodd()
d_object.methodc()
d_object.methodb()
d_object.methoda()
# The ClassD() has several Parent/base which allows any instance to call every method
# of every single method of any Parent/base class

# For a instance of a Class with several parent is checked if is a instance of any of its 
# Parent/base Classes it will return a True value

print ('isinstance(d_object,ClassD) = ',isinstance(d_object,ClassD))
print ('isinstance(d_object,ClassC) = ',isinstance(d_object,ClassC))

# There's a base Class in Python called 'object' (which ironically is a function 'object()')
print ('isinstance(d_object,object) = ',isinstance(d_object,object))

# There's a way to check if a Class inherits from another Class
print ('issubclass(ClassD,ClassC) = ',issubclass(ClassD,ClassC))
print ('issubclass(ClassD,object) = ',issubclass(ClassD,object))
print ('issubclass(ClassC,ClassD) = ',issubclass(ClassC,ClassD))

# When a method from base Class is overwreitten by a method of a sub class it's said that it has been
# Overrided

class ClassE(ClassD):
    def methodd (self):
        print ('method d declared in ClassE')
    def methode (self):
        print ('method e')


e_object = ClassE()
e_object.methodb()
e_object.methodc()
e_object.methodd()
e_object.methode()
# The 'ClassE' is Overriding the 'methodd' which is first inherited from 'ClassD' and then redefined inside the 'ClassE'
# The Overriding applies to the magic methods as well

# To avoid overriding there can be used the 'super()' method. This places a method on top of the
# overriding hyerarchy

class ClassF:
    def __init__(self):
        self.value = 1

class ClassG(ClassF):
    def __init__(self):
        super().__init__()
        self.boolean = True

g_object = ClassG()

print ('g_object.value = ',g_object.value)
print ('g_object.boolean = ',g_object.boolean)
# This allows to keep values from the base method and adds the values from the actual SubClass

class ClassH:
    def method_common (self):
        print ('method_common ClassH')

class ClassI(ClassH):
    def method_common (self):
        super().method_common()
        print ('method_common ClassI')

i_object = ClassI()
print ('i_object.method_common(): ',i_object.method_common())
# It prints in order the 'method_common' print from 'ClassH' and then it returns the print from 'method_common' in 'ClassI' 
# If modified the position ofm the 'super()' method to the bottom of the 'ClassI' 'method_common'

class ClassJ:
    def method_common (self):
        print ('method_common ClassJ')

class ClassK(ClassJ):
    def method_common (self):
        print ('method_common ClassK')
        super().method_common()

k_object = ClassK()
print ('k_object.method_common(): ',k_object.method_common())
# In this case the 'method_common' from 'ClassK' is first excecuted and then is the 'method_common' from 'ClassJ'

# When it comes to inherit from a class a tupple is passed with every Parent/base Class.
# Every Parent/base method can be overrided by any other Parent/base method, standing at the end the Parent/base method
# first defined

class ClassL: # Parent/base
    def method_common(self):
        print ('method_common ClassL')

class ClassM: # Parent/base
    def method_common(self):
        print ('method_common ClassM')

class ClassN: # Parent/base
    def method_common(self):
        print ('method_common ClassN')

class ClassO (ClassL,ClassM,ClassN):
    pass

o_object = ClassO()
print ('o_object.method_common() = ',o_object.method_common())
# This object will take the inheritance of the 'method_common' from the first inherited 
# Class, in this case is the 'ClassL' 'method_common'

# If changed the order of the inheritage the overriding process will change

class ClassP (ClassM,ClassN,ClassL):
    pass

p_object = ClassP()
print ('p_object.method_common() = ',p_object.method_common())
# In this case is the 'ClassM' 'method_common' is the one employed by the SubClass 'ClassP'

# To avoid any poblem with overriding is a better to use methods with different name

# -----------------------------------------------------------------
# -------------------------- Data Classes -------------------------
# -----------------------------------------------------------------

# There are classes meant to store data in any model defined. Even though 2 objects may be instance
# of the same object and store the same data, both objects are not equal because both objects are stored 
# in different memory spaces

class DataClassA:
    def __init__(self, x, y):
        self.x = x
        self.y = y

data_class_a = DataClassA(2,3)
data_class_b = DataClassA(2,3)

print ('data_class_a == data_class_b :',data_class_a == data_class_b)

print ('id(data_class_a) = ', id(data_class_a))
print ('id(data_class_b) = ', id(data_class_b))
# These two objects are not equal

# Every object is stored in a memory adress that is different everytime a program is executed
# But there are several objects that have a constant and unique id, like integers from -5 to 256

# The behaviour of the '==' operator can me modified using the '__eq__()' method. This will return a True
# statetment even tough these objects have a different 'id()' value

class DataClassB:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

data_class_c = DataClassB (2,3)
data_class_d = DataClassB (2,3)

print ('data_class_c == data_class_d :',data_class_c == data_class_d)
print ('id(data_class_c) :',id(data_class_c))
print ('id(data_class_d) :',id(data_class_d))
# As seen before, this arrange of the '__eq__()' method allows us to create pbjects with different ID
# that can be considered equals

# To create objects that stores a simple amount of fields such as the previous example
# there's a simple way employing the 'namedtuple' object from the 'collections' module

from collections import namedtuple
# To declare a simple object there has to be provided 2 arguments:
# 1 - A string with a name for this object using the pascal's convention
# 2 - A list of fields that this object will store

NT = namedtuple ('NT',['name','age','address'])

nt_a = NT (name = 'Arnold', age = 24, address = 'EVERYWHERE')
nt_b = NT ('Arnold',24,'EVERYWHERE')

print ('nt_a = ',nt_a)
print ('type(nt_a) = ',type(nt_a))
# This a new object which name is defined when setting the namedtuple. In this case is 'NT'

print ('nt_a == nt_b :', nt_a == nt_b)
# The namedtuple is considered as the pythonic way to build a simple dataclass

# To get every value of every attribute we consider a simple getter method
print ('nt_a.name = ',nt_a.name)

# This type of object is inmutable. But it can recieve a change on any of it's values and store the changed value
# in the original namespace and memory space using the '_replace()' method

print ('id(nt_a) = ',id(nt_a))

nt_a._replace(name = 'NOT Arnold')
print ('Updated nt_a.name = ',nt_a.name)
print ('Updated id(nt_a) = ',id(nt_a))

# To get every field of data stored in the named tuple there can be used the '_fields()' method. This method
# returns a tuple

print ('nt_a._fields = ',nt_a._fields)
print ('type(nt_a._fields) = ',type(nt_a._fields))

# Once defined a named tuple, an instance can be used by passing a iterable and the '_make()' method over the namedtumple
nt_list = ['A Name', 55, 'An address']
nt_c = NT._make(nt_list)

print ('nt_c = ',nt_c)
# A named tuple has been created

# -----------------------------------------------------------------
# ---------------------------- Iterators --------------------------
# -----------------------------------------------------------------

# Iterator objects can be personalized employing the '__iter__()' and the '__next__()'
# These two magic methods are colectively called the 'iterator protocol'

# An object is iterable if an iterator can be get out of it. Most of containers have the iterator protocol

it_list = [0,1,2,3,4]

first_iterator = iter(it_list)
# This function calls the '__iter__()' method from our list

print ('type(first_iterator)', type(first_iterator))
# This type of iterator is a <class 'list_iterator'>

# Every value can be manually accessed using the 'next()' function
print (next(first_iterator))
print (next(first_iterator))
# This process can proceed using the '__next__()' method
print (first_iterator.__next__())
print (first_iterator.__next__())
# For this list, the return of the '__next__()' mthod will return a int
print ('type(first_iterator.__next__()) = ', type(first_iterator.__next__()))
# This function calls every value of the iterator until no more values are available

# If passed a iterator with no more values it will return a exception called 'StopIteration'
try:
    next(first_iterator)
except StopIteration:
    print ('No more values to iterate')

# The 'for loop' has 2 main variables when being executed:
# 1 - The name that we'll give to the return of the '__next__()' method until the 'StopIteration' exception apperears
# 2 - The iterable itself

# Internally a 'for loop' behaves like a 'while loop'

iterable = iter(it_list)

while True:
    try:
        variable_name = next(iterable) 
        print (variable_name)
    except StopIteration:
        print ('No more values to iterate')
        break
# This a modified but useful example on how for loops are built

# When declaring a Class a custom iterator can be build

class IteratorA:
    def __init__(self,value): # Constructor declares a value that has to be pass when intanciating this Class
        self.value = value
    def __iter__(self): # This method declares this objects as a iterable one
        self.n = 0
        return self
    def __next__(self): # This method declares how it will be iterable
        if self.n <= self.value:
            ret_value = self.value ** 2
            self.value -= 1
            return ret_value
        else:
            raise StopIteration

iterator_a = IteratorA(9)
# This instance have the capability to be iterated on

iterable_a = iter(iterator_a)
print ('type(iteratorable_a) = ',type(iterable_a))

# This iterable can provide values for every iteration which can be accessed and displayed using the 'next()' function or the '__next__()' method
while True:
    try:
        variable_name = next(iterable_a) 
        print (variable_name)
    except StopIteration:
        break

# 'iterator_a' can be used on a 'for loop' since it has a '__iter__()' and '__next__()' 
# or the called 'iterator protocol'
for value in iterator_a:
    print (value)

# The 'iter()' can recieve an aditional argument called sentinel, which will be a value meant to stop the iterator when such value is reached
# For this example the 'int()' function will be employed, which will return '0' when no argument is given

print ('int() = ',int())

iterable_b = iter(int,1)
# Since the return value of the iterable for 'int()' will never be anything different than '0'
# This is a infinite iterable

variable_name = next(iterable_b) 
print (next(iterable_b))
print (next(iterable_b))
print (next(iterable_b))
print (next(iterable_b))
# No different value than '0'

# A for loop will be infinite as well (interrupt it by uning Ctrl + c)

# for i in iterable_b:
#     print (i)

# There's a usage for infinite iterators. Different to the for loop, calling every next value of an iterator
# allows us to consume only the particular fraction of the processing resource to create the next output. With the 
# for loop every value is built

class IteratorB:
    def __iter__(self):
        self.num = 1
        return self
    def __next__(self):
        num = self.num
        self.num += 2
        return num

iterator_b = IteratorB()

iterable_c = iter(iterator_b)
print ('next(iterable_c) = ',next(iterable_c))
print ('next(iterable_c) = ',next(iterable_c))
print ('next(iterable_c) = ',next(iterable_c))
print ('next(iterable_c) = ',next(iterable_c))
print ('next(iterable_c) = ',next(iterable_c))

# -----------------------------------------------------------------
# --------------------------- Generators --------------------------
# -----------------------------------------------------------------

# There's a way to create a simple iterator without having to build a Class
# The generators are functions are functions that helps to build iterators

# This functions allows us to get any variable value after its exectution and it returns an iterator object
# Every value meant to be returned is served using the 'yield' expression

def generator_a ():
    x = 1
    print ('1st iteration')
    yield x
    x = 2
    print ('2nd iteration')
    yield x
    x = 3
    print ('3rd iteration')
    yield x


generator_instance_a = generator_a()
print ('type(generator_instance_a) = ',type(generator_instance_a))
# The Class of this type of function is <class 'generator'>

print ('next(generator_instance_a) =',next(generator_instance_a))
print ('next(generator_instance_a) =',next(generator_instance_a))
print ('next(generator_instance_a) =',next(generator_instance_a))
# This next iteration will raise a StopIteration exception
try:
    print ('next(generator_instance_a) =',next(generator_instance_a))
except StopIteration:
    print ('StopIteration exception reached')
# Once reached the end of the iteration the object won't work any further

generator_instance_b = generator_a()
# In a 'for loop' this generator will perform as with the 'next()' function

for value in generator_instance_b:
    print ('value', value)
# This 'for loop' runs trhough this generator until it ends

# There's a way to simply build a generator with generator expression
# Is created as the same way a comprenhension list is created but it uses '()' instead of '[]'

gen_expr = (x*2 for x in range(0,5))
print ('type(gen_expr) = ',type(gen_expr))
# The Class of this type of this expresion is <class 'generator'>

print ('next(gen_expr) = ',next(gen_expr))
print ('next(gen_expr) = ',next(gen_expr))
print ('next(gen_expr) = ',next(gen_expr))
# As well as with previous generators, the 'next()' function will return a many values as it can

# This generator expresions can be passed as an argument to a function in case a function recieves a generator as an argument

def generator_b (generator):
    while True:
        try:
            print ('item ', next(generator))
        except StopIteration:
            print ('Iterator stopped')
            break
# This functions iterates over a generator

generator_b (x**2 for x in range(0,5))
# This generator expresion builds a generator as a argument

print ('sum((x**2 for x in range(0,5)) = ',sum((x**2 for x in range(0,5))))
# Another example on how a generator can be passed as an argument

# Generator are easy to create and implement
def generator_c (value):
    n = 0
    while n <= value:
        yield value ** n
        n += 1

generator_instace_c = generator_c (8)
print ('next(generator_instace_c) = ',next(generator_instace_c))
print ('next(generator_instace_c) = ',next(generator_instace_c))
print ('next(generator_instace_c) = ',next(generator_instace_c))
print ('next(generator_instace_c) = ',next(generator_instace_c))

# Generators are used to represent an infinite stream of data

def generator_d():
    n = 0
    while True:
        yield n
        n += 2

generator_instace_d = generator_d()
print ('next(generator_instace_d) = ',next(generator_instace_d))
print ('next(generator_instace_d) = ',next(generator_instace_d))
print ('next(generator_instace_d) = ',next(generator_instace_d))
print ('next(generator_instace_d) = ',next(generator_instace_d))
# This procces can endlessly be executed being resource efficient

# Generator can be used in a 'pipeline' sequence
def generator_e(value): # This generators returns the n-th values of the Fibonaci sequence
    prev, curr = 0 , 1
    for _ in range(value): # A iterable range is built for the amount of numbers we want for the Fibonaci sequence
        yield prev # The yield instruction indicates that the return of this function is a generator
        prev, curr = curr , curr + prev # The value of the Fibonaci sequence is updated

def generator_d(generator): # This function recieves a generator as its argument
    for n in generator: # It iterates along it
        yield n ** 2 # It returns an generator itself

generator_e = generator_d(generator_e(7))
print ('next(generator_e) = ',next(generator_e))
print ('next(generator_e) = ',next(generator_e))
print ('next(generator_e) = ',next(generator_e))

# -----------------------------------------------------------------
# ---------------------------- Closure ----------------------------
# -----------------------------------------------------------------

# A closure is a function object that stores a value from nested functions (or enclosed scopes)
# To have a Closure there has to be a criteria reponding to these 3 aspects:
# 1 - There has to be a nested function
# 2 - The nested function must refer a value devined in the nest function
# 3 - The enclosing function must return the nested function

def closure_outer_a (message):
    def closure_inner_a ():
        print (message)
    closure_inner_a ()

closure_outer_a ('Cactus')
# This example shows how a nested function can access the nest variables/values

def closure_outer_b ():
    value = 7
    def closure_inner_b ():
        nonlocal value # Nonlocal statement allows to change the value of such variable
        print ('inner access value = ',value)
        value = 77
        print ('Updated inner access value = ',value)
    closure_inner_b ()
    print ('outer value =', value)

closure_outer_b()
# This example shows how a variable is available within a nested function to set new value

# To retrive data for a un-executed function which has recieved a variable we should return
# the inner function

def closure_outer_c ():
    value = 7
    def closure_inner_c ():
        nonlocal value # Nonlocal statement allows to change the value of such variable
        print ('inner access value = ',value)
        value = 77
        print ('Updated inner access value = ',value)
    return closure_inner_c

closure_return_c = closure_outer_c ()
print ('closure_return_c = ',closure_return_c)
print ('type(closure_return_c) = ',type(closure_return_c))
# The 'closure_inner_c' has been passed to the 'closure_return_c' variable

# If we decided to delete the 'closure_outer_c' function, the value stored on
# the 'closure_return_c' variable will remain

del closure_outer_c 
closure_return_c()
# The values stored in the 'closure_return_c' variable is called a reference and a reference to a function
# can be executed

# Closure can be used to pre charge values for a set of functions

def closure_outer_d (outer_value):
    def closure_inner_d (inner_value):
        value = inner_value ** outer_value
        print (f'The {outer_value} power of {inner_value} is {value}')
    return closure_inner_d

closure_return_c_3 = closure_outer_d (3)
closure_return_c_4 = closure_outer_d (4)

closure_return_c_3 (5)
closure_return_c_4 (6)
# This process offers an output that prints a value which is the n-th power of a  m-value
# This n-th vaule is provided to the enclosing function which then is called by the nested function
# The enclosing function returns the nested function which then recieves the m-value as the argument
# to then print the power relation

closure_return_c_3.__closure__
# The '__closure__' method returns a tuple with 1 item

closure_return_c_3.__closure__[0]
# The object stored has a data that can be called

closure_return_c_3.__closure__[0].cell_contents
# This attribute returns thw value passed to the 'closure_outer_d' in the first place

closure_return_c_4.__closure__[0].cell_contents
# This applies to every closure


# -----------------------------------------------------------------
# -------------------------- Decorators ---------------------------
# -----------------------------------------------------------------

# Decorator is a functionallity of Python that allows to add functionallity to a code
# in a process called meta-programming 

# 1 - Decorators work on Python objects. Which means that decorators works on every 
# value/container/class/function. There are no exceptions
# 2 - 

def decortator_a (string):
    print (string)
# A function can be created

decortator_b = decortator_a
# A function can be copied

decortator_a ('Altair')
decortator_b ('Ezio')
# Copied function have different outputs in this case

print ('id(decortator_a ("Altair")) = ',id(decortator_a ('Altair')))
print ('id(decortator_b ("Ezio")) = ',id(decortator_b ('Ezio')))
# In both cases, since a function was copied into a namespace, both functions haver the same id

# Functions that recieve anothert functions as an argument are called higher_level functions

def decorator_c (value): # Low order function
    return value + 1

def decorator_d (value): # Low order function
    return value - 1

def decorator_e (result, value): # High order function
    output = result (value)
    return output

decorator_instance_a = decorator_e (decorator_c,70)
decorator_instance_b = decorator_e (decorator_d,70)
# This high function order function recieves a function and pasees a value to it
# returning an aoutput of the nested return

# The closure is an fuctionallity to preserve or store values required for a nested function that
# are called from the nest function

def decorator_f ():
    def decorator_g():
        print ('Nested function output')
    return decorator_g

decorator_instance_c = decorator_f ()
decorator_instance_c ()
# This two lines of code are the same as the next one

decorator_f ()()
# This means that the return of that function will be executed as a function without arguments

# A Callable class is one that has the '__call__()'

# For practical porpuses we can call this functions on different ways

# Decorator
def decorator_h (func):
    def decorator_i():
        print ('Before func execution')
        func()
        print ('After func execution')
    return decorator_i

# Decorated
def decorator_j():
    print ('func itself')

# The decorator function adds extra functionallity (in this case 2 outputs) to a main
# function. If the decorators would have the form of flowers would be easier to notice

# For aestethics this example will be re writed

# Decorator
def decorator_h (func):
    def decorator_i():
        print ('Before func execution')
        print ('★彡[Decoration]彡★')
        func()
        print ('★彡[Decoration]彡★')
        print ('After func execution')
    return decorator_i

# Decorated
def decorator_j():
    print ('func itself')

decorator_j()
# This execution will return the Un-Decorated function's output

# But...

decorator_instance_d = decorator_h (decorator_j)
decorator_instance_d()
# Outputs a super awesome looking ultra pro version of the now Decorated function

# This is the base to understand decorators

# To use decorators there's a easier way previously seen which conditions the execution for a function
# passing it as an argument of a decorator function

def decorator_k (func):
    def decorator_l():
        print ('Before func execution')
        print ('★彡[Decoration]彡★')
        func()
        print ('★彡[Decoration]彡★')
        print ('After func execution')
    return decorator_l

@decorator_k # This is the decorator itself. The next function will be an argument for the decorator
def decorator_m():
    print ('func itself')

# @decorator_k is the same as decorator_k(decorator_m)
# When the decorated function is executed it will be passed through the decorator

decorator_m()
# Tadah!

# A function can be decorated with parameters

def decorator_n (func):
    def decorator_o (x,y):
        print (f"{x} / {y} = ")
        if y == 0:
            print ('Cannot divide by zero')
            return
        return func(x,y)
    return decorator_o

@decorator_n
def decorator_p (x,y):
    print (x/y)

decorator_p (2,4)
decorator_p (4,7)
decorator_p (4,0)
# This example shows how a function functionallity can be enhanced by a decorator

# In the case of expecting several arguments these can be accepted by the decorator
# using the '*args' or the '**kwargs'

def decorator_q (func):
    def decorator_r (*args):
        func (*args)
    return decorator_r

@decorator_q
def decorator_s (x,y,z):
    print (x*y*z)

decorator_s (3,4,'-')
decorator_s (6,7,9)
# This decorator passes any value to the 'decorator_s' function passed as a tuple

def decorator_t (func):
    def decorator_u (**kwargs):
        func(**kwargs)
    return decorator_u

@decorator_t
def decorator_v (a,b,c,d):
    print (a+b-(c+d))

decorator_v (a = 2, b = 5 , c = 8, d = 12)
# This decorator passes any value to the 'decorator_v' function passed as a tuple

# Decorators can be chained one to another, meaning an order of execution of every decorator function

def decorator_w (func):
    def decorator_x(*args):
        print ('1st decorator')
        func(*args)
    return decorator_x

def decorator_y (func):
    def decorator_z(*args):
        print ('2nd decorator')
        func(*args)
    return decorator_z

@decorator_w
@decorator_y
def decorator_aa (name,lastname):
    print (f'My full name is {name} {lastname}')

decorator_aa('Bearer','of the curse')
# This example shows how several decorator can be chained and are executed in the order
# that has ben passed

# -----------------------------------------------------------------
# --------------------------- Modules -----------------------------
# -----------------------------------------------------------------

# Modules refer to a file containing definitions or statements. This file name 'notes.py'
# is a python module itself. Every statement and definition within a module have to refer to each 
# other which makes this module self contained. Modules are used to break down large applications
# in small, manageable and organized parts meant to be used and reused by other modules

# To use another module outside of the current one we can import it.
# It's provided a new module in this same folder for every exercise provided in this
# study guide

# This module is called 'new_module.py'

# To import any object from a method a method has to be provided as an object from a module.
# Such instrction is paseed as following:

# In order to get Python to look in the current working directory, which is assumed to be on the same folder as this 
# file, it is required to change the current working directory of the terminal and then execute Python from there.

# Theres also a way to change the current working directory by importing the 'os' mdoule which comes with Python by unsing:
# 'import os'
# Then the 'os.chdir()' method allows to pass the directory as a string to can look for the
# provided module

from new_module import string1
from new_module import Class1
from new_module import function1
# This is how a particular object is imported. Any of these objects can be used in this module

print ('string1 = ',string1)
module_a = Class1()
print ('module_a.value1 = ',module_a.value1)
module_a.method1()
function1()
# This is how a particular object is called

# A more comfortable way to get objects from a module is to pass a tuple to import several values
from new_module import string1, Class1,function1

# In case is required the full module to be called it's recommended to import the whole module
import new_module
# To call any object from such module it will be called like a method using the 'dot' notation

print ('new_module.string1 = ',new_module.string1)
print ('new_module.Class1().value1 = ',new_module.Class1().value1)
new_module.Class1().method1()
print ('new_module.string1 = ',new_module.string1)
# This is the way any object is called within a module

# Every way of importing objects is equal on a performance scope

# There has to be consider the fact that when executing a module in Python it will create a caché folder
# which allows Python to strore and access every data required to execute that module

# Whenever Python tries to import a module Python searches for such a module on the currendt directory. If not found
# Python will access any of the locations/directories created when Python got installed

# To check which are these directories these instructions are meant to be followed

import sys
print (sys.path)
# This are all the folder created by Python's installer and there is where Python will look
# whenever it tries to get a module

# Python has a way to store the modules and set of modules.
#  'Packages' for directories and 'modules' for files.

# When developing a application is required to store similar modules in a same package
# and different modules in different packages. In this way a project can be easy to manage
# and is conceptually easier to develop.

# As directories have sub directories, a package can have sub packages

# To create a package there has te be created a directory with a '__init__.py' file in it
# There was made a package called 'package1' with a '__init__.py' and a 'module1.py' files

# To import a package there are several approachs.

# 1 -:
import package1.module1

package1.module1.module_1()
package1.module1.module_2()

# 2 -:
from package1.module1 import module_1,module_2

module_1()
module_2()

# 3 -:
from package1 import module1

module1.module_1()
module1.module_2()

# There was created another directory within the 'package1' directory called 'subpackage1' with
# a '__init__.py' and a 'submodule1.py' files

# To import the 'subpackage1' there's used the dot notation from 'package1' and from there
# the required module and sub module should be called

from package1.subpackage1 import submodule1

submodule1.submodule_1()

# Every subpackage has a set of modules, and every module have a set of methods
# These methods can be accessed using the 'dir()' function or the '__dir__()' method

print ('dir(submodule1) = ', dir(submodule1))
# The output of this function gives us every method related to this package

print ('submodule1.__name__ = ', submodule1.__name__)
# This method returns the name of the module

print ('submodule1.__package__ = ', submodule1.__package__)
# This method returns the package where this module belongs

print ('submodule1.__file__ = ', submodule1.__file__)
# This method returns the file name + location of the package

# -----------------------------------------------------------------
# --------------------------- Built-In ----------------------------
# --------------------------- Libraries ---------------------------
# -----------------------------------------------------------------

# Every package from the Standard Python Library can be found here:
# https://docs.python.org/3.8/library/

# -----------------------------------------------------------------
# ----------------------------- Path ------------------------------
# -----------------------------------------------------------------

# The Path library is a library made to manage in a easier way directory or file
# paths

from pathlib import Path

# To create an object that can be used to refer functional Python Path 
# we create an instance of the Path method

path_a = Path('C:\\Users\\Wilfred M PRO\\Desktop\\portfolio\\study\\python\\package1\\subpackage1')
print ('path_a = ',path_a)
print ('type(path_a) = ',type(path_a))
# This is a <class 'pathlib.WindowsPath'> object
# The usage of doubble '\\' is used to place a simple '\'

# To use a one '\' to place one '\', the 'r' argument is placed before
# the string. This is used to track every character in a raw string

path_b = Path(r"C:\Users\Wilfred M PRO\Desktop\portfolio\study\python\package1\subpackage1")
print ('path_b = ',path_b)
print ('type(path_b) = ',type(path_b))
# This is a <class 'pathlib.WindowsPath'> object

# A relative path is a path created to start from some point of the current working directory

path_c = Path(r"portfolio\study\python\package1\subpackage1")
print ('path_c = ',path_c)
print ('type(path_c) = ',type(path_c))
# This is a <class 'pathlib.WindowsPath'> object

# The current folder is represented by the argument-less 'Path' class
path_d = Path()
print ('path_d = ',path_d)
print ('type(path_d) = ',type(path_d))

# Theres a way to combine two path objects

path_e = Path(r"portfolio\study\python")
path_f = Path(r"\package1\subpackage1")
path_g = path_e / path_f
print ('path_g = ',path_g)
print ('type(path_g) = ',type(path_g))
# This is a <class 'pathlib.WindowsPath'> object

# Thre's a way to combine several strings to a path
path_h = Path(r"\package1\subpackage1") / r"\package1\subpackage1"
print ('path_h = ',path_h)
print ('type(path_h) = ',type(path_h))

# There's a way to get the user of the current working directory

print ('User directory = ',Path.home())
print ('type(Path.home()) = ',type(Path.home()))
# This is a <class 'pathlib.WindowsPath'> object

# Thre's a method that checks if a File or Folder exists

path_i = Path() # Relative current folder
path_j = Path(r'C:\Users\Wilfred M PRO\Desktop\portfolio\study\python\package1\__init__.py') # Relative path for a file
path_k = Path(r'\package1') # Relative folder

print ('path_i.exists() = ',path_i.exists())
print ('path_j.exists() = ',path_j.exists())
print ('path_k.exists() = ',path_k.exists())

# There are several methods to check Paths
print ('path_i.exists() = ',path_i.is_dir())
print ('path_j.exists() = ',path_j.is_dir())
print ('path_k.exists() = ',path_k.is_dir())
# Checks if a Path corresponds to a directory

print ('path_i.exists() = ',path_i.is_file())
print ('path_j.exists() = ',path_j.is_file())
print ('path_k.exists() = ',path_k.is_file())
# Checks if a Path corresponds to a file

print ('path_i.exists() = ',path_i.name)
print ('path_j.exists() = ',path_j.name)
print ('path_k.exists() = ',path_k.name)
# Returns the name atribute of the last part of this path wether is a 
# file or a directory

# To get the extension of a path (if the path is of a file) there's the suffix method
print ('path_i.exists() = ',path_i.suffix)
print ('path_j.exists() = ',path_j.suffix)
print ('path_k.exists() = ',path_k.suffix)

# In case a particular ending element of a path has to be changed there can be used a method
# called 'with_name()'

path_l = path_j.with_name('__new_name__.mp3')
print ('path_l = ',path_l)
print ('type(path_l) = ',type(path_l))
# This is a <class 'pathlib.WindowsPath'> object

path_m = path_i.absolute()
print ('path_m = ',path_m)
print ('type(path_m) = ',type(path_m))
# This is a <class 'pathlib.WindowsPath'> object
# Note that this value is the absolute path for the CWD

# To only change the suffix of a path there can be used the 'with_suffix()' method and provide a desired string

path_n = path_l.with_suffix('.new')
print ('path_n = ',path_n)
print ('type(path_n) = ',type(path_n))
# This is a <class 'pathlib.WindowsPath'> object

# -----------------------------------------------------------------
# ------------------------- Directories ---------------------------
# -----------------------------------------------------------------

# Directories are data containers on a OS. These can store files or other containers
# These have a path within a device and a name, and, such name and path is unique within 
# its's containing folder. These directories can be created, modified and erased.
# If a directory is modified, every other file or folder within such directory
# have threir path modified

# Python can manage directories employing Path objects

path_o = Path().absolute() / 'dir_example'
path_o.mkdir()
print ('path_o.exists() = ',path_o.exists())
# This instruction will create the 'dir_example' directory in our CWD and can create any directory given any Path

path_o.rename('UPDATED_dir_example')
# This instruction renames the directory

path_o = Path().absolute() / 'UPDATED_dir_example'
# It's stablished again the base-line

path_o.rmdir()
print ('path_o.exists() = ',path_o.exists())
# This instruction removes a directory given any path

directory_a = Path().absolute().iterdir()
print ('type(directory_a) = ',type(directory_a))
# The 'iterdir()' method returns a <class 'generator'> object

# There can be passed this generator to create a list
list_directory_a = [directory for directory in Path().absolute().iterdir()]
print ('list_directory_a = ',list_directory_a)
# This list stores all the Path objects related to every file within such directory

# such list can be filtered to retgurn a list with values that are 
# either files or directories
list_directory_b = [directory for directory in Path().absolute().iterdir() if directory.is_dir()]
print ('list_directory_b = ',list_directory_b)
# This list will store only directories within a directory

list_directory_c = [directory for directory in Path().absolute().iterdir() if directory.is_file()]
print ('list_directory_c = ',list_directory_c)
# This list will store only files within a directory

# Theres a way to filter files with some simple patterns using the 'glob()' method
list_directory_d = [directory for directory in Path().absolute().glob('*.py') ]
print ('list_directory_d = ',list_directory_d)

# To get every file regardless of its suffix
list_directory_e = [directory for directory in Path().absolute().glob('*.*') ]
print ('list_directory_e = ',list_directory_e)

# -----------------------------------------------------------------
# --------------------------- Files -------------------------------
# -----------------------------------------------------------------

# File is a data container that stores information. It has a format and is meant
# be accesed (or not), modified (or not), created (or not), and deleted (or not)
# These eceptions means that dependeding on the privileges or the directory where is sotred
#  these actions can be limited

# Python can manage files employing Path objects

# For the porpuse of the next file related excercises, there will be created the next files
# which are contained on the '.../exercises/files' folder

# 1 - 'example1.py'
# 2 - 'example2.py'
# 3 - 'example3.py'

path_p = Path().absolute() /  'exercises/files/example1.py'
path_q = Path().absolute() /  'exercises/files/example2.py'
path_r = Path().absolute() /  'exercises/files/example1.py'

print ('path_p.exists() = ',path_p.exists())
print ('path_q.exists() = ',path_q.exists())
print ('path_r.exists() = ',path_r.exists())
# This method checks if a file exists

path_r.rename ('__init__.py')
# This method renames every file. It has to be placed the corresponding suffix

path_q.unlink()
# The 'unlink()' method removes a file given any path

print ('path_p.stat() = ',path_p.stat())
print ('type(path_p.stat()) = ', type(path_p.stat()))
# This method returns a <class 'os.stat_result'> object

print ('path_p.write_bytes() = ',path_p.write_bytes(b'# Hello world!'))
# This object returns a integer for the ammount of bytes are written within the file and the
# data within this file has to be passed in the binary notation
# The binary notation is this form "b''"". Allows a string only within simple quote marks

print ('path_p.read_bytes() = ',path_p.read_bytes())
print ('type(path_p.read_bytes()) = ',type(path_p.read_bytes()))
# This method retunrs a <class 'bytes'> object. Its content is a binary object

print ('path_p.write_text() = ',path_p.write_text(r'print ("Hello world")'))
# This method allows to reviece a string and write a file

print ('path_p.read_text() = ',path_p.read_text())
print ('type(path_p.read_text()) = ',type(path_p.read_text()))
# This method returns a string containing the text within a file
# This returns a <class 'str'>

# Wtih the 'shutil' module a file can be copied from one location to another
import shutil

shutil.copy(path_p,Path())
# This will copy a file at any path to any other path

# -----------------------------------------------------------------
# ------------------------- Zip Files -----------------------------
# -----------------------------------------------------------------

# Zip files are a type of files that store several other objects. It encodes data to reduce
# it size in memory storage capability (bytes). To access files inside Zip files it's 
# required to decode or extract files first

# Python can manage Zip files employing Path objects and the 'zipfile' module

# For the porpuse of the next file related excercises, there will be created the next files
# which are contained on the '.../exercises/zip files' folder

# 1 - 'example1.py'
# 2 - 'example2.py'
# 3 - 'example3.py'

from zipfile import ZipFile

zip_a = ZipFile('exercises/zip file/example_1.zip','w')
print ('zip_a = ',zip_a)
print ('type(zip_a) = ', type(zip_a))
# This instruction will create a zip file in the pointed path and will return a <class 'zipfile.ZipFile'> object

# To add a file to a Zip file there has to be passed a Path object as an argument to the write method

path_s = Path () / 'exercises/zip file/example1.py'
path_t = Path () / 'exercises/zip file/example2.py'
path_u = Path () / 'exercises/zip file/example3.py'

zip_a.write (path_s)
zip_a.write (path_t)
zip_a.write (path_u)
# This returns a'.zip' file with the whole tree of the relative path within CWD it's
# This is has to be considered

zip_a.close()
# This instruction closes the file, leaving it available to access and modify for any other way

# There is a way to copy a whole branch of a directory tree

path_v = Path ()
zip_b = ZipFile('exercises/zip file/example_2.zip','w')
for path in path_v.rglob('*.*'):
    print (path)
    # zip_b.write(path)

# This 'for loop' will copy every file within a location

path_w = Path ()
zip_c = ZipFile('exercises/zip file/example_2.zip','w')
for path in path_w. rglob('*.py'):
    zip_c.write(path)
# This approach brings a way to filter some files and a branch

path_w = Path ()
zip_c = ZipFile('exercises/zip file/example_2.zip','w')
for path in path_w. rglob('*.py'):
    zip_c.write(path)