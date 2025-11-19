from datetime import datetime

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d")

def get_days_from_today(date_input):
    """Return whole days between today and date_input.

    Accepts a datetime instance or a 'YYYY-MM-DD' string. Only the date component is used.
    The result is positive when today is after date_input, negative if date_input is in the future.
    """
    if isinstance(date_input, datetime):
        target_date = date_input.date()
    elif isinstance(date_input, str):
        try:
            target_date = string_to_date(date_input).date()
        except ValueError as exc:
            raise ValueError("date must be a string in 'YYYY-MM-DD' format") from exc
    else:
        raise TypeError("date must be a 'YYYY-MM-DD' string or a datetime instance")

    today = datetime.today().date()
    return (today - target_date).days