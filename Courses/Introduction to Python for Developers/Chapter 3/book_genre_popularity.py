genre_sales = {'Adventure': 367500000, 'Horror': 312500000, 'Literature': 80000000,
               'Manga': 5166000000, 'Mystery': 300000000, 'Romance': 252500000, 'Thriller': 320000000}

for genre, average_sale in genre_sales.items():
    if average_sale == 5166000000:
        print("Most popular genre: ", genre)
        print("Average sales: ", average_sale)
    elif average_sale == 80000000:
        print("Least popular genre: ", genre)
        print("Average sales: ", average_sale)
