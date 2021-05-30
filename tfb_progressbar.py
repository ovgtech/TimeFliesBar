"""Timefliesbar progressbar function."""

# MIT License

# Copyright (c) 2020 melancholicbot

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#---------------------------------------------------------------------------#

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
