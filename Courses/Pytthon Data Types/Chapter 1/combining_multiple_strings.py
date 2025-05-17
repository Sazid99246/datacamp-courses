boy_names = ['Josiah', 'Ethan', 'David', 'Jayden', 'Mason',
             'Ryan', 'Christian', 'Isaiah', 'Jayden', 'Michael']

preamble = "The top ten boy names are: "
conjunction = ", and"
first_nine_names = ", ".join(boy_names[0:9])

print(f"{preamble}{first_nine_names}{conjunction} {boy_names[-1]}.")
