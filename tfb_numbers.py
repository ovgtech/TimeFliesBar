""" TIMEFLIESBAR DATE-RELATED CALCULATIONS. """

# Contact.

# ovgpcomms@outlook.com

# ---------------------------------------------------------------------------#

import datetime
from calendar import isleap

# ---------------------------------------------------------------------------#

# Obtain current basic information.
# All of the operations are intended to be minute-focused, because this is one
# of the principals for this project.

current_date: str
current_year: int
current_day: str
current_day_upscaled: str
previous_day: str
current_hour: int
current_minute: int

current_date = datetime.datetime.now()
current_year = current_date.year
current_day = current_date.strftime("%j")
current_day_upscaled = int(current_day)*2
previous_day = int(current_day) - 1
current_hour = current_date.strftime("%H")
current_minute = current_date.strftime("%M")

# ---------------------------------------------------------------------------#

# Obtain year type and total days (There is a dedicated method from Calendar: isleap).

total_days: int

if isleap(current_year) == True:
    total_days = 366

elif isleap(current_year) == False:
    total_days = 365

else:
    pass

# ---------------------------------------------------------------------------#

# Obtain total minutes.

total_minutes: int # Days * 24 * 60.

total_minutes = total_days * 1440

# ---------------------------------------------------------------------------#

# Obtain gone minutes.

gone_minutes: int 

gone_minutes = int(current_day) * 1440 + int(current_hour) * 60 + int(current_minute)

# ---------------------------------------------------------------------------#

# Obtain remaining minutes.

remaining_minutes: int

remaining_minutes = int(total_minutes) - int(gone_minutes)
