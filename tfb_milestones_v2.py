""" TimeFliesBar Milestones v2. """

# ---------------------------------------------------------------------------#
# Contact.
# ovgpcomms@outlook.com
# ---------------------------------------------------------------------------#

# Imports.
from tfb_numbers_v2 import half_year as hy
from tfb_numbers_v2 import total_days as td

# Variables.
hy: int # Day which is half of the year.
td: int # Total days in a year.
mid: str # Half year message.
last: str # Last day of the year message.
first: str # First day of the year message.


# Message intended to show
mid = "Today we are reaching the 50% of the year."
last = "Today we are reaching the 100% of the year.\nTomorrow will be a new year!"
first = "Happy New Year! Everything starts again."


# Function
def milestones(cd):

    if cd == 1:
        return first
    elif cd == hy:
        return mid
    elif cd == td:
        return last
    else:
        pass