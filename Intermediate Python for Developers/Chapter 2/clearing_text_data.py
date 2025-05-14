def clean_string(text):
    no_spaces = text.replace(" ", "_")
    clean_text = no_spaces.lower()
    return clean_text


converted_text = clean_string("I LoVe dATaCamP!")
print(converted_text)
