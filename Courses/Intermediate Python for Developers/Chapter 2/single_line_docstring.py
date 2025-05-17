def clean_string(text):
  
  """Swap spaces to underscores and convert text to lowercase."""

  no_spaces = text.replace(" ", "_")
  clean_text = no_spaces.lower()
  return clean_text

# Access the docstring
print(clean_string.__doc__)