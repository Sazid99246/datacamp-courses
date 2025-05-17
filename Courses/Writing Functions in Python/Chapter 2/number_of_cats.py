with open('alice.txt', encoding="UTF-8") as file:
    text = file.read()
    n = 0
    for word in text.split():
        if word.lower() in ['cat', 'cats']:
            n += 1
    print('Lewis Carroll uses the word "cat" {} times'.format(n))
