title_71 = '''-----------------------------------------------------------------
------------------------ 71 th Excercise ------------------------
------------------- Convert list to dictionary ------------------
------------------------------------------------------------------'''

excercise_71 = '''Convert the below list to dictionary'''

print(title_71)
print(excercise_71)

list_a = []
dict_a = dict.fromkeys(list_a,None)

title_72 = '''-----------------------------------------------------------------
------------------------ 72 th Excercise ------------------------
------------------- Merge two dictionaries ------------------
------------------------------------------------------------------'''

excercise_72 = '''Merge two Python dictionaries into one'''

print(title_72)
print(excercise_72)

dict_a = {
    'a':1,
    'b':2,
    'c':3,
    'd':4
}

dict_b = {
    'e':5,
    'f':6,
    'g':7,
    'h':8
}
try:
    dict_c = dict_a | dict_b
    print (f'Merged dictionaries {dict_c}')
except:
    pass

# or 

try:
    dict_c = {**dict_a, **dict_b}
    print (f'Merged dictionaries {dict_c}')
except:
    pass

title_73 = '''-----------------------------------------------------------------
------------------------ 73 th Excercise ------------------------
-------------------- Access the value of a key ------------------
------------------------------------------------------------------'''

excercise_73 = '''Access the value of the key 'history' from the below dictionary'''

print(title_73)
print(excercise_73)

dict_a = {
    'cactus': True,
    'history': False
}

print (f'Value {dict_a["history"]}')

title_74 = '''-----------------------------------------------------------------
------------------------ 74 th Excercise ------------------------
----------------- Initialize a Dict with default ----------------
------------------------------ value ---------------------------
------------------------------------------------------------------'''

excercise_74 = '''Initialize a dictionary with default value'''

print(title_74)
print(excercise_74)

list_a = ['Wilfred','Linus','Satoshi']
dict_a = {
    'position':'Python developer',
    'salary':60000,
}

dict_b = dict.fromkeys(list_a,dict_a)
print (f'Default dict {dict_b}')

title_75 = '''-----------------------------------------------------------------
------------------------ 75 th Excercise ------------------------
------------------ Create a dictionary from the -----------------
-------------------- keys of another dictionary -----------------
------------------------------------------------------------------'''

excercise_75 = '''Create a new dictionary by extracting the following keys from below dictionary'''

print(title_75)
print(excercise_75)

dict_a = {
    'a':1,
    'b':2,
    'c':3,
    'd':4
}

list_a = ['a','b']

dict_b = {key: dict_a[key] for key in list_a}
print (f'New dictionary {dict_b}')

title_76 = '''-----------------------------------------------------------------
------------------------ 76 th Excercise ------------------------
--------------- Delete set of keys from dictionary --------------
------------------------------------------------------------------'''

excercise_76 = '''Delete a set of keys from a dictionaey'''

print(title_76)
print(excercise_76)

dict_a = {
    'a':1,
    'b':2,
    'c':3,
    'd':4
}

list_a = ['a','b']

dict_a = {key: dict_a[key] for key in dict_a.keys() - list_a}
print (f'New dictionary {dict_a}')

title_77 = '''-----------------------------------------------------------------
------------------------ 77 th Excercise ------------------------
-------------------- Check if value exists ----------------------
------------------------------------------------------------------'''

excercise_77 = '''Check if a value 200 exists in a dictionary'''

print(title_77)
print(excercise_77)

dict_a = {
    'a':1,
    'b':2,
    'c':3,
    'd':200,
}

if 200 in dict_a.values():
    print ('Value exists')

title_78 = '''-----------------------------------------------------------------
------------------------ 78 th Excercise ------------------------
--------------------- Rename key from dict ----------------------
------------------------------------------------------------------'''

excercise_78 = '''Rename a key city to location in the following dictionary'''

print(title_78)
print(excercise_78)

dict_a = {
    'a':1,
    'b':2,
    'c':3,
    'city':'Naiwatown-City',
}

dict_a['location'] = dict_a.pop('city')
print (f'Updated dictionary {dict_a}')

title_79 = '''-----------------------------------------------------------------
------------------------ 79 th Excercise ------------------------
---------------------- Get key from value -----------------------
------------------------------------------------------------------'''

excercise_79 = '''Get key of a minimun value from the following dictionary'''

print(title_79)
print(excercise_79)

dict_a = {
    'a':1,
    'b':2,
    'c':3,
    'd':4
}

key_a = min(dict_a,key = dict_a.get)
print (f'Updated dictionary {key_a}')

title_80 = '''-----------------------------------------------------------------
------------------------ 80 th Excercise ------------------------
-------------------- Change value from dict ---------------------
------------------------------------------------------------------'''

excercise_80 = '''Change Wilfred's salary from the following dictionar'''

print(title_80)
print(excercise_80)

list_a = ['Wilfred','Linus','Satoshi']
dict_a = {
    'position':'Python developer',
    'salary':60000,
}
dict_b = dict.fromkeys(list_a,dict_a)
dict_b['Wilfred']['salary'] = 90000