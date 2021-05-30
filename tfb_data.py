"""Timefliesbar data function."""

# Contact.

# timefliesbar@protonmail.com

#---------------------------------------------------------------------------#

# Declaring variables.

remaining: int
"""Minutes remaining of the year."""
year: int
"""Current year."""
remainingDecimals: int
"""Decimals to show on remaining days."""
progressData: str
"""Progress data printing."""

#---------------------------------------------------------------------------#

# Obtain data.

def tfbData (remaining, year, remainingDecimals = 0):

	data = ('There are still %s min remaining in %s.' % (("{0:." + str(remainingDecimals) + "0f}").format(remaining), year))

	return(data)