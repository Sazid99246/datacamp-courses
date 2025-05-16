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

if "Tompkins Square Park" in squirrels_by_park:
    print('Found Tompkins Square Park')

if "Central Park" in squirrels_by_park:
    print('Found Central Park')
else:
    print('Central Park missing')
