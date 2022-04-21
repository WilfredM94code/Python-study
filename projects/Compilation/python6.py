title_52 = '''-----------------------------------------------------------------
------------------------ 52 th Excercise ------------------------
------------------ Create a list from two lists -----------------
------------------------------------------------------------------'''

excercise_52 = '''Create a list from two lists by picking add-index elements from the first list and even-index elements from the second'''

print(title_52)
print(excercise_52)

list_a = [0,1,2,3,4,5,6,7,8,9]
list_b = ['a','b','c','d','e','f','g','h','i','j']
list_c = [items[0] if index%2 == 0 else items[1] for index,items in enumerate(zip(list_a,list_b))]

print (f'New list = {list_c}')

title_53 = '''-----------------------------------------------------------------
------------------------ 53 th Excercise ------------------------
----------------- Change item position from list ----------------
------------------------------------------------------------------'''

excercise_53 = '''Given a list, remopve the elements at the index 4 and add it to the 2nd position and at the end of the list'''

print(title_53)
print(excercise_53)

list_a = [0,1,2,3,4,5,6,7,8,9]
list_a.pop(4)
list_a [2] = list_a[4]
list_a [-1] = list_a[4]
print (f'Modified list = {list_a}')

title_54 = '''-----------------------------------------------------------------
------------------------ 54 th Excercise ------------------------
--------------- Count the occurence of every item ---------------
--------------------------- from a list -------------------------
------------------------------------------------------------------'''

excercise_54 = '''Given a list, ount the occurence of every item an store the result on a dictionary
'''

print(title_54)
print(excercise_54)

list_a = ['a','b','c','d','e','f','g','h','i','j','a','b','c','d','h','i','j','a','b']
dict_a = {}
for item in list_a:
    if item not in dict_a:
        dict_a [item] = list_a.count (item)

for counter in dict_a.items():
    print (f'Key {counter[0]} Count {counter[1]}')

title_55 = '''-----------------------------------------------------------------
------------------------ 55 th Excercise ------------------------
------------------ Create a set from two lists ------------------
------------------------------------------------------------------'''

excercise_55 = '''Given two lists of equal size create a set such that it shows the element for both lists in the pair'''

print(title_55)
print(excercise_55)

list_a = [0,1,2,3,4,5,6,7,8,9]
list_b = ['a','b','c','d','e','f','g','h','i','j']
set_a = set(list_b).union(set(list_a))

title_56 = '''-----------------------------------------------------------------
------------------------ 56 th Excercise ------------------------
-------------- Erase the intercepted values of two --------------
------------------------------ sets -----------------------------
------------------------------------------------------------------'''

excercise_56 = '''Given two sets erase the interection from the first set'''

print(title_56)
print(excercise_56)

set_a = {0,1,2,3,4,5}
set_b = {4,5,6,7,8,9}
set_a = set_a - (set_a & set_b)
print (f'Set a {set_a}')

title_57 = '''-----------------------------------------------------------------
------------------------ 57 th Excercise ------------------------
-------------- Check for sub or super set relation --------------
------------------------------------------------------------------'''

excercise_57 = '''Given two sets check if a set is a sub set or a super set of another set'''

print(title_57)
print(excercise_57)

set_a = {0,1,2,3,4,5}
set_b = {1,3,4}

if set_a.issubset(set_b):
    set_a.clear()
    print ('Subset found - 1st is subset')
elif set_b.issubset(set_a):
    set_b.clear()
    print ('Subset found - 2nd is subset')

title_58 = '''-----------------------------------------------------------------
------------------------ 58 th Excercise ------------------------
------------------- Cross list and dictionary -------------------
------------------------------------------------------------------'''

excercise_58 = '''Check if a value in a list is a key of a dictionary. If is not erase suck value from the list'''

print(title_58)
print(excercise_58)

list_a = ['a','b','c','d','e','f']
dict_a = {
    'a': 0,
    'b': 1,
    'c': 2,
}

counter = 0
while True:
    try:
        if dict_a.get(list_a[counter]) is None:
            list_a.remove(list_a[counter])
        else:
            counter += 1
    except IndexError:
        break

print (f'List {list_a}')

title_59 = '''-----------------------------------------------------------------
------------------------ 59 th Excercise ------------------------
---------------- Create a list from a dictionary ----------------
------------------------------------------------------------------'''

excercise_59 = '''Given a dictionary get all the values from the dictionary and add them to a list but dont add duplicates'''

print(title_59)
print(excercise_59)

dict_a = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 0,
    'f': 1,
    'g': 2,
    'h': 3,
}
list_a = []
for key,value in dict_a.items():
    if value not in list_a:
        list_a.append(value)

print (f'List {list_a}')

title_60 = '''-----------------------------------------------------------------
------------------------ 60 th Excercise ------------------------
--------------- Create a tuple without duplicated ---------------
----------------------------- values ----------------------------
------------------------------------------------------------------'''

excercise_60 = '''Remove dulicate from a list and create a tuple and find the minimun and maximun number'''

print(title_60)
print(excercise_60)

list_a = ['a','b','c','d','e','f','g','h','i','j','a','b','c','d','h','i','j','a','b']
tuple_a = tuple(set(list_a))

print (f'Tuple {tuple_a}')