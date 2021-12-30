""" TIMEFLIESBAR DATE-RELATED CALCULATIONS. """

# ---------------------------------------------------------------------------#
# Contact.
# ovgpcomms@outlook.com
# ---------------------------------------------------------------------------#


# Imports
import datetime
from calendar import isleap


# Variables
current_date: str # Current date.
current_year: int # Current year.
current_day: str # Current day.
previous_day: str # Previous day.
total_days: int # Total days the in the current year.

half_year: int # Day wich is half of a year.

current_day_upscaled: int # Current day upscaled to fit 1:2 Day/Pixel ratio.
current_percent: str # Current percent elapsed.
current_percent_left: str # Percent left.


# Obtain current basic information.
current_date = datetime.datetime.now()
current_year = current_date.year
current_day = current_date.strftime("%j")
previous_day = int(current_day) - 1


# Obtain total days and half of the year depending if the current year is leap or not.
if isleap(current_year):
    total_days = 366
    half_year = total_days/2
elif not isleap(current_year):
    total_days = 365
    half_year = total_days/2
else:
    pass


# Obtain gone and left percentages.
current_percent = round(100 * (int(current_day)/int(total_days)), 2) # Percent gone
current_percent_left = round(100 - current_percent, 2) # Percent Left (This is a reverse bot)


# Current day times 2 to fit 1:2 Day/Pixel ratio for the Progress Bar.
current_day_upscaled = int(current_day)*2