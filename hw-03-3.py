import re

def normalize_phone(phone_number:str) -> str:
    """
    Normalize a phone number to the canonical Ukrainian format '+380XXXXXXXXX'.

    Accepts various common presentations (spaces, punctuation, leading '+', '00' prefix).
    Returns a 13-digit string starting with '+380' or raises ValueError for unsupported formats.
    """
    if not isinstance(phone_number, str):
        raise TypeError("Phone number must be a string.")

    # Remove all non-digit characters
    digits = re.sub(r'\D', '', phone_number)

    if digits.startswith('380') and len(digits) == 12:
        return '+' + digits
    elif digits.startswith('80') and len(digits) == 11:
        return '+3' + digits
    elif digits.startswith('0') and len(digits) == 10:
        return '+38' + digits
    elif len(digits) == 9:
        return '+380' + digits
    else:
        raise ValueError("Unsupported phone number format.")
