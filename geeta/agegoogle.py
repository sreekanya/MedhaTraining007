def calculateAge(born):
    """Calculate the age of a user."""
    today = date.today()
    birthday = date(today.year, born.month, born.day)
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year