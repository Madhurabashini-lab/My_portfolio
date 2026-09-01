def make_base(size, type):
    print(f'making a {size} inch pizza with a {type} base...')
    my_pizza = {'size': size, 'base': type}
    return my_pizza

def add_sauce(new_pizza, sauce):
    new_pizza['sauce'] = sauce
    print(new_pizza)
    my_pizza = new_pizza
    return my_pizza

def add_toppings(new_pizza, *toppings):
    new_pizza['toppings'] = toppings
    
    my_pizza = new_pizza
    return my_pizza
