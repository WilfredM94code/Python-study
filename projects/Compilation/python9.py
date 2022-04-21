title_81 = '''-----------------------------------------------------------------
------------------------ 81 th Excercise ------------------------
-------------------- Add elements to a set ----------------------
------------------------------------------------------------------'''

excercise_81 = '''Add a list of elements to a set'''

print(title_81)
print(excercise_81)

set_a = {0,1,2,3}
list_a = [4,5,6,7,8,9]
set_a = set_a + set(list_a)
print (f'Updated set {set_a}')

title_82 = '''-----------------------------------------------------------------
------------------------ 82 th Excercise ------------------------
-------------------- Create a set from two ----------------------
----------------------------- sets ------------------------------
------------------------------------------------------------------'''

excercise_82 = '''Return a new set of identical items from two sets given'''

print(title_82)
print(excercise_82)

set_a = {2,3,4,5,6}
set_b = {4,5,6,7,8}
set_c = set_a.intersection(set_b)
print (f'Updated set {set_c}')

title_83 = '''-----------------------------------------------------------------
------------------------ 83 th Excercise ------------------------
-------------------- Create a set from two ----------------------
------------------------- sets - remix --------------------------
------------------------------------------------------------------'''

excercise_83 = '''Return a new set with all items from two sets removing duplicates'''

print(title_83)
print(excercise_83)

set_a = {2,3,4,5,6}
set_b = {4,5,6,7,8}
set_c = set_a.union(set_b)
print (f'Updated set {set_c}')

title_84 = '''-----------------------------------------------------------------
------------------------ 84 th Excercise ------------------------
-------------------- Create a set from two ----------------------
------------------------- sets - remix 2 --------------------------
------------------------------------------------------------------'''

excercise_84 = '''Given two sets, update the first set with items that exists only in the first set and not in the second set'''

print(title_84)
print(excercise_84)

set_a = {2,3,4,5,6}
set_b = {4,5,6,7,8}
set_a.difference(set_b)
print (f'Updated set {set_a}')

title_85 = '''-----------------------------------------------------------------
------------------------ 85 th Excercise ------------------------
------------------- Remove seveal items from --------------------
------------------------------ set ------------------------------
------------------------------------------------------------------'''

excercise_85 = '''Remove items 10,20,30 from the following set at once'''

print(title_85)
print(excercise_85)

set_a = {10,20,30,40,50,60}
set_a.symmetric_difference_update({10,20,30})
print (f'Updated set {set_a}')

title_86 = '''-----------------------------------------------------------------
------------------------ 86 th Excercise ------------------------
----------------- Create set of unique values -------------------
------------------------- from two sets -------------------------
------------------------------------------------------------------'''

excercise_86 = '''Return all rhe unique elements in set A&B'''

print(title_86)
print(excercise_86)

set_a = {2,3,4,5,6}
set_b = {4,5,6,7,8}
print (f'Return {set_a.symmetric_difference(set_b)}')

title_87 = '''-----------------------------------------------------------------
------------------------ 87 th Excercise ------------------------
---------------- Check if two sets have common ------------------
---------------------------- elements ---------------------------
------------------------------------------------------------------'''

excercise_87 = '''Check if two sets have common elements. If so display common elements'''

print(title_87)
print(excercise_87)

set_a = {2,3,4,5,6}
set_b = {4,5,6,7,8}
set_c = set_a.intersection(set_b)
if set_c != set():
    print (f'Return {set_c}')

title_88 = '''-----------------------------------------------------------------
------------------------ 88 th Excercise ------------------------
----------------- Update set a set with uncommon ----------------
---------------------------- elements ---------------------------
------------------------------------------------------------------'''

excercise_88 = '''Update set 1 by adding items from set 2, except common items'''

print(title_88)
print(excercise_88)

set_a = {2,3,4,5,6}
set_b = {4,5,6,7,8}
set_a.symmetric_difference_update(set_b)
print (f'Updated set {set_a}')

title_89 = '''-----------------------------------------------------------------
------------------------ 89 th Excercise ------------------------
----------------- Remove uncommon items from set ----------------
------------------------------------------------------------------'''

excercise_89 = '''Remove items from set 1 that are not common in both set 1 and set 2'''

print(title_89)
print(excercise_89)

set_a = {2,3,4,5,6}
set_b = {4,5,6,7,8}
set_a = set_a - set_b
print (f'Updated set {set_a}')