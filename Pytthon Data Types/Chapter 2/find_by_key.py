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

print(squirrels_by_park.get('Union Square Park'))
print(type(squirrels_by_park.get('Fort Tryon Park')))
print(squirrels_by_park.get('Central Park', 'Not Found'))
