title_43 = '''-----------------------------------------------------------------
------------------------ 43 th Excercise ------------------------
------------------- Arrange string characters -------------------
----------------- such that lowercase come first ----------------
-----------------------------------------------------------------'''

excercise_43 = '''Arrange string characters such that lowercase come first'''

print(title_43)
print(excercise_43)

string = input('Introduce a string\n')
string = 'AbCdEfGhIjKlMnOpQrStUvWxYz'
string = list(string)
string.sort()
string = string [::-1]
string = ''.join(string)
print (f'Sorted string {string}')

title_44 = '''-----------------------------------------------------------------
------------------------ 44 th Excercise ------------------------
----------------- Count the number of lowercase -----------------
----------------- uppercase, numbers and symbols ----------------
--------------------------- in a string -------------------------
-----------------------------------------------------------------'''

excercise_44 = ''' Count the number of lowercase uppercase, numbers and symbols in a string'''

print(title_44)
print(excercise_44)

string = input('Introduce a string\n')
lower_count = 0
upper_count = 0
number_count = 0
symbol_count = 0
for char in string:
    if char.islower():
        lower_count += 1
    elif char.isupper():
        upper_count += 1
    elif type(char) is int:
        number_count += 1
    else:
        symbol_count += 1

print (f'Lower {lower_count}\nUpper {upper_count}\nNumber {number_count}\nSymbol {symbol_count}')

title_45 = '''-----------------------------------------------------------------
------------------------ 45 th Excercise ------------------------
----------------- Find acurrances of a substring ----------------
------------------------- within a string -----------------------
------------------------------------------------------------------'''

excercise_45 = '''Find all occurances of 'is in a given string ignoring the case'''

print(title_45)
print(excercise_45)

string = input('Introduce a string\n')
occurances = string.lower().count('is')

title_46 = '''-----------------------------------------------------------------
------------------------ 46 th Excercise ------------------------
----------------- Count character occurances in -----------------
---------------------------- a string ---------------------------
------------------------------------------------------------------'''

excercise_46 = '''Find all occurances of every character within a string'''

print(title_46)
print(excercise_46)

string = input('Introduce a string\n')
empty_str = ''
dictionary_a = {}
for char in string:
    if char in empty_str:
        dictionary_a[char] += 1
    else:
        empty_str += char
        dictionary_a[char] = 1

print (f'Characters and values {dictionary_a}')

title_47 = '''-----------------------------------------------------------------
------------------------ 47 th Excercise ------------------------
-------------------- Reverse a given string ---------------------
------------------------------------------------------------------'''

excercise_47 = '''Reverse a given string'''

print(title_47)
print(excercise_47)

string = input('Introduce a string\n')
print (f'Normal string: {string}')
string = string[::-1]
print (f'Reversed string: {string}')

title_48 = '''-----------------------------------------------------------------
------------------------ 48 th Excercise ------------------------
------------------- Find the last position of -------------------
----------------- substring 'Kelly' in a given ------------------
----------------------------- string ----------------------------
------------------------------------------------------------------'''

excercise_48 = '''Find the last position of substring 'Kelly' in a given string'''

print(title_48)
print(excercise_48)

string = ''' I wanna talk to you
The last time we talked, Mr. Smith, you reduced me to tears
I promise you it won't happen again
Do I attract you? Do I repulse you with my queasy smile?
Am I too dirty, am I too flirty? Do I like what you like?
I could be wholesome, I could be loathsome, I guess I'm a little bit shy
Why don't you like me, why don't you like me, without making me try?
I tried to be like Grace Kelly, mmh
But all her looks were too sad, aah
So I tried a little Freddie, mmh
I've gone identity mad!
I could be brown, I could be blue, I could be violet sky
I could be hurtful, I could be purple, I could be anything you like
Gotta be green, gotta be mean, gotta be everything more
Why don't you like me, why don't you like me?
Why don't you walk out the door?
Getting angry doesn't solve anything
How can I help it, how can I help it? How can I help what you think?
Hello my baby, hello my baby, putting my life on my brink
Why don't you like me, why don't you like me? Why don't you like yourself?
Should I bend over, should I look older, just to be put on your shelf?
I tried to be like Grace Kelly, mmh
But all her looks were too sad, aah
So I tried a little Freddie, mmh
I've gone identity mad!
I could be brown, I could be blue, I could be violet sky
I could be hurtful, I could be purple, I could be anything you like
Gotta be green, gotta be mean, gotta be everything more
Why don't you like me, why don't you like me?
Walk out the door!
Say what you want to satisfy yourself, hey
But you only want what everybody else says you should want
You want
I could be brown, I could be blue, I could be violet sky
I could be hurtful, I could be purple, I could be anything you like
Gotta be green, gotta be mean, gotta be everything more
Why don't you like me, why don't you like me?
Walk out the door!
I could be brown, I could be blue, I could be violet sky
I could be hurtful, I could be purple, I could be anything you like
Gotta be green, gotta be mean, gotta be everything more
Why don't you like me, why don't you like me?
Walk out the door!
Uuh, ah
Humphry, we're leaving
Ca-ching!'''
last_occur = string.rfind('Kelly')

title_49 = '''-----------------------------------------------------------------
------------------------ 49 th Excercise ------------------------
------------------- Repla -------------------
----------------- substring 'Kelly' in a given ------------------
----------------------------- string ----------------------------
------------------------------------------------------------------'''

excercise_49 = '''Find the last position of substring 'Kelly' in a given string'''

print(title_49)
print(excercise_49)