girl_names = ['Jada', 'Emily', 'Ava', 'Serenity', 'Claire', 'Sophia', 'Sarah', 'Ashley', 'Chaya', 'Abigail', 'Zoe', 'Leah',
              'Hailey', 'Ava', 'Olivia', 'Emma', 'Chloe', 'Sophia', 'Aaliyah', 'Angela', 'Camila', 'Savannah', 'Serenity', 'Fatoumata']

names_with_s = [name for name in girl_names if name.lower().startswith('s')]
print(names_with_s)

names_with_angel = [name for name in girl_names if 'angel' in name.lower()]
print(names_with_angel)
