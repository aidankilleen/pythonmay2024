# dicitionary_investigation.py

info = {
    'a': 1, 
    'b': 10, 
    'c': 7
}

print (info)

print (info['a'])
print (info['b'])
print (info['c'])

print (info.keys())

for key in info.keys():
    print (f"{ key } = { info[key] }")

print (info.values())

print (info.items())


for item in info.items():
    print (item)


# iterate using the key and value
    
for key, value in info.items():

    print (f"{ key } = { value }")



data = {
    'cork': {
        'population': 300000, 
        'area': 123456,
        'towns':("Mallow", "Mitchelstown", "Midleton")
    }, 
    'dublin': {
        'population': 1230000, 
        'area': 12345, 
        'towns':("Dun Laoghaire", "Swords", "Sallins")
    }
}
print (data['cork']['population'])

for town in data['dublin']['towns']:
    print (town)

# dictionaries are mutable
    
data['waterford'] = {
    'population': 150000, 
    'area': 33333, 
    'towns': ("Dungarvan", "Tramore")
}

for town in data['waterford']['towns']:
    print (town)


print ("===========================")

population = 0

for county in data.keys():
    print (county)
    #population = population + data[county]['population']
    population += data[county]['population']

print (f"Total population:{ population }")


print ("=" * 25)





