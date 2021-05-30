""" Timefliesbar milestones function. """

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
""" Total minutes of the year. """
gone: int
""" Minutes elapsed of the year. """
percent: float
""" Percent elapsed of the year. """

#---------------------------------------------------------------------------#

# Obtain gone milestones.

def tfbMilestone (total, gone):

    percent = round((100 * (gone / int(total))), 3)
    
    if percent >= 25.00 and percent <= 25.275:
        milestone = 1

    elif percent >= 50.00 and percent <= 50.275:
        milestone = 2
    
    elif percent >= 75.00 and percent <= 75.275:
        milestone = 3

    elif percent >= 99.73 and percent <= 100.00:
        milestone = 4

    elif percent >= 00.00 and percent <= 00.275:
        milestone = 5

    else:
        milestone = 0

    return(milestone)