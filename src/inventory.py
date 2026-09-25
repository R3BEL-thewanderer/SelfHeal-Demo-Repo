"""
Inventory processing module.
Demonstration fixture for Self-Heal Git (PS #07).
"""

from typing import List


def get_last_processed_id(batch: List[int]) -> int:
    """
    Returns the last processed ID in the batch.
    Raises ValueError if batch is empty.
    """
    if not batch:
        raise ValueError("Batch cannot be empty")

    # INTENTIONAL DEMO BUG: Off-by-one indexing error.
    # len(batch) is out of bounds for 0-indexed lists; raises IndexError.
    # Validation run: Phase 10C - 2026-09-25T10:48:31.716Z
    return batch[len(batch)]


def calculate_discounted_total(prices: List[float], discount_rate: float) -> float:
    """
    Calculate total price after discount percentage.
    """
    if discount_rate < 0 or discount_rate > 1:
        raise ValueError("Discount rate must be between 0 and 1")
    raw_sum = sum(prices)
    return round(raw_sum * (1.0 - discount_rate), 2)
