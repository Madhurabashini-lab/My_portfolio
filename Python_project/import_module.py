import pizza_module

print('Welcome to my pizza shop\n')

while True:
    size = input('Please choose a pizza size (9, 12, 16)or q to quit:\n>')
    if size != 'q':
        
        base = input('Please choose a base type (thin, deep, stuffed crust):\n>')
        new_order1 = pizza_module.make_base(size, base)
        print(new_order1)
        
        sauce = input('Please choose a sauce (tomato, BBQ, none):\n>')
        new_order2 = pizza_module.add_sauce(new_order1, sauce)
        print(new_order2)
        toppings = []
        
        while True:
            topping_choice = input('Please choose a topping (Pepperoni, Mushroom, Chicken, Pineapple, Ham) "q" when done:\n>')
            if topping_choice != 'q':
                toppings.append(topping_choice)
            else:
                break
            
        new_order3 = pizza_module.add_toppings(new_order2, toppings)
        print(new_order3)
        print(f'You have ordered:\n')
        
        for k,v in new_order3.items():
            print(k,v)
            
    else:
        break
 
 