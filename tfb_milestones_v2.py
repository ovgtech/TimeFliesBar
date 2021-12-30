""" TimeFliesBar Milestones v2. """

# ---------------------------------------------------------------------------#
# Contact.
# ovgpcomms@outlook.com
# ---------------------------------------------------------------------------#


# Variables.
mid: str # Half year message.
last: str # Last day of the year message.
first: str # First day of the year message.


# Message intended to show
mid = "Today we are reaching the 50% of the year."
last = "Today we are reaching the 100% of the year.\nTomorrow will be a new year!"
first = "Happy New Year! Everything starts again."


# Function
def milestones(cd, hy, td):

    if cd == 1:
        return first
    elif cd == hy:
        return mid
    elif cd == td:
        return last
    else:
        pass