"""Timefliesbar progressbar function."""

# Contact.

# timefliesbar@protonmail.com

#---------------------------------------------------------------------------#

# Declaring variables.

total: int
"""Total minutes of the year."""
gone: int
"""Minutes elapsed of the year."""
percentDecimals: int
"""Decimals to show on percentages."""
length: int
"""Bar length."""
fill: str
"""Character for filled bar."""
notFill: str
"""Character for not filled bar."""
percentRight: int
"""Percentage of year gone."""
percentLeft: int
"""Percentage of year left"""
filledLength: int
"""Length for filled bar."""
notFilledLength: int
"""Length for not filled bar."""
bar: str
"""Progress bar representation."""
progressbar: str
"""Progress bar printing."""

#---------------------------------------------------------------------------#

# Obtain gone progressbar.

def tfbProgressbar (total, gone, percentDecimals = 2, length = 12, fill = '░', notFill = '▓'):

	percentRight = ("{0:." + str(percentDecimals) + "f}").format(100 - (100 * (gone / int(total))))
	percentLeft = ("{0:." + str(percentDecimals) + "f}").format(100 * (gone / int(total)))
	filledLength = int(length * gone // total)
	notFilledLength = int(length - filledLength)
	bar = fill * filledLength + notFill * notFilledLength
	progressbar = (f'{percentLeft}% Gone {bar} Left {percentRight}%')

	return(progressbar)
