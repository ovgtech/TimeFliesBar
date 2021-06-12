""" Timefliesbar milestone function. """

# Contact.

# timefliesbar@protonmail.com

# ---------------------------------------------------------------------------#

# Declaring variables.

tm: int
"""total_minutes from tfb_calculus."""
gm: int
"""gone_minutes from tfb_calculus."""

percent: float
""" Elapsed percent of the year. """

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

# ---------------------------------------------------------------------------#

# Obtain milestones and the message intended to show

twentyfive = "Today we have reached the 25% of the year."
fifty = "Today we have reached the 50% of the year."
seventyfive = "Today we have reached the 75% of the year."
ninetynine = "Today we have reached the 99% of the year. Tomorrow will be a new year!"
cero = "Happy New Year! Everything starts again."


def tfb_milestone(tm, gm):

    percent = round((100 * (gm / int(tm))), 3)

    if percent >= 25.000 and percent <= 25.275:
        return twentyfive

    elif percent >= 50.000 and percent <= 50.275:
        return fifty

    elif percent >= 75.000 and percent <= 75.275:
        return seventyfive

    elif percent >= 99.730 and percent <= 100.00:
        return ninetynine

    elif percent >= 00.000 and percent <= 00.275:
        return cero

    else:
        pass
