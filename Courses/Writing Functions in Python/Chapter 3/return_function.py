def create_math_function(func_name):
    if func_name == 'add':
        def add(a, b):
            return a + b
        return add
    elif func_name == 'subtract':
        def subtract(a, b):
            return a - b
        return subtract
    else:
        print("I don't know that one")


add = create_math_function('add')
print('5 + 2 = {}'.format(add(5, 2)))

subtract = create_math_function('subtract')
print('5 - 2 = {}'.format(subtract(5, 2)))


x = 50


def one():
    x = 10


def two():
    global x
    x = 30


def three():
    x = 100
    print(x)


for func in [one, two, three]:
    func()
    print(x)
