def make_pizzas(size, *toppings):
    '''Print the pizza for size and topping'''
    print('Make a -' + str(size) + 'inches pizza with topping:')
    for topping in toppings:
        print('- {}'.format(topping).title())



#When I write down these 2 lines, I always write print. should remember no need for print
make_pizzas(16, 'mushroom')
make_pizzas(18, 'mushroom' , 'pepperoni' , 'cheese')
