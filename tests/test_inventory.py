import pytest
from src.inventory import get_last_processed_id, calculate_discounted_total


def test_last_processed_id_valid_batch():
    batch = [101, 102, 103, 104]
    # Standard contract: expect last element 104
    assert get_last_processed_id(batch) == 104


def test_impossible_batch_contract():
    # INTENTIONAL DEMO NON-CONVERGENCE (Phase 10D):
    # Demands 999999 for the identical input [101, 102, 103, 104],
    # creating an impossible contradiction with test_last_processed_id_valid_batch.
    batch = [101, 102, 103, 104]
    assert get_last_processed_id(batch) == 999999


def test_calculate_discounted_total():
    prices = [10.0, 20.0, 30.0]
    assert calculate_discounted_total(prices, 0.1) == 54.0
