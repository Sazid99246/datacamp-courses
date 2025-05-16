squirrels_by_park['Madison Square Park'] = squirrels_madison
squirrels_by_park.update([squirrels_union])
for park_name in squirrels_by_park:
    print(park_name, [squirrel.get('primary_fur_color', 'N/A')
          for squirrel in squirrels_by_park[park_name]])
