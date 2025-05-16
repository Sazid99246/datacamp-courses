squirrels = [('Marcus Garvey Park', ('Black', 'Cinnamon', 'Cleaning', None)),
             ('Highbridge Park', ('Gray', 'Cinnamon', 'Running, Eating',
                                  'Runs From, watches us in short tree')),
             ('Madison Square Park', ('Gray', None, 'Foraging', 'Indifferent')),
             ('City Hall Park', ('Gray', 'Cinnamon', 'Eating', 'Approaches')),
             ('J. Hood Wright Park', ('Gray', 'White', 'Running', 'Indifferent')),
             ('Seward Park', ('Gray', 'Cinnamon', 'Eating', 'Indifferent')),
             ('Union Square Park', ('Gray', 'Black', 'Climbing', None)),
             ('Tompkins Square Park', ('Gray', 'Gray', 'Lounging', 'Approaches'))]
squirrels_by_park = {}

for park, squirrels_details in squirrels:
    squirrels_by_park[park] = squirrels_details


squirrels_madison = squirrels_by_park.pop('Madison Square Park')
squirrels_city_hall = squirrels_by_park.pop('City Hall Park', {})

del squirrels_by_park["Union Square Park"]
print(squirrels_by_park)
