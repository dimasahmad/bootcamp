# day of the programmer
# https://www.hackerrank.com/challenges/day-of-the-programmer/problem

def day_of_programmer(year: int) -> str:
    """Determine Day of the Programmer of the year given

    Args:
        year (int): year given
    Returns:
        str: string representing the date of the 256th day of the year given in the format dd.mm.yyyy
    """

    # days per month from January to August
    month_days: list[int] = [31, None, 31, 30, 31, 30, 31, 31]

    if year == 1918:
        month_days[1] = 15  # Feb starts at 14th in 1918
    elif year < 1918:
        month_days[1] = 29 if year % 4 == 0 else 28
    elif year > 1918:
        month_days[1] = 29 if year % 400 == 0 or (
            year % 4 == 0 and not year % 100 == 0) else 28

    dd: int = 256 - sum(month_days)

    return f"{dd}.09.{year}"
