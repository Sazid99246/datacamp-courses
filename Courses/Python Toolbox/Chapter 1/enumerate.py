mutants = ['charles xavier', 'bobby drake',
           'kurt wagner', 'max eisenhardt', 'kitty pryde']

mutant_list = list(enumerate(mutants))
print(mutant_list)

for index1, value1 in enumerate(mutants):
    print(index1, value1)

for index2, value2 in list(enumerate(mutants, start=1)):
    print(index2, value2)
