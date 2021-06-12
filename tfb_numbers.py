""" Timefliesbar date calculus. """

# Contact.

# timefliesbar@protonmail.com

# ---------------------------------------------------------------------------#

import datetime
from calendar import isleap

# ---------------------------------------------------------------------------#

# Obtain basic year information.

current_date: str
current_year: int
current_day: str

current_date = datetime.datetime.now()
current_year = current_date.year
current_day = current_date.strftime("%j")

# ---------------------------------------------------------------------------#

# Obtain year type and total days
# There is a dedicated method from Calendar: isleap.

# string_current_year: str
# """ Int to string conversion needed. """

# string_current_year = str(current_year)

# second_last_digit_current_year: str
# last_digit_current_year: str
# leap_year: int

# second_last_digit_current_year = string_current_year[2:3]
# last_digit_current_year = string_current_year[3:4]

# if current_year % 4 == 0:

#     if second_last_digit_current_year == 0 and last_digit_current_year == 0:

#         if current_year % 400 == 0:

#             leap_year = 1

#         elif current_year % 400 != 0:
#             leap_year = 0

#     else:
#         pass

# elif current_year % 4 != 0:
#     # leap_year = 0

# Total days.

# total_days: int
# """ Total days depending on year type. """

# if leap_year == 1:
#     total_days = 366

# elif leap_year == 0:
#     total_days = 365

# ---------------------------------------------------------------------------#

# Obtain year type and total days.

total_days: int
""" Total days depending on year type. """

if isleap(current_year) == True:
    total_days = 366

elif isleap(current_year) == False:
    total_days = 365

else:
    pass

# ---------------------------------------------------------------------------#

# Obtain total minutes.

total_minutes: int
""" Total minutes. Days * 24 * 60. """

total_minutes = total_days * 1440

# ---------------------------------------------------------------------------#

# Obtain gone minutes.

current_hour: int
""" Local current hour. """
current_minute: int
""" Local current minute. """

gone_minutes: int
""" Minutes elapsed untill current time. """

# Spain local time
current_hour = current_date.strftime("%H")
current_minute = current_date.strftime("%M")

gone_minutes = int(current_day) * 1440 + int(current_hour) * 60 + int(current_minute)


# ---------------------------------------------------------------------------#

# Obtain remaining minutes.

remaining_minutes: int
""" Minutes remaining this year. """

remaining_minutes = int(total_minutes) - int(gone_minutes)
