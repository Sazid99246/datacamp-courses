ash_pokedex = ['Pikachu', 'Bulbasaur', 'Koffing', 'Spearow',
               'Vulpix', 'Wigglytuff', 'Zubat', 'Rattata', 'Psyduck', 'Squirtle']

brock_pokedex = ['Onix', 'Geodude', 'Zubat', 'Golem', 'Vulpix',
                 'Tauros', 'Kabutops', 'Omastar', 'Machop', 'Dugtrio']

# Convert Brock's Pokédex to a set
brock_pokedex_set = set(brock_pokedex)
print(brock_pokedex_set)

# Check if Psyduck is in Ash's list and Brock's set
print('Psyduck' in ash_pokedex)
print('Psyduck' in brock_pokedex_set)

# Check if Machop is in Ash's list and Brock's set
print('Machop' in ash_pokedex)
print('Machop' in brock_pokedex_set)
