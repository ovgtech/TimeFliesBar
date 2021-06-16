""" Timefliesbar milestone function. """

# Contact.

# timefliesbar@protonmail.com

# ---------------------------------------------------------------------------#

# Declaring variables.

tm: int # total_minutes from tfb_calculus.
""" Total minutes in a year. """
gm: int # gone_minutes from tfb_calculus.
""" Minutes elapsed. """

twentyfive: str
""" 25% milestone. """
fifty: str
""" 50% milestone. """
seventyfive: str
""" 75% milestone. """
ninetynine: str
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
ninetynine = "Today we have reached the 99% of the year. Tomorrow will be a new year!"
cero = "Happy New Year! Everything starts again."

def milestone(tm, gm):

    current_percent = round((100 * (gm / int(tm))), 3)

    one_day_percent = round((100 * ((24 * 60) / int(tm))), 3)
    print(one_day_percent)

    # 0.274 is the aproximation of 1 day value in %

    if current_percent >= 25.000 and current_percent <= (25.000 + one_day_percent):
        return twentyfive

    elif current_percent >= 50.000 and current_percent <= 50.274:
        return fifty

    elif current_percent >= 75.000 and current_percent <= 75.274:
        return seventyfive

    elif current_percent >= 99.726 and current_percent <= 100.00:
        return ninetynine

    elif current_percent >= 00.000 and current_percent <= 00.274:
        return cero

    else:
        pass
        # print(one_day_percent)