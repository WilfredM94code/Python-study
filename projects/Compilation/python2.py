title_16 = '''-----------------------------------------------------------------
-------------------------- 16 th Excercise ----------------------
------------------------- Accept two values ---------------------
--------------------------- print product -----------------------
-----------------------------------------------------------------'''

excercise_16 = '''Print a downward pyramid pattern with asteisk'''

print(title_16)
print(excercise_16)

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

print ('Introduce a value')
number_a = inp_covertor_a()
print ('Introduce another value')
number_b = inp_covertor_a()
print (f'Product {number_a*number_b}')

title_17 = '''-----------------------------------------------------------------
-------------------------- 17 th Excercise ----------------------
------------------------- Display a name using ------------------
-------------------------- print formatting ---------------------
-----------------------------------------------------------------'''

excercise_17 = '''Input a 'name' string and print 'My name is xx' '''

print(title_17)
print(excercise_17)

def inp_covertor_b():
    while True:
        arg = input('Please input your name\n')
        try:
            arg = int(arg)
            arg = None
        except:
            pass
        if arg != None:
            return arg
        print ('Input an actual name\n')

name = inp_covertor_b()
print (f'My name is {name}')

title_18 = '''-----------------------------------------------------------------
-------------------------- 18 th Excercise ----------------------
------------------------ Display two decimal --------------------
------------------------- places using print --------------------
-----------------------------------------------------------------'''

excercise_18 = '''Display a float number with two decimal places using print '''

print(title_18)
print(excercise_18)

number_a = inp_covertor_a()
number_a_str = str(number_a)
number_a_str_point = number_a_str.find('.')
if number_a_str_point != -1:
    try:
        print (number_a_str [number_a_str_point + 2 : ])
    except:
        print ('No second decimal value\nTherefore = ',0)
else:
    print (0)



title_19 = '''-----------------------------------------------------------------
-------------------------- 19 th Excercise ----------------------
-------------------------- Customize a list ---------------------
-----------------------------------------------------------------'''

excercise_19 = '''Accept the number of items of alist and every value'''

print(title_19)
print(excercise_19)

def inp_covertor_c():
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


def list_creator():
    n_items = inp_covertor_c()
    count = 0
    list_a = []
    while count <= n_items:
        print (f'Items {count}/{n_items}')
        item = inp_covertor_a()
        list_a.append (item)
        count += 1
    return list_a

list_a = list_creator()
print (f'list_a = {list_a}')