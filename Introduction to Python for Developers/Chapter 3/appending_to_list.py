authors_below_twenty_five = []

for key, value in authors.items():
    if value < 25:
        authors_below_twenty_five.append(key)

print(authors_below_twenty_five)
