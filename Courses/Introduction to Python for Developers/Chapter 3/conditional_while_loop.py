release_date = 26
current_date = 22

while current_date <= release_date:
    if current_date <= 24:
        print("Purchase before the 25th for early access")
    elif current_date == 25:
        print("Coming soon!")
    else:
        print("Available now!")
    current_date += 1
