names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

indexed_names = []
for i, name in enumerate(names):
    index_name = (i, name)
    indexed_names.append(index_name)
print(indexed_names)

indexed_names_comp = [(i, name) for i, name in enumerate(names)]
print(indexed_names_comp)

indexed_names_unpack = [*enumerate(names, start=1)]
print(indexed_names_unpack)
