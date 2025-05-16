squirrels = [('Marcus Garvey Park', ('Black', 'Cinnamon', 'Cleaning', None)),
             ('Highbridge Park', ('Gray', 'Cinnamon', 'Running, Eating',
                                  'Runs From, watches us in short tree')),
             ('Madison Square Park', ('Gray', None, 'Foraging', 'Indifferent')),
             ('City Hall Park', ('Gray', 'Cinnamon', 'Eating', 'Approaches')),
             ('J. Hood Wright Park', ('Gray', 'White', 'Running', 'Indifferent')),
             ('Seward Park', ('Gray', 'Cinnamon', 'Eating', 'Indifferent')),
             ('Union Square Park', ('Gray', 'Black', 'Climbing', None)),
             ('Tompkins Square Park', ('Gray', 'Gray', 'Lounging', 'Approaches'))]
squirrels_union = ('Union Square Park',
                   [{'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Eating, Foraging', 'interactions_with_humans': None},
                       {'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Cinnamon',
                           'activities': 'Climbing, Eating', 'interactions_with_humans': None},
                       {'primary_fur_color': 'Cinnamon', 'highlights_in_fur_color': None,
                           'activities': 'Foraging', 'interactions_with_humans': 'Indifferent'},
                       {'primary_fur_color': 'Gray', 'highlights_in_fur_color': None,
                           'activities': 'Running, Digging', 'interactions_with_humans': 'Runs From'},
                       {'primary_fur_color': 'Gray', 'highlights_in_fur_color': None,
                           'activities': 'Digging', 'interactions_with_humans': 'Indifferent'},
                       {'primary_fur_color': 'Gray', 'highlights_in_fur_color': 'Black',
                           'activities': 'Climbing', 'interactions_with_humans': None},
                       {'primary_fur_color': 'Gray', 'highlights_in_fur_color': None, 'activities': 'Eating, Foraging', 'interactions_with_humans': None}])
squirrels_by_park = {}

for park, squirrels_details in squirrels:
    squirrels_by_park[park] = squirrels_details

squirrels_madison = squirrels_by_park['Madison Square Park']
squirrels_by_park.update([squirrels_union])

for park_name, data in squirrels_by_park.items():
    if isinstance(data, list):
        print(park_name, [squirrel.get('primary_fur_color', 'N/A')
              for squirrel in data])
    else:
        print(park_name, "Data not in dictionary format")
