""" TimeFliesBar Milestones v2. """

# ---------------------------------------------------------------------------#
# Contact.
# ovgpcomms@outlook.com
# ---------------------------------------------------------------------------#

# Imports.
from tfb_numbers_v2 import half_year as hy
from tfb_numbers_v2 import total_days as td
from tfb_numbers_v2 import current_year as cy

# Variables.
hy: int # Day which is half of the year.
td: int # Total days in a year.
mid: str # Half year message.
last: str # Last day of the year message.
first: str # First day of the year message.
message: str # Message to be shown if milestone is happening.


# Message intended to show
mid = "Today we reach the halfway point of the year " + str(cy) + ". You still have time."
last = "Today time is running out for the year " + str(cy) + ". Have you made the most of it?"
first = "Today everything starts again with " + str(cy) + ". You know what to do."


# Function
def milestones(cd):
    if int(cd) == int(1):
        message = first
        return message
    elif int(cd) == int(hy):
        message = mid
        return message
    elif int(cd) == int(td):
        message = last
        return message
    else:
        pass