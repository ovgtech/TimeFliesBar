"""TimeFliesBar"""

# Contact.

# timefliesbar@protonmail.com

#---------------------------------------------------------------------------#

# Import modules.

# import tweepy
# from tfb_keys import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

from tfb_calculus import minutesRemaining, minutesGone, totalMinutes #, currentYear
from tfb_progressbar import tfbProgressbar as P
# from tfb_data import tfbData
from tfb_milestone import tfbMilestone as M


#---------------------------------------------------------------------------#

# Authentication.

# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
# api = tweepy.API(auth)

#---------------------------------------------------------------------------#

# Progressbar execution.

# bar: str
# """Progress bar representation."""
# data: str
# """Progress data printing."""

# if minutesRemaining > 0:

#     print('Tweeting')

#     bar = P(totalMinutes, minutesGone)
#     print('%s' % (bar))
#     # api.update_status(status = '%s' % (bar))

# else:

#     pass

#---------------------------------------------------------------------------#

# Final content to show: 
# If there is a regular day with no milestone, print the progressbar. If a milestone happens this day, print the corresponding message.

milestone: str
"""Returns milestone value."""
bar: str
"""Progress bar representation."""

milestone = M(totalMinutes, minutesGone) # Milestone execution.
bar = P(totalMinutes, minutesGone) # Progressbar execution.

if not milestone: # If milestone is returned empty, it means that no milestone happens today and the function pass.

    if minutesRemaining > 0:
        print('%s' % (bar))
        # api.update_status(status = '%s' % (bar))

    else:
        pass

else:
    print(milestone)
    # api.update_status(status = '%s' % (milestone))