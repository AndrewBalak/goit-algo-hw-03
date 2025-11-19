import random

def get_numbers_ticket(min:int, max:int, quantity:int) -> list[int]:
    """Return a sorted list of unique random numbers within a specified range.

    Args:
        min (int): The minimum number in the range (inclusive). Must be >= 1.
        max (int): The maximum number in the range (inclusive). Must be <= 1000.
        quantity (int): The number of unique random numbers to generate. Must be between min and max.
    """
    if min < 1 or max > 1000:
        raise ValueError("min must be >= 1 and max must be <= 1000.")
    if quantity > (max - min + 1):
        raise ValueError("Quantity exceeds the range of unique numbers available.")

    return sorted(list(set(random.sample(range(min, max + 1), quantity))))

print(get_numbers_ticket(1, 10, 4))