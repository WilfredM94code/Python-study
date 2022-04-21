from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
print ('''from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta''')

title_98 = '''-----------------------------------------------------------------
------------------------ 98 th Excercise ------------------------
------------------ Print current date and time ------------------
------------------------------------------------------------------'''

excercise_98 = '''Print current date and time'''

print(title_98)
print(excercise_98)

print (f'Datetime {datetime.now()}')

title_99 = '''-----------------------------------------------------------------
------------------------- 99 th Excercise ------------------------
-------------------- Convert string in datetime ------------------
------------------------------ object ----------------------------
------------------------------------------------------------------'''

excercise_99 = '''Convert string into a datetime object'''

print(title_99)
print(excercise_99)

string_a = 'Feb 25 2020 04:20PM'

datetime_a = datetime.strptime(string_a, "%b %d %Y %I:%M%p")
print (f'Datetime {datetime_a}')

title_100 = '''-----------------------------------------------------------------
------------------------- 100 th Excercise -----------------------
-------------------- Substract a week from date ------------------
------------------------------------------------------------------'''

excercise_100 = '''Subtract a week (7 days) from a given date'''

print(title_100)
print(excercise_100)

datetime_a = datetime.now()
timedelta_a = timedelta(days= 7)
timedelta_a = datetime_a - timedelta_a
print (f'Previous week from now {timedelta_a}')

title_101 = '''-----------------------------------------------------------------
------------------------- 101 th Excercise -----------------------
------------------- Print date in the following ------------------
------------------------------ format ----------------------------
------------------------------------------------------------------'''

excercise_101 = '''Print a date in the following format'''

print(title_101)
print(excercise_101)

# 02-02-2022 15:55:32

datetime_a = datetime.now()
strftime_a = datetime_a.strftime('%d-%m-%Y %H:%M:%S')
print (f'Date in string {strftime_a}')

title_102 = '''-----------------------------------------------------------------
------------------------- 102 th Excercise -----------------------
----------------- Find day of the week from given ----------------
------------------------------- date -----------------------------
------------------------------------------------------------------'''

excercise_102 = '''Find day of the week from given date'''

print(title_102)
print(excercise_102)

datetime_a = datetime(day = 1 , month = 3 , year = 1955)
print (f'Datetime {datetime_a}')
print (f'Day of the week {datetime_a.weekday()}')
print (f'Day of the week {datetime_a.strftime("%A")}')

title_103 = '''-----------------------------------------------------------------
------------------------- 103 th Excercise -----------------------
------------------ Add days and hours to a given -----------------
------------------------------- date -----------------------------
------------------------------------------------------------------'''

excercise_103 = '''Add a week and 12 hours to a given date'''

print(title_103)
print(excercise_103)

datetime_a = datetime.now()
timedelta_a = timedelta(days= 7, hours= 12)
timedelta_a = datetime_a + timedelta_a
print (f'Actual datetime {datetime_a}')
print (f'Modified datetime {timedelta_a}')

title_104 = '''-----------------------------------------------------------------
------------------------- 104 th Excercise -----------------------
---------------- Print current time in miliseconds ---------------
------------------------------------------------------------------'''

excercise_104 = '''Print current time in miliseconds'''

print(title_104)
print(excercise_104)

datetime_a = datetime.now().timestamp()
print (f'Actual datetime in milisecond {datetime_a}')

title_105 = '''-----------------------------------------------------------------
------------------------- 105 th Excercise -----------------------
---------------- Convert the following datetime to ---------------
------------------------------ string ----------------------------
------------------------------------------------------------------'''

excercise_105 = '''Convert the following datetime to string'''

print(title_105)
print(excercise_105)

datetime_a = datetime(day = 23 , month = 11 , year = 1995)
strftime_a = datetime_a.strftime('%d-%m-%Y')
print(f'Datetime in string {strftime_a}\nType {type(strftime_a)}')

title_106 = '''-----------------------------------------------------------------
------------------------- 106 th Excercise -----------------------
----------------- Calculate the date 4 months from ---------------
--------------------------- a given date -------------------------
------------------------------------------------------------------'''

excercise_106 = '''Calculate the date 4 months from a given date'''

print(title_106)
print(excercise_106)

datetime_a = datetime(day = 12 , month = 9 , year = 2011).date()
relativedelta_a = relativedelta(month = 4)
relativedelta_a = datetime_a + relativedelta_a
print (f'Given time {datetime_a}')
print (f'Updated time {relativedelta_a}')

title_107 = '''-----------------------------------------------------------------
------------------------- 107 th Excercise -----------------------
----------------- Calculate number of days between ---------------
---------------------------- two dates ---------------------------
------------------------------------------------------------------'''

excercise_107 = '''Calculate number of days between two dates'''

print(title_107)
print(excercise_107)

datetime_a = datetime(day = 12 , month = 9 , year = 2011)
datetime_b = datetime(day = 12 , month = 12 , year = 2019)
if datetime_a > datetime_b:
    delta = datetime_a - datetime_b
else:
    delta = datetime_b - datetime_a

print (f'Ammount of days {delta.days}')