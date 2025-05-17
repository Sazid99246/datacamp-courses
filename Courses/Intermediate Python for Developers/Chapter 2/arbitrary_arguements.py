def concat(*args):
    result = ""
    for arg in args:
        result += " " + arg
    return result

print(concat("Python", "is", "great!"))