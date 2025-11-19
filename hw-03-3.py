def normalize_phone(phone_number):
    """Normalize a phone number to the format '380XXXXXXXXX'."""
    cleaned_number = ''.join(filter(str.isdigit, phone_number))

    if cleaned_number.startswith('0') and len(cleaned_number) == 10:
        # Local format starting with '0'
        return '38' + cleaned_number
    elif cleaned_number.startswith('380') and len(cleaned_number) == 12:
        # Already in correct format
        return cleaned_number
    elif cleaned_number.startswith('80') and len(cleaned_number) == 11:
        # Missing leading '3'
        return '3' + cleaned_number
    elif len(cleaned_number) == 9:
        # Missing country code
        return '380' + cleaned_number
    else:
        raise ValueError(f"Unrecognized phone number format: {phone_number}")