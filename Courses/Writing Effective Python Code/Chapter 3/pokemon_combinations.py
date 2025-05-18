from itertools import combinations

pokemon = ['Geodude', 'Cubone', 'Lickitung', 'Persian', 'Diglett']

combos_obj = combinations(pokemon, 2)
print(type(combos_obj), '\n')

combos_2 = [*combos_obj]
print(combos_2, '\n')

combos_4 = [*combinations(pokemon, 4)]
print(combos_4)
