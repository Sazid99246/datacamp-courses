import pandas as pd
import pytest


@pytest.fixture
def get_df():
    return pd.read_csv('https://assets.datacamp.com/production/repositories/6253/datasets/757c6cb769f7effc5f5496050ea4d73e4586c2dd/laptops_train.csv')


def agg_with_sum(data, group_by_column, aggregate_column):
    return data.groupby(group_by_column)[aggregate_column].sum()


def test_agg_feature(get_df):
    aggregated = agg_with_sum(get_df, 'Manufacturer', 'Price')

    assert type(aggregated) == pd.Series
    assert aggregated.shape[0] > 0
    assert aggregated.dtype in (int, float, 'int64', 'float64')
