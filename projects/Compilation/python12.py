title_108 = '''-----------------------------------------------------------------
------------------------- 108 th Excercise -----------------------
------------------ Create an class with several ------------------
--------------------------- attributes ---------------------------
------------------------------------------------------------------'''

excercise_108 = '''Create a Vehicle class with max_speed and mileage instance attributes'''

print(title_108)
print(excercise_108)

class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

object_a = Vehicle(max_speed = 100,mileage = 10000)
print (f'Object attributes\nobject_a.max_speed = {object_a.max_speed}\nobject_a.mileage = {object_a.mileage}')

title_109 = '''-----------------------------------------------------------------
------------------------- 109 th Excercise -----------------------
---------------- Create an class without variables ---------------
--------------------------- or methods ---------------------------
------------------------------------------------------------------'''

excercise_109 = '''Create an class without variables or methods'''

print(title_109)
print(excercise_109)

class Vehicle:
    pass

title_110 = '''-----------------------------------------------------------------
------------------------- 110 th Excercise -----------------------
---------------------- Create a child class ----------------------
------------------------------------------------------------------'''

excercise_110 = '''Create a child class Bus that will inherit all of the variables and methods from the Vehicle class'''

print(title_110)
print(excercise_110)

class Vehicle:
    def __init__(self,max_speed,mileage,name):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name

class Bus (Vehicle):
    pass

object_a = Bus (100,1000,'Encava el miooo')

print (f'Object attributes\nobject_a.max_speed = {object_a.max_speed}\nobject_a.mileage = {object_a.mileage}\nobject_a.name = {object_a.name}')

title_111 = '''-----------------------------------------------------------------
------------------------- 111 th Excercise -----------------------
------------------------ Class inheritance -----------------------
------------------------------------------------------------------'''

excercise_111 = '''Class inheritance given: create a bus class that inherits from the Vehicle class. 
Give the capacity argument of Bus.seating_cpacity a default value of 50. Use the following code for 
your parent Vehicle class. Method overriding is meant to be used'''

print(title_111)
print(excercise_111)

class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

class Bus (Vehicle):
    def __init__(self,max_speed,mileage,seating_cpacity = 50):
        super().__init__(max_speed,mileage)
        self.seating_cpacity = seating_cpacity

object_a = Bus(seating_cpacity = 51,max_speed = 150 ,mileage = 450)
print (f'Object attributes\nobject_a.max_speed = {object_a.max_speed}\nobject_a.mileage = {object_a.mileage}\nobject_a.seating_cpacity = {object_a.seating_cpacity}')

# Another approach

class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

class Bus (Vehicle):
    def __init__(self,seating_cpacity = 50,**kwargs):
        super().__init__(**kwargs)
        self.seating_cpacity = seating_cpacity

object_a = Bus(seating_cpacity = 51,max_speed = 150 ,mileage = 450)
print (f'Object attributes\nobject_a.max_speed = {object_a.max_speed}\nobject_a.mileage = {object_a.mileage}\nobject_a.seating_cpacity = {object_a.seating_cpacity}')

title_112 = '''-----------------------------------------------------------------
------------------------- 112 th Excercise -----------------------
---------------- Define a default class property -----------------
------------------------------------------------------------------'''

excercise_112 = '''Define property that should have the same value for every class instance. 
Define a class attribute 'color' default value. Every Vehicle should have that color'''

print(title_112)
print(excercise_112)

class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = 'Whilte'

object_a = Vehicle (50,1)
print (f'Object attributes\nobject_a.max_speed = {object_a.max_speed}\nobject_a.mileage = {object_a.mileage}\nobject_a.color = {object_a.color}')

title_113 = '''-----------------------------------------------------------------
------------------------- 113 th Excercise -----------------------
------------------- Class inheritance - REMIX --------------------
------------------------------------------------------------------'''

excercise_113 = '''Class inheritance given: Create a Bus child class that inherits from the Vehicle
class. The default fare charge of any vehicle is seating capacity *100. If Vehicle is Bus instance, 
we need to add and extra 10%/ an full fare as a maintenance charge. So total fare Bus isntance will 
become the final ammount = total fare + 10%/ of the total fare'''

print(title_113)
print(excercise_113)

class Vehicle:
    def __init__(self,max_speed,mileage,name,seating_capacity):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name
        self.seating_capacity = seating_capacity * 100

class Bus (Vehicle):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        if issubclass(Bus,Vehicle):
            self.seating_capacity = self.seating_capacity * 1.1

object_a = Vehicle(100,1000,"92' Chevette", 4)
object_b = Bus(max_speed = 200,mileage = 2000,name = 'Encava boleta el mio',seating_capacity = 50)

print ('Vehicle instance')
print (f'max speed{object_a.max_speed}\nmileage {object_a.mileage}\nname {object_a.name}\nseating_capacity {object_a.seating_capacity}')
print ('Bus instance')
print (f'max speed{object_b.max_speed}\nmileage {object_b.mileage}\nname {object_b.name}\nseating_capacity {object_b.seating_capacity}')

title_114 = '''-----------------------------------------------------------------
------------------------- 114 th Excercise -----------------------
---------------- Check object type of an isntance ----------------
------------------------------------------------------------------'''

excercise_114 = '''Determine which class a given Bus object belongs to (Check type of an object) - 
Keep previous values'''

print(title_114)
print(excercise_114)

print (f'Vehicle instance type {type(object_a)}')
print (f'Bus instance type {type(object_b)}')

title_115 = '''-----------------------------------------------------------------
------------------------- 115 th Excercise -----------------------
-------------- Check if an instance of child class ---------------
------------------- is instance of parent class ------------------
------------------------------------------------------------------'''

excercise_115 = '''Determine if an instance of child class is instance of parent class'''

print(title_115)
print(excercise_115)

print (f'Bus instance check {isinstance(object_b,Vehicle)}') 
print (f'Bus instance check {isinstance(object_b,Bus)}')

# Yay!