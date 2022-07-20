title_34 = '''-----------------------------------------------------------------
-------------------------- 34 th Excercise ----------------------
------------------------- Create a function ---------------------
----------------------- Recieve name and age --------------------
---------------------------- Print result -----------------------
-----------------------------------------------------------------'''

excercise_34 = '''Create a function that can accept two arguments name,age and print their value'''

print(title_34)
print(excercise_34)

def name_and_age (name,age):
    print (f'Name = {name}\nAge = {age}')

name = 'Wilfred'
age = '28'
name_and_age (name,age)

title_35 = '''-----------------------------------------------------------------
-------------------------- 35 th Excercise ----------------------
------------------------- Create a function ---------------------
---------------------- Any number of arguments ------------------
------------------------- Print all values ----------------------
-----------------------------------------------------------------'''

excercise_35 = '''Create a function that can accept several arguments name and print every value'''

print(title_35)
print(excercise_35)

def several_arg(*arg):
    print (f'arg = ',arg)

several_arg(0,1,2,3,4,5,6,7,8,9)

title_36 = '''-----------------------------------------------------------------
------------------------ 36 th Excercise ------------------------
----------------------- Create a function -----------------------
---------------------- Recieve two values -----------------------
----------------------- Sum and substract ------------------------
------------------- return unce two operations -------------------
-----------------------------------------------------------------'''

excercise_36 = '''Create a function that recieves two values, sums and substracts them and then returns both results onvce'''

print(title_36)
print(excercise_36)

def calculation (val_a,val_b):
    sum = val_a+val_b
    sub = val_a-val_b
    return sum,sub

val_a = 1.2
val_b = 44

sum,sub = calculation (val_a,val_b)
print (f'sum,sub = {sum,sub}')

title_37 = '''-----------------------------------------------------------------
------------------------ 37 th Excercise ------------------------
----------------------- Create a function -----------------------
-------------------- Recieve name and salary --------------------
-------------- and print both or a default salary ---------------
------------------------ if value mising ------------------------
-----------------------------------------------------------------'''

excercise_37 = '''Create a function that recieves two values, name and salary, then, if salary missing, it's value is 9000 by default. Display both'''

print(title_37)
print(excercise_37)

def showEmployee(name,salary = 9000):
    print (f'Name: {name}\nSalary: {salary}')

name = 'Wilfred'
salary = 60000
# Salary passed
showEmployee(name,salary)
# Salary not passed
showEmployee(name)

title_38 = '''-----------------------------------------------------------------
------------------------ 38 th Excercise ------------------------
----------------------- Create a function -----------------------
--------------------- with nested function ----------------------
-----------------------------------------------------------------'''

excercise_38 = '''Create a function with a nested function where:
- Outer function will accept parametes a,b
- Create an inner function inside outer function that will calculate the addition of a and b
- At last The outer function will add 5 to the addutuib abd return it'''

print(title_38)
print(excercise_38)

def outer (a,b):
    sum_val = None
    def inner ():
        nonlocal sum_val
        sum_val = a+b
        print (sum_val)
    inner ()
    return sum_val + 5

a = 54
b = 6
outer (a,b)

title_39 = '''-----------------------------------------------------------------
------------------------ 39 th Excercise ------------------------
------------------ Create a recursive function ------------------
------------------ to sum values from 0 to 10 -------------------
-----------------------------------------------------------------'''

excercise_39 = '''Create a recursive function that sums values from 0 to 10'''

print(title_39)
print(excercise_39)

def recursive ():
    value = 0
    count = 0
    def nested_recursive ():
        nonlocal value
        nonlocal count 
        if count < 10:
            count += 1
            value += count
            nested_recursive ()
        else:
            return value
    nested_recursive ()
    return value

recursive ()

title_40 = '''-----------------------------------------------------------------
------------------------ 40 th Excercise ------------------------
------------------------ Create function ------------------------
----------- name a variable, store the function and -------------
--------------- then call it by the new varaible ----------------
-----------------------------------------------------------------'''

excercise_40 = '''Create function store it in a new variable name and then call the function by the new name'''

print(title_40)
print(excercise_40)

def basic (name = 'Wise', age = '999'):
    print (f'This is a {name}\nof {age} years old')

unbasic = basic
print ('Basic function')
basic()
print ('Un-basic function')
unbasic ('Wilfred',28) # Function stored in a new variable

title_41 = '''-----------------------------------------------------------------
------------------------ 41 th Excercise ------------------------
------------------------ Create function ------------------------
----------- that generates a Python list of all even ------------
-------------- numbers from 4 to 30 and return it ---------------
-----------------------------------------------------------------'''

excercise_41 = '''Create function that generates a Python list of all even numbers from 4 to 30 and return it'''

print(title_41)
print(excercise_41)

def even_list ():
    list_a = []
    for item in range (4,31):
        if item % 2 == 0:
            list_a.append (item)
    return list_a

list_a = even_list ()
print (f'List_a = {list_a}')

title_42 = '''-----------------------------------------------------------------
------------------------ 42 th Excercise ------------------------
------------------------ Create function ------------------------
---------------- that return the largest item of ----------------
------------------------ a bigger list -------------------------
-----------------------------------------------------------------'''

excercise_42 = '''Create function that returns the lasrgest item of a given list'''

print(title_42)
print(excercise_42)

def largest_item (list):
    value = max(list)
    return value

list_a = [123,345,456,567,678,789,56,345,2341,23345,567,67,9,99999999999999999]
value = largest_item (list)
print (f'Largest value = {value}')