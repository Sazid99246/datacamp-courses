if num_beds < min_num_beds:
    print("Insufficient bedrooms")
elif sq_foot <= min_sq_foot:
    print("Too small")
elif rent > max_rent:
    print("Too expensive")
else:
    print("This looks promising!")
