"""TimeFliesBar"""

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

# Import modules.

import tweepy
from tfb_keys import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

from tfb_calculus import minutesRemaining, minutesGone, totalMinutes #, currentYear
from tfb_progressbar import tfbProgressbar
# from tfb_data import tfbData
from tfb_milestones import tfbMilestone


#---------------------------------------------------------------------------#

# Authentication.

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#---------------------------------------------------------------------------#

# Progressbar execution.

bar: str
"""Progress bar representation."""
data: str
"""Progress data printing."""

if minutesRemaining > 0:

    print('Tweeting')

    bar = tfbProgressbar(totalMinutes, minutesGone)
    print('%s' % (bar))
    api.update_status(status = '%s' % (bar))

    # data = tfbData(minutesRemaining, currentYear)
    # print('%s' % (data))
    # api.update_status(status = '%s' % (data))

else:

    pass

#---------------------------------------------------------------------------#

# Milestones

milestone: str

milestone = tfbMilestone(totalMinutes, minutesGone)

if milestone == 0:
    print("No milestone today.")

elif milestone == 1:
    print("Today we have reached the 25% of the year.")
    api.update_status(status = '%s' % ("Today we have reached the 25% of the year."))

elif milestone == 2:
    print("Today we have reached the 50% of the year.")
    api.update_status(status = '%s' % ("Today we have reached the 50% of the year."))

elif milestone == 3:
    print("Today we have reached the 75% of the year.")
    api.update_status(status = '%s' % ("Today we have reached the 75% of the year."))

elif milestone == 4:
    print("Today we have reached the 90% of the year. Tomorrow will be a new year!")
    api.update_status(status = '%s' % ("Today we have reached the 90% of the year. Tomorrow will be a new year!"))

elif milestone == 5:
    print("Happy New Year! Everything starts again.")
    api.update_status(status = '%s' % ("Happy New Year! Everything starts again."))