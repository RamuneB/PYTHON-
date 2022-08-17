# Turimas "users" masyvas. 

# Parašykite funkcijas, kurios atlikas nurodytas užduotis:
# 1. funkcija "getUserAverageAge" - kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins visų "users" amžiaus visurkį kaip skaičių.
# 2. funkcija "getUsersNames" -  kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins visų "users" vardus naujame list'e pvz., ['Alex John', 'Ann Smith'...].

# Pastaba: rezultatai turi būti išrikiuoti abėcėlės tvarka
import json
users = """
[
  { "id": "1", "name": "John Smith", "age": 20 },
  { "id": "2", "name": "Ann Smith", "age": 24 },
  { "id": "3", "name": "Tom Jones", "age": 31 },
  { "id": "4", "name": "Rose Peterson", "age": 17 },
  { "id": "5", "name": "Alex John", "age": 25 },
  { "id": "6", "name": "Ronald Jones", "age": 63 },
  { "id": "7", "name": "Elton Smith", "age": 16 },
  { "id": "8", "name": "Simon Peterson", "age": 30 },
  { "id": "9", "name": "Daniel Cane", "age": 51 }
]"""
users_trans = json.loads(users)
def getUserAverageAge(users):
    users_age = 0
    users_sk = 0
    for age in users:              
      users_age = users_age + int((age['age']))
      users_sk += 1
    average_age = users_age/users_sk
    return average_age

print(f" Amžiaus vidurkis:", getUserAverageAge(users_trans))

def getUsersNames(users):
    users_list = []
    for us in users:              
     users_list.append(us['name'])
   
    return sorted(users_list)

print(f" Users:", getUsersNames(users_trans))