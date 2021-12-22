""" TIMEFLIESBAR GRAPHIC_PROGRESS BAR FUNCTION """

# Contact.

# ovgpcomms@outlook.com

# ---------------------------------------------------------------------------#

import tweepy
from tfb_secrets import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from os import name, remove
from calendar import isleap
import datetime

from tfb_numbers import gone_minutes as gm
from tfb_numbers import total_minutes as tm
from tfb_numbers import current_day as cd
from tfb_numbers import previous_day as pd


# ---------------------------------------------------------------------------#

""" Gone minutes. """
gm: int
"""" Total minutes. """
tm: int
""" Current day. """
cd: str
"""" Previous day. """
pd: str
""" Name for the current image to save and publish. """
name_save: str
""" Name for the previous and now useless image. """
name_delete: str


# ---------------------------------------------------------------------------#

# Authentication.

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# ---------------------------------------------------------------------------#


#def graphic_bar(gm, tm, cd, pd):
    #return name_save

# Open template and get drawing context
if isleap:
    img = Image.open('./images/base_leap.png').convert('RGB')
else:
    img = Image.open('./images/base.png').convert('RGB')

draw = ImageDraw.Draw(img)
write = ImageDraw.Draw(img)


# Draw line at right end of progress bar
color=(255,255,255)

if isleap:
    draw.line((385,30 , (385 - int(cd)),30), fill=color, width=50) # 385 are the left margin pixels + 366 pixels to reach the end of the bar and start from there
else:
    draw.line((384,30 , (384 - int(cd)),30), fill=color, width=50) # 384 are the left margin pixels + 365 pixels to reach the end of the bar and start from there


# Print the percentage at bar center (202 pixel)
fnt = ImageFont.truetype("./fonts/Cloude_Regular_1.02.ttf", 50)
percent_left = ("{0:." + str(2) + "f}").format(100 - (100 * (gm / int(tm))))
write.text((155, 5), "" + percent_left + "% Left", font=fnt, fill=(0, 0, 0))


# Name resolution
name_save = './to_publish/test' + str(cd) + '.png'
name_delete = './to_publish/test' + str(pd) + '.png'


# Saving current to publish and deleting previous (if exists)


try:
    img.save(name_save)
    api.update_with_media(name_save, status="")
    try:
        remove(name_delete)
    except FileNotFoundError:
        exit()
except FileNotFoundError:
    exit()

""" 
try:
    remove(name_save)
except FileNotFoundError:
    img.save(name_save)
    api.simple_upload(status = '%s' % (img.save))

    try:
        remove(name_delete)
    except FileNotFoundError:
        exit()
    exit() 
"""