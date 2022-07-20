# -----------------------------------------------------------------
# -------------------------- Excercise 1 --------------------------
# -----------------------------------------------------------------


title_1 = '''-----------------------------------------------------------------
------------------------- 1 st Excercise ------------------------
------------------------- print from two ------------------------
----------------------------- values ----------------------------
-----------------------------------------------------------------'''

excercise_1 = '''Print the result of a multiplication of two sets of integers if the result is less than 1000.
If the result is greater than 1000, print the sum '''

print(title_1)
print(excercise_1)

# This function converts a string output into either a float if the posibility is given
# or into a integer. If an input cannot be converted into a numerical value it will loop
# again to ask for a useful value

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

# Here is excecuted the function storing the retunr valuue in two variables
print ('First number')
number_a = inp_covertor_a()
print ('Second number')
number_b = inp_covertor_a()
# Here these two value will be multiplied
number_c = number_a*number_b
condition = 'multiplied'
# The multiplied values will ve evaluated. If such value is bigger that 1000 it will be
# Changed that value to the sum of such values. Else nothing else happens
if number_c > 1000:
    number_c = number_a + number_b
    condition = 'sumed'

# The result will be printed
print (f'The numbers have been {condition} and the result is =',number_c)

# -----------------------------------------------------------------
# -------------------------- Excercise 2 --------------------------
# -----------------------------------------------------------------

title_2 = '''-----------------------------------------------------------------
------------------------- 2 nd Excercise ------------------------
------------------------- Iterate and sum -----------------------
----------------------------- values ----------------------------
-----------------------------------------------------------------'''

excercise_2 = '''Iterate from a firts number to a second number and then print the sum of that value with the previous one'''

print(title_2)
print(excercise_2)

def inp_covertor_b():
    while True:
        arg = input('Please input a number\n')
        try:
            arg = int(arg)
        except:
            # If the value cannot be converten into a either a floar or a interger the input will be 'False'
            arg = None
        # If the value is False it means that the input cannot be converted into a numerical value
        if arg != None:
            return arg
        print ('Input an useful value\n')


# Taking the 'inp_covertor()' function we proceed to recieve two values
print ('Starting value')
number_a = inp_covertor_b()
print ('Ending value')
number_b = inp_covertor_b()
# Is checked if there was a issue while 
if number_b < number_a:
    number_a , number_b = (number_b, number_a)
prev_value = 0
for value in range(number_a , number_b):
    sum_values = prev_value + value
    print ('Sum = ')
    prev_value = value

# -----------------------------------------------------------------
# -------------------------- Excercise 3 --------------------------
# -----------------------------------------------------------------

title_3 = '''-----------------------------------------------------------------
-------------------------- 3 rd Excercise -----------------------
------------------------- From string print ---------------------
----------------------- even-index characters -------------------
-----------------------------------------------------------------'''

excercise_3 = '''From a string print the characters on the even index values'''

print(title_3)
print(excercise_3)
# A function is made 
def function_a():
    # An input is requested
    input_a = input('Input any string\n')
    for index,char in enumerate(input_a): # The iterable is enumerated
        if index % 2 == 0: # Is checked if the index value is even or what is the same. if the index divided by two it returns 0 as a remain
            print (f'Even character {char}')# The even character is printed

# The function is excecuted
function_a()

# -----------------------------------------------------------------
# -------------------------- Excercise 4 --------------------------
# -----------------------------------------------------------------

title_4 = '''-----------------------------------------------------------------
-------------------------- 4 th Excercise -----------------------
------------------------ Remove n characters --------------------
--------------------------- From a String -----------------------
-----------------------------------------------------------------'''

excercise_4 = '''From a string print the characters on the even index values'''

print(title_4)
print(excercise_4)

def function_b():
    # A loop is initialized
    while True:
        input_a = input ('Input a string\n') # The string is requested
        print ('Input a value lesser than the lenght of a string')
        number_a = inp_covertor_b() # An integer input is requested
        if len(input_a) >= number_a: # The compatilibilty is checked
            print (f'Remaining string \n{input_a[number_a-len(input_a) :]}') # The remaining string is displayed
            break # The loop ends
        else:
            print ('Incompatibility between input') # The incompatibility is detected and the loop restarts

function_b()

# -----------------------------------------------------------------
# -------------------------- Excercise 5 --------------------------
# -----------------------------------------------------------------

title_5 = '''-----------------------------------------------------------------
-------------------------- 5 th Excercise -----------------------
---------------------- Check of repeated value ------------------
---------------------------- From a List ------------------------
-----------------------------------------------------------------'''

excercise_5 = '''Given two lists of numbers return true if the first and last value is the same'''

print(title_5)
print(excercise_5)

def function_c():
    def inp_covertor_c():
        while True:
            input_value = input('Please input a number\n')
            try:
                # If the value is zero or if the argument cannot be converted it will rise an exception
                # If the value float(arg) - int(float(arg)) == 0 it means that the input has no 
                # decimal value
                if float(input_value) - int(float(input_value)) != 0:
                    arg = float(input_value)
                else:
                    raise ValueError
            except:
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
        list_a = []
        print ('Input several values to a list\nWhen done type NO')
        while True:
            value_a = inp_covertor_c()
            if value_a == None: # If returned a False value the loop will break
                return list_a
            else:
                list_a.append (value_a) # In case is recieved a value the loop will continue to ask values to append 
    list = function_d() # Here the append function starts
    if list [0] == list [-1]: # Here is checked the condition of equal values between the 1st and last value
        return True # If so, it returns True
    else:
        return False # Else it returns False

print (function_c())

# -----------------------------------------------------------------
# -------------------------- Excercise 6 --------------------------
# -----------------------------------------------------------------

title_6 = '''-----------------------------------------------------------------
-------------------------- 6 th Excercise -----------------------
------------------------ Print only numbers ---------------------
-------------------------- divisible by 5 -----------------------
-----------------------------------------------------------------'''

excercise_6 = '''Given a lists of numbers print only values divisibles by 5'''

print(title_6)
print(excercise_6)

def function_d():
    def inp_covertor_d():
        while True:
            input_value = input('Please input a number\n')
            try:
                # If the value is zero or if the argument cannot be converted it will rise an exception
                # If the value float(arg) - int(float(arg)) == 0 it means that the input has no 
                # decimal value
                if float(input_value) - int(float(input_value)) != 0:
                    arg = float(input_value)
                else:
                    raise ValueError
            except:
                try:
                    # If the ValueError exception was raised or if there's no difference between the transformation of the value
                    # between a float or an interger it will try to convert it to a integer
                    arg = int(float(input_value))
                except:
                    arg = False
            # If the value is False it means that the input cannot be converted into a numerical value
            if arg != False:
                return arg
            elif input_value.lower() == 'no': # If the value is meant to cancel the process of appending it return a false value which will be passed to break the cicle
                return False
            print ('Input an useful value\n') # If the value is not a useful value it will print this message and the loop will restart
    def function_e():
        list_a = []
        print ('Input several values to a list\nWhen done type NO')
        while True:
            value_a = inp_covertor_d()
            if value_a == False:# If returned a False value the loop will break
                return list_a
            else:
                list_a.append (value_a) # In case is recieved a value the loop will continue to ask values to append 
    list = function_e() # Here the append function starts
    for item in list:
        if item%5 ==0: # Here is checked if the value is divisible by 5
            print (item) # If so the value is printed
    print ('Done')

function_d() # Here the overall function is executed

title_7 = '''-----------------------------------------------------------------
-------------------------- 7 th Excercise -----------------------
------------------ Count the times a sub string -----------------
------------------------ in within a string ---------------------
-----------------------------------------------------------------'''

excercise_7 = '''Count the ammount of times a strin is within another string'''

print(title_7)
print(excercise_7)

string_a = input ('Input a huge string\n')
string_b = input ('Input a substring\n')
count = string_a.count (string_b)
print (f'Count = {count}')

# -----------------------------------------------------------------
# -------------------------- Excercise 8 --------------------------
# -----------------------------------------------------------------

title_8 = '''-----------------------------------------------------------------
-------------------------- 8 th Excercise -----------------------
----------------------- Print a triangle form -------------------
--------------------------- 1 to a value ------------------------
-----------------------------------------------------------------'''

excercise_8 = '''Print a triangle of numbers starting from 1 with base n'''

print(title_8)
print(excercise_8)

def inp_covertor_c():
    while True:
        arg = input('Please input a number\n')
        try:
            arg = int(arg)
        except:
            # If the value cannot be converten into a either a floar or a interger the input will be 'False'
            arg = False
        # If the value is False it means that the input cannot be converted into a numerical value
        if arg <= 1:
            arg = False
            print ('Value cannot be <= 1')
        if arg != False:
            return arg
        print ('Input an useful value\n')

number_a = inp_covertor_c()
for item in range(1,number_a):
    level = str(item) + ' ' # The string to display is the string of the value with an space ' '
    print (level*item) # Every level will return the value displayed as many times as this value is

# -----------------------------------------------------------------
# -------------------------- Excercise 9 --------------------------
# -----------------------------------------------------------------

title_9 = '''-----------------------------------------------------------------
-------------------------- 9 th Excercise -----------------------
-------------------- Input a number and return ------------------
-------------------- True if it's a plaindrome ------------------
-----------------------------------------------------------------'''

excercise_9 = '''Recive a numeric value and return True if such value is considered as a palindrome'''

print(title_9)
print(excercise_9)

def function_d ():
    number_a =  inp_covertor_b()
    number_a = str(number_a)
    number_b = number_a [::-1]  # The '[::-1]' Instruction iverts a string
    if number_b == number_a:
        return (True)
    else:
        return (False)

print (function_d ())


# -----------------------------------------------------------------
# -------------------------- Excercise 10 -------------------------
# -----------------------------------------------------------------

title_10 = '''-----------------------------------------------------------------
-------------------------- 10 th Excercise ----------------------
------------------------ Input a a list then --------------------
---------------------- make two list with odd -------------------
----------------------- index or even numbers -------------------
-----------------------------------------------------------------'''

excercise_10 = '''Recieve several numerical values to build a list, then, from that list, create two lists, one with the even index values and another with the odd index values'''

print(title_10)
print(excercise_10)

def function_e():
    def inp_covertor_c():
        while True:
            input_value = input('Please input a number\n')
            try:
                # If the value is zero or if the argument cannot be converted it will rise an exception
                # If the value float(arg) - int(float(arg)) == 0 it means that the input has no 
                # decimal value
                if float(input_value) - int(float(input_value)) != 0:
                    arg = float(input_value)
                else:
                    raise ValueError
            except:
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
        list_a = []
        print ('Input several values to a list\nWhen done type NO')
        while True:
            value_a = inp_covertor_c()
            if value_a == None:
                return list_a
            elif value_a != None: # If returned a False value the loop will break
                list_a.append (value_a)
    list_a = function_d ()
    return list_a

def function_f():
    list_a = function_e()
    list_b = []
    list_c = []
    for index,value in enumerate(list_a):
        if index == 0 or index % 2 == 0:
            list_b.append(value)
        else:
            list_c.append(value)
    return list_b, list_c

list_b, list_c = function_f()
print (f'Even list {list_b}\nOdd list {list_c}')

# The exercise has been missunerstood and will be redo later

title_11 = '''-----------------------------------------------------------------
-------------------------- 11 th Excercise ----------------------
------------------------- Extract each digit --------------------
------------------------- from a integer in ---------------------
--------------------------- reverse order -----------------------
-----------------------------------------------------------------'''

excercise_11 = '''Recieve an integer and then extract every digit in the reverse order'''

print(title_11)
print(excercise_11)

number_a = inp_covertor_b()
for digit in str(number_a)[::-1]:
    print (int(digit))

title_12 = '''-----------------------------------------------------------------
-------------------------- 12 th Excercise ----------------------
--------------------------- Calculate TAX -----------------------
-----------------------------------------------------------------'''

excercise_11 = '''Recive an anual income then calculate the tax'''

print(title_11)
print(excercise_11)

inp_covertor_b

def inp_covertor_d():
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
        if arg != None and arg > 0 :
            return arg
        print ('Input an useful value\n')

print ('Input your yearly income')
number_a = inp_covertor_d()
if number_a <= 10000:
    tax = 0
elif number_a > 10000 and number_a <= 10000*2:
    tax = number_a*0.10
elif number_a > 10000*2:
    tax = number_a*0.20

print (f'Yearly income = {number_a}\nTax = {tax}')

title_13 = '''-----------------------------------------------------------------
-------------------------- 13 th Excercise ----------------------
---------------------- Print the mulplication -------------------
---------------------- table of x and n terms -------------------
-----------------------------------------------------------------'''

excercise_13 = '''Recive a value and the number of terms for a multiplication table'''

print(title_13)
print(excercise_13)

def inp_covertor_e():
    while True:
        arg = input('Please input a number\n')
        try:
            arg = int(arg)
        except:
            # If the value cannot be converten into a either a floar or a interger the input will be 'False'
            arg = None
        # If the value is False it means that the input cannot be converted into a numerical value
        if arg != None and arg > 0:
            return arg
        print ('Input an useful value\n')

print ('Introduce a number')
number_a = inp_covertor_d()
print ('Introduce n terms')
number_b = inp_covertor_e()
print ('Multiplication table')
for product in range(0,number_b):
    print (f'{number_a} x {product} = {product*number_a}')

title_14 = '''-----------------------------------------------------------------
-------------------------- 14 th Excercise ----------------------
------------------------ Print downward half --------------------
------------------------------ pyramid --------------------------
-----------------------------------------------------------------'''

excercise_14 = '''Print a downward pyramid pattern with asteisk'''

print(title_14)
print(excercise_14)

print ('Introduce n terms')
number_a = inp_covertor_e()
count = number_a
while count > 0:
    print ('*'*count)
    count -= 1

title_15 = '''-----------------------------------------------------------------
-------------------------- 15 th Excercise ----------------------
------------------------ Print base, exp and --------------------
---------------------------- power value ------------------------
-----------------------------------------------------------------'''

excercise_15 = '''Print a downward pyramid pattern with asteisk'''

print(title_15)
print(excercise_15)

print ('Introduce base')
number_a = inp_covertor_b()
print ('Introduce n power')
number_b = inp_covertor_e()

count = number_b
while count >= 0:
    value = number_a**count
    print (f'Base {number_a} power {count} = {value}')
    count -= 1
