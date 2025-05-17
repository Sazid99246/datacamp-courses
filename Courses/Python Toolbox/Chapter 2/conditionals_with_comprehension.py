fellowship = ['frodo', 'samwise', 'merry',
              'aragorn', 'legolas', 'boromir', 'gimli']

new_fellowship = [member if len(member) >= 7 else "" for member in fellowship]

print(new_fellowship)
