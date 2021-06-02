""" Timefliesbar milestones function. """

# Contact.

# timefliesbar@protonmail.com

#---------------------------------------------------------------------------#

# Declaring variables.

total: int
""" Total minutes of the year. """
gone: int
""" Minutes elapsed of the year. """
percent: float
""" Percent elapsed of the year. """

#---------------------------------------------------------------------------#

# Obtain milestones.

def tfbMilestone (total, gone):

    percent = round((100 * (gone / int(total))), 3)
    
    if percent >= 25.000 and percent <= 25.275:
        milestone = 1

    elif percent >= 50.000 and percent <= 50.275:
        milestone = 2
    
    elif percent >= 75.000 and percent <= 75.275:
        milestone = 3

    elif percent >= 99.730 and percent <= 100.00:
        milestone = 4

    elif percent >= 00.000 and percent <= 00.275:
        milestone = 5

    else:
        milestone = 0

    return(milestone)