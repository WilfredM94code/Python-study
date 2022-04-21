title_61 = '''-----------------------------------------------------------------
------------------------ 61 th Excercise ------------------------
------------------------- Reverse a list ------------------------
------------------------------------------------------------------'''

excercise_61 = '''Remove the given list'''

print(title_61)
print(excercise_61)

list_a = [0,1,2,3,4,5,6,7,8,9]
list_a = list_a [::-1]
print (f'list_a = {list_a}')

title_62 = '''-----------------------------------------------------------------
------------------------ 62 th Excercise ------------------------
---------------------- Concatenate two list ---------------------
------------------------------------------------------------------'''

excercise_62 = '''Concatenate two lists index-wise'''

print(title_62)
print(excercise_62)

list_a = [0,1,2,3,4]
list_b = [5,6,7,8,9]
list_c = list_a + list_b
print (f'List {list_c}')

# The requested approach

list_c = [item_a + item_b for item_a,item_b in zip(list_a,)]
print (f'List {list_c}')

title_63 = '''-----------------------------------------------------------------
------------------------ 63 th Excercise ------------------------
--------------------- Turn values on a list ---------------------
------------------------ into it's square -----------------------
------------------------------------------------------------------'''

excercise_63 = '''Given a list, turn every value into it's square'''

print(title_63)
print(excercise_63)

list_a = [0,1,2,3,4,5,6,7,8,9]
list_a = [item**2 for item in list_a]
print (f'Squared list {list_a}')

title_64 = '''-----------------------------------------------------------------
------------------------ 64 th Excercise ------------------------
--------------------- Concatenate two lists ---------------------
------------------------------------------------------------------'''

excercise_64 = '''Concatenate two lists in a particular order'''

print(title_64)
print(excercise_64)

list_a = ['Hello','Hi']
list_b = ['Dear','Sir']

# ['Hello Dear','Hi Dear','Hello Sir','Hi Sir']

list_c = [item_b + ' ' + item_a for item_a in list_b for item_b in list_a]
print (f'Squared list {list_c}')

title_65 = '''-----------------------------------------------------------------
------------------------ 65 th Excercise ------------------------
----------------------- Iterate two lists -----------------------
------------------------------------------------------------------'''

excercise_65 = '''Iterate two lists simultaneously, one in normal order and the other reversed'''

print(title_65)
print(excercise_65)

list_a = [0,1,2,3,4]
list_b = [5,6,7,8,9]

for item_a,item_b in zip(list_a,list_b[::-1]):
    print (f'Item a {item_a} Item b {item_b}')

title_66 = '''-----------------------------------------------------------------
------------------------ 66 th Excercise ------------------------
------------------------- Clean a list --------------------------
------------------------------------------------------------------'''

excercise_66 = '''Remove empty string from a list of strings'''

print(title_66)
print(excercise_66)

list_a = ['','Time','','Pasees','','By', None]
list_a = [item for item in filter(None,list_a)]
print (f'Clean list {list_a}')

title_67 = '''-----------------------------------------------------------------
------------------------ 67 th Excercise ------------------------
----------------------- Add an item lists -----------------------
--------------------------- to a list ---------------------------
------------------------------------------------------------------'''

excercise_67 = '''Add item 7000 after 6000 in the following list'''

print(title_67)
print(excercise_67)

list_a = [10,20,[300,400,[5000,6000],500],30,40]
list_a[2][2].append(7000)
print (f'list_a = {list_a}')

title_68 = '''-----------------------------------------------------------------
------------------------ 68 th Excercise ------------------------
-------------------------- Add sub list -------------------------
--------------------------- to a list ---------------------------
------------------------------------------------------------------'''

excercise_68 = '''Given a nested list extend the sub list ['h','i','j'] in suchway it will look like the following list'''

print(title_68)
print(excercise_68)

list_a = ['a','b',['c',['d','e',['f','g'],'k'],'l'],'m','n']

#  ['a','b',['c'['d','e',['f','g','h','i','j'],'k'],'l'],'m','n']

list_a[2][1][2] = list_a[2][1][2] + ['h','i','j']
print (f'list_a = {list_a}')

title_69 = '''-----------------------------------------------------------------
------------------------ 69 th Excercise ------------------------
--------------------- Find and change value ---------------------
-------------- SEARCH AND DESTRO - Oh, just change --------------
------------------------------------------------------------------'''

excercise_69 = '''Find value 20 in the list, and if it is present, replace it with 200. Only update the 1st occurence of the value'''

print(title_69)
print(excercise_69)

list_a = [0,1,20,3,4,5,6,7,20,9]
if 20 in list_a:
    list_a[list_a.index(20)]= 200

print (f'list_a = {list_a}')

title_70 = '''-----------------------------------------------------------------
------------------------ 70 th Excercise ------------------------
----------------------- SEARCH AND DESTROY ---------------------
------------------------------------------------------------------'''

excercise_70 = '''Remove all occurences of 20 from the list'''

print(title_70)
print(excercise_70)

list_a = [0,1,20,3,20,20,20]
list_a = [item for item in filter(20,list_a)]