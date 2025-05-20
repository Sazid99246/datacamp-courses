import pytest


@pytest.fixture
def init_list():
    return []


@pytest.fixture(autouse=True)
def add_numbers_to_list(init_list):
    init_list.extend([i for i in range(10)])


def test_elements(init_list):
    assert len(init_list) == 10
    assert init_list == list(range(10))
