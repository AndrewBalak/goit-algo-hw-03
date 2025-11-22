import re

def normalize_phone(phone_number:str) -> str:
    """
    Normalize a phone number to international telephone code 
    or the canonical Ukrainian format '+380XXXXXXXXX' if international telephone code not set.

    Accepts various common presentations (spaces, punctuation, leading '+', '00' prefix).
    """
    if not isinstance(phone_number, str):
        raise TypeError("Phone number must be a string.")

    # Remove all non-digit characters
    digits = re.sub(r'\D', '', phone_number)

    # Check for international format starting with '+'
    if phone_number.startswith('+') or phone_number.startswith('00'):
        # Check if it is Ukranian number
        if digits.startswith('380') and len(digits) == 12:
            return '+' + digits
        # Else we believe its international number 
        # Country prefix(min 1) + region code(2) + telephone number(7) = 10
        elif len(digits) >= 10:
            return '+' + digits
        else:
            raise ValueError("Unsupported international phone number format.")
    # Handle Ukrainian formats
    else:
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
