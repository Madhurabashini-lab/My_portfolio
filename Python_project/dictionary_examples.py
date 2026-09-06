
river = {
    'nile': 'egypt',
    'ganges': 'india',
    'amazon': 'brazil'
}

for  name, place in river.items():
    print(f"The river name is {name} and place is {place}")
for name in river.keys():
    print(f"The name is {name}")
for place in river.values():
    print(f"the place is {place}")
#---------------------------------------------------------------------

frankie = {
    'animal' : 'dog',
    'owner name': 'bashini',
    'place': 'cork'
}

oreo = {
    'animal': 'cat',
    'owner name': 'guha',
    'place': 'dublin'
}

lucy ={
    'animal' : 'petdog',
    'owner': 'madhu',
    'place': 'west cork'
}
pets = (frankie, oreo, lucy)

for pet in pets:
    print(pet)
#-------------------------------------------------------

cats = {
    'weasley' : { 
        'fur': 'white and ginger',
        'eyes': 'yellow',
        'toes': 'pink'
        },

    'noche' : { 
        'fur': 'black',
        'eyes': 'green',
        'toes': 'pink'
        },

    'bigglesworth' : { 
        'fur': 'none',
        'eyes': 'red',
        'toes': 'cloven hoofs'
        }
}

for name, info in cats.items():
    print(f"the cat name is {name} and info about the cat is {info}" )

#-----------------------------------------------

cities = {
    'Cork': {
        'country': 'Ireland',
        'population': '225,000',
        'fact': 'Cork is known as the Rebel County.'
    },
    'London': {
        'country': 'United Kingdom',
        'population': '9,000,000',
        'fact': 'London is home to Big Ben.'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': '14,000,000',
        'fact': 'Tokyo is one of the largest metropolitan areas in the world.'
    }
}

for city, information in cities.items():
    print(city, information)





