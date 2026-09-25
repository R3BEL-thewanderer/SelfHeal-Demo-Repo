import pytest
from src.inventory import get_last_processed_id, calculate_discounted_total


def test_last_processed_id_valid_batch():
    batch = [101, 102, 103, 104]
    assert get_last_processed_id(batch) == 104


def test_calculate_discounted_total():
    prices = [10.0, 20.0, 30.0]
    assert calculate_discounted_total(prices, 0.1) == 54.0
