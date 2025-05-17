from collections import defaultdict

weight_log = [('Gentoo', 'MALE', 5500.0),
              ('Chinstrap', 'MALE', 4300.0),
              ('Adlie', 'MALE', 3800.0),
              ('Gentoo', 'MALE', 5800.0),
              ('Chinstrap', 'MALE', 4100.0),
              ('Adlie', 'MALE', 3975.0),
              ('Gentoo', 'MALE', 5400.0),
              ('Chinstrap', 'MALE', 4800.0),
              ('Chinstrap', 'MALE', 3950.0),
              ('Gentoo', 'MALE', 5250.0),
              ('Gentoo', 'MALE', 4925.0),
              ('Adlie', 'MALE', 3950.0),
              ('Chinstrap', 'MALE', 3800.0),
              ('Chinstrap', 'MALE', 4050.0),
              ('Adlie', 'MALE', 3650.0)]

labeled_entries = defaultdict(list)

for species, sex, body_mass in weight_log:
    labeled_entries[species].append(body_mass)

# Iterate over the first twenty entries in labeled_entries
for entry in labeled_entries[:20]:
    # Check if the species is 'Chinstrap'
    if entry.species == 'Chinstrap':
        # Print the sex and body_mass separated by a colon
        print(f'{entry.sex}:{entry.body_mass}')
