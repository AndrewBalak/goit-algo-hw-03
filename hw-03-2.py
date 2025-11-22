import random

def get_numbers_ticket(min:int, max:int, quantity:int) -> list[int]:
    """Return a sorted list of unique random numbers within a specified range.

    Args:
        min (int): The minimum number in the range (inclusive). Must be >= 1.
        max (int): The maximum number in the range (inclusive). Must be <= 1000.
        quantity (int): The number of unique random numbers to generate. Must be between min and max.
    """
    if not all(isinstance(i, int) for i in (min, max, quantity)):
        raise TypeError("All arguments must be integers.")
    if min < 1 or max > 1000 or quantity > (max - min + 1):
        return []

    return sorted(list(set(random.sample(range(min, max + 1), quantity))))