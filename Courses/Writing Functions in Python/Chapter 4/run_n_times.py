def run_n_times(func):
    def wrapper(*args, **kwargs):
        for _ in range(10):
            func(*args, **kwargs)
    return wrapper


@run_n_times(10)
def print_sum(a, b):
    print(a + b)


print_sum(15, 20)

run_five_times = run_n_times(5)


@run_five_times
def print_sum(a, b):
    print(a + b)


print_sum(4, 100)

print = run_n_times(20)(print)
print('What is happening?!?!')
