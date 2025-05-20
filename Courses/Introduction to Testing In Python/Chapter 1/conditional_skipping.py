from datetime import datetime
import pytest

day_of_week = datetime.now().isoweekday()


def get_unique_values(lst):
    return list(set(lst))


condition_string = 'day_of_week == 6'


@pytest.mark.skipif(condition_string)
def test_function():
    assert get_unique_values([1, 2, 3]) == [1, 2, 3]
    assert get_unique_values([1, 2, 3, 1]) == [1, 2, 3]
