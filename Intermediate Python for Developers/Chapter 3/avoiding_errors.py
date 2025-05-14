def snake_case(text):
  try:
    clean_text = text.replace(" ", "_")
    clean_text = clean_text.lower()
  except:
    print("The snake_case() function expects a string as an argument, please check the data type provided.")
    
snake_case("User Name 187")