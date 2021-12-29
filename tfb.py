"""TimeFliesBar"""

# Contact.

# ovgpcomms@outlook.com

# ---------------------------------------------------------------------------#

# Imports.

from os import remove

import tweepy
from tfb_secrets import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

from tfb_graphic import graphic_bar as G
from tfb_milestones import milestone as M

from tfb_numbers import gone_minutes as gm
from tfb_numbers import total_minutes as tm
from tfb_numbers import current_day as cd
from tfb_numbers import current_day_upscaled as cd_u
from tfb_numbers import previous_day as pd


# ---------------------------------------------------------------------------#

# Authentication.

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# ---------------------------------------------------------------------------#

# Pass-trough variables.
""" Gone minutes. """
gm: int
"""" Total minutes. """
tm: int
""" Current day. """
cd: str
""" Current day upscaled. """
cd_u: str
"""" Previous day. """
pd: str
""" Name for the current image to save and publish. """
img_save: str
""" Name for the previous and now useless image. """
img_remove: str

# Regular variables.
""" Name for the previous and now useless image. """
milestone: str
img_save: str

# ---------------------------------------------------------------------------#

# Content to show:
# If there is a regular day with no milestone, print the progressbar.
# If a milestone happens this day, print the milestone and the progressbar.

milestone = M(tm, gm)  # Milestone execution.
img_save, img_remove = G(cd_u, gm, tm, cd, pd)  # Graphic execution.

if not milestone:

    if not img_save:
        pass

    else:
        #api.update_status(status = '%s' % (progress_bar))
        api.update_with_media(img_save, status="(Testing)")

        # Try to remove the image of the previous day (if exists)
        try:
            remove(img_remove)
        except FileNotFoundError:
            pass
        
else:
    api.update_status(status = '%s' % (milestone))
    api.update_with_media(img_save, status="(Testing)")

    # Try to remove the image of the previous day (if exists)
    try:
        remove(img_remove)
    except FileNotFoundError:
        pass
    