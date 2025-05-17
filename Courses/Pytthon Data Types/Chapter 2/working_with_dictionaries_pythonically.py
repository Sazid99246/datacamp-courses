squirrels_by_park = {'Madison Square Park': [{'primary_fur_color': 'Gray',
                                              'highlights_in_fur_color': None,
                                              'activities': 'Foraging',
                                              'interactions_with_humans': 'Indifferent'},
                                             {'primary_fur_color': 'Gray',
                                              'highlights_in_fur_color': None,
                                              'activities': 'Sitting',
                                              'interactions_with_humans': 'Indifferent'}],
                     'Union Square Park': [{'primary_fur_color': 'Gray',
                                            'highlights_in_fur_color': None,
                                            'activities': 'Eating, Foraging',
                                            'interactions_with_humans': None},
                                           {'primary_fur_color': 'Cinnamon',
                                            'highlights_in_fur_color': None,
                                            'activities': 'Foraging',
                                            'interactions_with_humans': None},
                                           {'primary_fur_color': 'Gray',
                                            'highlights_in_fur_color': None,
                                            'activities': 'Eating, Foraging',
                                            'interactions_with_humans': None},
                                           {'primary_fur_color': 'Gray',
                                            'highlights_in_fur_color': None,
                                            'activities': 'Digging',
                                            'interactions_with_humans': 'Indifferent'}]}

for field, value in squirrels_by_park['Madison Square Park'][0].items():
    print(field, value)

print('-' * 13)

for field, value in squirrels_by_park['Union Square Park'][1].items():
    print(field, value)
