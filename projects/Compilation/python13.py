import json
from pathlib import Path
from json import JSONEncoder
print('''import json
from pathlib import Path
from json import JSONEncoder''')

title_116 = '''-----------------------------------------------------------------
------------------------- 116 th Excercise -----------------------
------------------- Convert dictionary in JSON -------------------
------------------------------------------------------------------'''

excercise_116 = '''Convert the following dictionary into a JSON format'''

print(title_116)
print(excercise_116)

dict_a = {
    'song': 'Oh my god',
    'artist': 'Birgersson Lundberg'
}

json_a = json.dumps(dict_a)
print (f'JSON file {json_a}')

title_117 = '''-----------------------------------------------------------------
------------------------- 117 th Excercise -----------------------
-------------------- Access a value from JSON --------------------
----------------------------- object -----------------------------
------------------------------------------------------------------'''

excercise_117 = '''Access a value from the following JSON'''

print(title_117)
print(excercise_117)

dict_a = {
    'song': 'Question!',
    'artist': 'System of a down'
}

json_a = json.dumps(dict_a)
dict_b = json.loads(json_a)

print(f'Value {dict_b["song"]}')

title_118 = '''-----------------------------------------------------------------
------------------------- 118 th Excercise -----------------------
------------------ Create and save a JSON file -------------------
------------------------------------------------------------------'''

excercise_118 = '''Start a JSON keys and write them into a file'''

print(title_118)
print(excercise_118)

dict_a = {
    'song': '(Interemezzo)Cavalleria Rusticana',
    'artist': 'Pietro Mascagni'
}

json_a = json.dumps(dict_a)
path_a = Path('json_a.json')
path_a.write_text(json_a)
print (f'Path {path_a}')

title_119 = '''-----------------------------------------------------------------
------------------------- 119 th Excercise -----------------------
------------------ Modify dested key from JSON -------------------
------------------------------------------------------------------'''

excercise_119 = '''Access the nested key 'salary' from the following JSON'''

print(title_119)
print(excercise_119)

string_a = '''{
    "company":{
        "employee":{
            "name":"Rick",
            "payable":{
                "salary":7500,
                "bonus":800
            }
        }
    }
}'''

dict_a = json.loads(string_a)
dict_a['company']['employee']['payable']['salary'] = 9000
print (f"Salary: {dict_a['company']['employee']['payable']['salary']}")

title_120 = '''-----------------------------------------------------------------
------------------------- 120 th Excercise -----------------------
-------------------- Convert object into JSON --------------------
------------------------------------------------------------------'''

excercise_120 = '''Convert the Vehicle object into JSON'''

print(title_120)
print(excercise_120)

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

class VehicleEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

vehicle = Vehicle('Toyota 4runner','2.5L', 75000)

json_a = json.dumps(vehicle, indent=4,cls=VehicleEncoder)
print(f'JSON: {json_a}')

title_121 = '''-----------------------------------------------------------------
------------------------- 121 th Excercise -----------------------
-------------------- Convert JSON into boject --------------------
------------------------------------------------------------------'''

excercise_121 = '''Convert a JSON into a Vehicle object'''

print(title_121)
print(excercise_121)

def vehicle_decoder(obj):
    return Vehicle(obj['name'],obj['engine'],obj['price'])

vehicle = json.loads(
    '{ "name":"Toyota 4runner", "engine":"2.5L", "price":75000 }',
    object_hook=vehicle_decoder)

print (f'Vehicle is instance of Vehicle :{isinstance(vehicle,Vehicle)}')

title_122 = '''-----------------------------------------------------------------
------------------------- 122 th Excercise -----------------------
------------------------ Parse a JSON file -----------------------
------------------------------------------------------------------'''

excercise_122 = '''Parse the following JSON to get all the values of a key "name" within an array'''

print(title_122)
print(excercise_122)

string_a = '''[
    {
        "id": 1,
        "name": "name1",
        "color": [
            "red",
            "green"
        ]
    },
    {
        "id": 2,
        "name": "name2",
        "color": [
            "pink",
            "yellow"
        ]
    }
]'''

dict_a = json.loads(string_a)
list_a = [item.get('name') for item in dict_a]
print(f'Name list: {list_a}')
