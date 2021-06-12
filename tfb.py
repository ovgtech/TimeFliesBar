"""TimeFliesBar"""

# Contact.

# timefliesbar@protonmail.com

# ---------------------------------------------------------------------------#

# Import.

import tweepy
from tfb_secrets import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

from tfb_progressbar import progress_bar as P
from tfb_milestones import milestone as M

from tfb_numbers import gone_minutes as gm
from tfb_numbers import total_minutes as tm

# ---------------------------------------------------------------------------#

# Authentication.

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# ---------------------------------------------------------------------------#

# Content to show:
# If there is a regular day with no milestone, print the progressbar. If a milestone happens this day, print the corresponding message.

milestone: str
"""Returns milestone value."""
progress_bar: str
"""Progress bar representation."""

milestone = M(tm, gm)  # Milestone execution.
progress_bar = P(tm, gm)  # Progressbar execution.

if not milestone:  # If milestone is returned empty, it means that no milestone happens today and the function pass.

    if not progress_bar:  # If bar is not returning anything, pass.
        pass

    else:
        print(progress_bar)
        api.update_status(status = '%s' % (progress_bar))

else:
    print(milestone)
    api.update_status(status = '%s' % (milestone))