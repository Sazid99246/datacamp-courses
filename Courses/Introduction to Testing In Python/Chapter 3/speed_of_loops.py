def test_list(benchmark):
    @benchmark
    def iterate_list():
        for _ in [i for i in range(1000)]:
            pass


def test_set(benchmark):
    @benchmark
    def iterate_set():
        for i in {i for i in range(1000)}:
            pass
