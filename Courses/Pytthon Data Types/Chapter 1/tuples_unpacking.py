girl_names = ['Jada', 'Emily', 'Ava', 'Serenity', 'Claire', 'Sophia', 'Sarah', 'Ashley', 'Chaya', 'Abigail', 'Zoe', 'Leah',
              'Hailey', 'Ava', 'Olivia', 'Emma', 'Chloe', 'Sophia', 'Aaliyah', 'Angela', 'Camila', 'Savannah', 'Serenity', 'Chloe', 'Fatoumata']
boy_names = ['Josiah', 'Ethan', 'David', 'Jayden', 'Mason', 'Ryan', 'Christian', 'Isaiah', 'Jayden', 'Michael', 'Noah', 'Samuel',
             'Sebastian', 'Noah', 'Dylan', 'Lucas', 'Joshua', 'Angel', 'Jacob', 'Matthew', 'Josiah', 'Jacob', 'Muhammad', 'Alexander', 'Jason']

pairs = zip(girl_names, boy_names)

for rank, pair in enumerate(pairs):
    girl_name, boy_name = pair
    print(f'Rank {rank+1}: {girl_name} and {boy_name}')
