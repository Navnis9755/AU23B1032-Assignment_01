def add_topping(scoop_size, topping):
    a=input()
    print('choose scoop size:', scoop_size)
    b=input()
    print('choose toppings of your choice', topping)
    return a
    return b
def make_shake(shake):
    c=input()
    print('shake of your choice', shake)
    return c

from ice_cream import*
scoop_size=['small', 'medium', 'large']
topping=['sprinkle', 'hot fudge', 'whipped cream', 'crushed nuts']
shake=['nuts', 'fruit']
add_topping(scoop_size, topping)
make_shake(shake)
