madhura = {
    'gender': 'female',
     'age':  '30',
     'city': 'cork'
}

madhura ['surname'] = 'guha'

car = {
    'color': 'blue',
    'model': 'golf',
    'year': '2020'

}

car1 = dict(car)

car1['color'] = 'red'
car1['model'] = 'polo'

print(f"madhura, your car color is {car['color']}")
print(f"Madhura your city is: {madhura['city']}")
print(madhura)
print(car)
print(car1)

#------------------------------------------------
# next example

bigglesworth = { 
    'fur': 'none',
    'eyes': 'souls of the damned',
    'toes': 'cloven hoofs',
    'favourite foods': ['joy', 'happiness', 'souls', 'tuna - occasionally']
    }
for details in bigglesworth['favourite foods']:
    print(f"bigglesworth's favourite food is {details}")