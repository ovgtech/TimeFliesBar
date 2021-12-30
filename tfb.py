""" TimeFliesBar Main. """

# ---------------------------------------------------------------------------#
# Contact.
# ovgpcomms@outlook.com
# ---------------------------------------------------------------------------#


# Imports.
from os import remove

import tweepy
from tfb_secrets import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

from tfb_drawbar import drawbar as D
from tfb_milestones_v2 import milestones as M

from tfb_numbers_v2 import current_year as cy
from tfb_numbers_v2 import half_year as hy
from tfb_numbers_v2 import previous_day as pd
from tfb_numbers_v2 import current_day as cd
from tfb_numbers_v2 import current_day_upscaled as cd_u
from tfb_numbers_v2 import total_days as td
from tfb_numbers_v2 import current_percent_left as cp_l
from tfb_numbers_v2 import current_percent as cp


# Authentication.
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


# Variables.
cd: str # Current day.
hy: str # Half of current year.
td: str # Total days in current year.

cy: str # Current year.
cd_u: str # Current day upscaled to fit 1:2 Day to Pixel ratio for the drawbar.
cp_l: str # Current percent left of the current year.
pd: str # Previous day.

milestones: str # Milestone function value.
img_save: str # Name for the current image to save and publish. 
img_remove: str # Name for the previous and now useless image. 


# Content to show:
#   - If there is a regular day with no milestone, print the progressbar.
#   - If a milestone happens this day, print the milestone and the progressbar.

milestones = M(cd, hy, td) # Milestones v2.
img_save, img_remove = D(cy, cd_u, cp_l, cd, pd)  # Drawing Progress Bar.

if not milestones:
    if not img_save:
        pass
    
    else:
        api.update_with_media(img_save, status="")
        try:
            remove(img_remove) # Try to remove the image of the previous day (if exists)
        except FileNotFoundError:
            pass

else:
    api.update_with_media(img_save, status="")
    api.update_status(status = '%s' % (milestones)) 
    try:
        remove(img_remove) # Try to remove the image of the previous day (if exists)
    except FileNotFoundError:
        pass