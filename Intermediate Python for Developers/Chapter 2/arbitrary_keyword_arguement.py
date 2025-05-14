def concat(**kwargs):
    result = ""

    for kwarg in kwargs.values():
        result += " " + kwarg

    return result

print(concat(start="Python", middle="is",end="great!"))
