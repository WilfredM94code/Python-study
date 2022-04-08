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
                arg = False
        # If the value is False it means that the input cannot be converted into a numerical value
        if arg != False:
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
            # If the ValueError exception was raised or if there's no difference between the transformation of the value
            # between a float or an interger it will try to convert it to a integer
            arg = int(arg)
        except:
            # If the value cannot be converten into a either a floar or a interger the input will be 'False'
            arg = False
        # If the value is False it means that the input cannot be converted into a numerical value
        if arg != False:
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

title_4 = '''-----------------------------------------------------------------
-------------------------- 5 th Excercise -----------------------
---------------------- Check of repeated value ------------------
---------------------------- From a List ------------------------
-----------------------------------------------------------------'''

excercise_4 = '''Given two lists of numbers return true if the first and last value is the same'''

print(title_4)
print(excercise_4)

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
                    arg = False
            # If the value is False it means that the input cannot be converted into a numerical value
            if arg != False:
                return arg
            elif input_value.lower() == 'no':
                return False
            print ('Input an useful value\n')
    def function_d():
        list_a = []
        print ('Input several values to a list\nWhen done type NO')
        while True:
            value_a = inp_covertor_c()
            if value_a == False:
                return list_a
            else:
                list_a.append (value_a)
    list = function_d()
    if list [0] == list [-1]:
        return True
    else:
        return False