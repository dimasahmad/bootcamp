# determine if it's christmas eve and time for milk and cookies
# https://edabit.com/challenge/6nSckbgCx9hjTwmcw

import datetime


def time_for_milk_and_cookies(date: datetime) -> bool:
    return date.month == 12 and date.day == 24


print('time_for_milk_and_cookies(datetime.date(2013, 12, 24)):\n\t{}'.format(
    time_for_milk_and_cookies(datetime.date(2013, 12, 24))))
print('time_for_milk_and_cookies(datetime.date(3000, 12, 24)):\n\t{}'.format(
    time_for_milk_and_cookies(datetime.date(3000, 12, 24))))
print('time_for_milk_and_cookies(datetime.date(2013, 1, 23)):\n\t{}'.format(
    time_for_milk_and_cookies(datetime.date(2013, 1, 23))))
print('time_for_milk_and_cookies(datetime.date(2010, 11, 2)):\n\t{}'.format(
    time_for_milk_and_cookies(datetime.date(2010, 11, 2))))
print('time_for_milk_and_cookies(datetime.date(1980, 9, 24)):\n\t{}'.format(
    time_for_milk_and_cookies(datetime.date(1980, 9, 24))))
