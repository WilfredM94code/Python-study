title_90 = '''-----------------------------------------------------------------
------------------------ 90 th Excercise ------------------------
------------------------ Reverse a tuple ------------------------
------------------------------------------------------------------'''

excercise_90 = '''Reverse the following tuple'''

print(title_90)
print(excercise_90)

tuple_a = (0,1,2,3,4,5,6,7,8,9)
tuple_a = tuple_a[::-1]
print (f'Reversed tuple {tuple_a}')

title_91 = '''-----------------------------------------------------------------
------------------------ 91 th Excercise ------------------------
-------------------- Access value from tuple --------------------
------------------------------------------------------------------'''

excercise_91 = '''Access 20 value from the following tuple'''

print(title_91)
print(excercise_91)

tuple_a = (0,1,20,3,4,5,6,7,8,9)
value = tuple_a[2]
print (f'Value 20 from tuple {value}')

title_92 = '''-----------------------------------------------------------------
------------------------ 92 th Excercise ------------------------
---------------- Create tuple with single value -----------------
------------------------------------------------------------------'''

excercise_92 = '''Create a tuple with single item 50'''

print(title_92)
print(excercise_92)

tuple_a = tuple(50)
print (f'Created tuple {tuple_a}')

title_93 = '''-----------------------------------------------------------------
------------------------ 93 th Excercise ------------------------
----------------- Unpack a tuple in 4 variables -----------------
------------------------------------------------------------------'''

excercise_93 = '''Unpack the following tuple into 4 variables'''

print(title_93)
print(excercise_93)

tuple_a = (0,1,2,3,4,5,6,7,8,9)
var_a, *var_b, var_c, var_d = tuple_a
print (f'var_a, *var_b, var_c, var_d = {var_a, var_b, var_c, var_d}')

title_94 = '''-----------------------------------------------------------------
------------------------ 94 th Excercise ------------------------
----------------- Swap the following two tuples -----------------
------------------------------------------------------------------'''

excercise_94 = '''Swap the following two tuples'''

print(title_94)
print(excercise_94)

tuple_a = (0,1,2,3,4)
tuple_b = (5,6,7,8,9)
print (f'tuple_a {tuple_a} \ntuple_b {tuple_b}')
tuple_a,tuple_b = tuple_b,tuple_a
print (f'Swaped\ntuple_a {tuple_a} \ntuple_b {tuple_b}')

title_95 = '''-----------------------------------------------------------------
------------------------ 95 th Excercise ------------------------
-------------- Copy elements from tuple in another --------------
----------------------------- tuple -----------------------------
------------------------------------------------------------------'''

excercise_95 = '''Copy element 44 and 55 from the following tuple into a new tuple'''

print(title_95)
print(excercise_95)

tuple_a = (0,1,2,3,44,55,6,7,8,9)
tuple_b = tuple_a[4],tuple_a[5]
print (f'Created tuple {tuple_b}')

title_96 = '''-----------------------------------------------------------------
------------------------ 96 th Excercise ------------------------
-------------------- Change value from a list -------------------
------------------------------------------------------------------'''

excercise_96 = '''Change the value of the first item of the list to 222'''

print(title_96)
print(excercise_96)

tuple_a = (0,1,[21,31],4,5,6)
tuple_a[2][0] = 222
print (f'Updated tuple {tuple_a}')

title_97 = '''-----------------------------------------------------------------
------------------------ 97 th Excercise ------------------------
------------------- Count ocurrence of a value ------------------
------------------------------------------------------------------'''

excercise_97 = '''Count the ocurrence of the value 50'''

print(title_97)
print(excercise_97)

tuple_a = (0,50,2,3,4,50,6,50,8,9)
counter = tuple_a.count(50)
print (f'Counter {counter}')