"""TimeFliesBar"""

# Contact.

# ovgpcomms@outlook.com

# ---------------------------------------------------------------------------#

# Imports.

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

# Pass-trough variables.

gm: int
tm: int

# Regular variables.

milestone: str
progress_bar: str

# ---------------------------------------------------------------------------#

# Content to show:
# If there is a regular day with no milestone, print the progressbar.
# If a milestone happens this day, print the milestone and the progressbar.

milestone = M(tm, gm)  # Milestone execution.
progress_bar = P(tm, gm)  # Progressbar execution.

if not milestone:

    if not progress_bar:
        pass

    else:
        api.update_status(status = '%s' % (progress_bar))

else:
    api.update_status(status = '%s' % (milestone))
    api.update_status(status = '%s' % (progress_bar))