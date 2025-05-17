def convert_data_structure(data, data_type="list"):
  if data_type == "tuple":
    data = tuple(data)  
  elif data_type == "set":
    data = set(data)
  else:
    data = list(data)
  return data

convert_data_structure({"a", 1, "b", 2, "c", 3}, data_type="set")