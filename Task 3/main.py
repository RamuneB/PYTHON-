# Turimas "audi" dict.

# Parašykite funkciją "showObjectKeys", kuri kaip argumentą priims objektą 
# ir grąžins visus jo "values" list'e.

audi = {
  "make": 'audi',
  "model": 'A6',
  "year": 2005,
  "color": 'white',
}

def showObjectKeys(au):
  for val in au.values():
    if isinstance(val, dict):
      yield from showObjectKeys(val)
    else:
      yield val
audi_list = list(showObjectKeys(audi))
print(f"Value's :", audi_list)
