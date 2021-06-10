""" Timefliesbar date calculus. """

# Contact.

# timefliesbar@protonmail.com

# ---------------------------------------------------------------------------#

import datetime

# ---------------------------------------------------------------------------#

# Obtain basic year information.

current_date: str
current_year: int
current_day: str

current_date = datetime.datetime.now()
current_year = current_date.year
current_day = current_date.strftime("%j")

# ---------------------------------------------------------------------------#

# Obtain year type.

string_current_year: str
""" Int to string conversion needed. """

string_current_year = str(current_year)

second_last_digit_current_year: str
last_digit_current_year: str
leap_year: int

second_last_digit_current_year = string_current_year[2:3]
last_digit_current_year = string_current_year[3:4]

if current_year % 4 == 0:

    if second_last_digit_current_year == 0 and last_digit_current_year == 0:

        if current_year % 400 == 0:

            leap_year = 1

        elif current_year % 400 != 0:
            leap_year = 0

    else:
        pass

elif current_year % 4 != 0:
    leap_year = 0

# ---------------------------------------------------------------------------#

# Obtain total days.

total_days: int
""" Total days depending on year type. """

if leap_year == 1:
    total_days = 366

elif leap_year == 0:
    total_days = 365

# ---------------------------------------------------------------------------#

# Obtain total minutes.

total_minutes: int
""" Total minutes. Days + 60. """

total_minutes = total_days * 1440

# ---------------------------------------------------------------------------#

# Obtain gone minutes.

# pe_current_hour: str
# """ PythonEverywhere current hour. """
# pe_current_minute: str
# """ PythonEverywhere current minute. """

current_hour: int
""" Local current hour. """
current_minute: int
""" Local current minute. """

gone_minutes: int
""" Minutes elapsed untill current time. """

# PE date correction
# pe_current_hour = current_date.strftime("%H")  #PythonEverywhere environment has 1 hour less
# pe_current_minute = current_date.strftime("%M")   #PythonEverywhere environment has 60 minutes less

# current_hour = int(pe_current_hour) + 1    #Hour more correction to local hour
# current_minute = int(pe_current_minute) + 60   #Hour more correction to local hour

# Straight hour
current_hour = current_date.strftime("%H")
current_minute = current_date.strftime("%M")

gone_minutes = int(current_day) * 1440 + int(current_hour) * 60 + int(current_minute)

# ---------------------------------------------------------------------------#

# Obtain remaining minutes.

remaining_minutes: int
""" Minutes remaining this year. """

remaining_minutes = int(total_minutes) - int(gone_minutes)
