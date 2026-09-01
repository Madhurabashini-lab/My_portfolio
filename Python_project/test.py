
def describe_pet(pet_name, animal_type, pet_last_name=' '):
    if pet_last_name:
        pet_info = pet_name + ', ' + pet_last_name + ', ' + animal_type
    else:
        pet_info = pet_name + ', ' + animal_type
    return pet_info

my_pet = describe_pet('Frankie', 'dachshund')
print(my_pet)

my_pet = describe_pet('Frankie', 'dachshund', 'Furter')
print(my_pet)
#--------------------------------------------------------------------------------------------

fridge = ['chicken', 'beef', 'sausages']
empty_items = []

def eat_food(name, foods):
    print(foods)
    for food in foods:
        print(f"{name} is eating {food}")  
        empty_items.append(food)
        fridge.remove(food)

cooked = fridge[:]
eat_food('Scout', cooked)
for item in empty_items:
    print(f"You've eaten all of the {item}!")
if not fridge:
    print("\nYou've eaten everything in the house!")