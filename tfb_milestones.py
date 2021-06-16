""" TIMEFLIESBAR MILESTONES FUNCTION. """

# Contact.

# ovgpcomms@outlook.com

# ---------------------------------------------------------------------------#

# Pass-trough variables.

tm: int # total_minutes from tfb_calculus.
""" Total minutes in a year. """
gm: int # gone_minutes from tfb_calculus.
""" Minutes elapsed. """

# Regular variables.

twentyfive: str
""" 25% milestone. """
fifty: str
""" 50% milestone. """
seventyfive: str
""" 75% milestone. """
hundred: str
""" 99% milestone. """
cero: str
""" 0% milestone. """

current_percent: float
""" Elapsed percent of the year. """
one_day_percent: float
""" Elapsed percent of the year in one day. """

# ---------------------------------------------------------------------------#

# Obtain milestones and the message intended to show

twentyfive = "Today we have reached the 25% of the year."
fifty = "Today we have reached the 50% of the year."
seventyfive = "Today we have reached the 75% of the year."
hundred = "Today we are going to reach the 100% of the year.\nTomorrow will be a new year!"
cero = "Happy New Year! Everything starts again."

def milestone(tm, gm):

    current_percent = round((100 * (gm / int(tm))), 3)

    one_day_percent = round((100 * ((24 * 60) / int(tm))), 3)

    if current_percent >= 25.000 and current_percent <= (25.000 + one_day_percent):
        return twentyfive

    elif current_percent >= 50.000 and current_percent <= (50.000 + one_day_percent):
        return fifty

    elif current_percent >= 75.000 and current_percent <= (75.000 + one_day_percent):
        return seventyfive

    elif current_percent >= (100.000 - one_day_percent) and current_percent <= 100.000:
        return hundred

    elif current_percent >= 00.000 and current_percent <= 00.274:
        return cero

    else:
        pass