def create_list():
    return [i for i in range(1000)]


def create_set():
    return set([i for i in range(1000)])


def find(it, el=50):
    return el in it


def create_list():
    return [i for i in range(1000)]


def create_set():
    return set([i for i in range(1000)])


def find(it, el=50):
    return el in it


def test_list(benchmark):
    benchmark(find, it=create_list())


def test_set(benchmark):
    benchmark(find, it=create_set())
