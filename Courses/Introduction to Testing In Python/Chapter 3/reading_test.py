import pandas as pd
import pytest


@pytest.fixture
def get_df():
    return pd.read_csv('https://assets.datacamp.com/production/repositories/6253/datasets/757c6cb769f7effc5f5496050ea4d73e4586c2dd/laptops_train.csv')


def test_get_df(get_df):
    assert type(get_df) == pd.DataFrame
    assert len(get_df) > 0
