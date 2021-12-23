""" TIMEFLIESBAR GRAPHIC_PROGRESS BAR FUNCTION """

# Contact.

# ovgpcomms@outlook.com

# ---------------------------------------------------------------------------#

#import tweepy
#from tfb_secrets import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
#from os import remove
from calendar import isleap

#from tfb_numbers import gone_minutes as gm
#from tfb_numbers import total_minutes as tm
#from tfb_numbers import current_day as cd
#from tfb_numbers import current_day_upscaled as cd_u
#from tfb_numbers import previous_day as pd


# ---------------------------------------------------------------------------#

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


# ---------------------------------------------------------------------------#

# Authentication.

#auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
#api = tweepy.API(auth)

# ---------------------------------------------------------------------------#

# Graphic Progress Bar Function

def graphic_bar(cd_u, gm, tm, cd, pd):

    # Open base image and get drawing context
    if isleap:
        img = Image.open('./images/base_leap_upscaled.png').convert('RGB')
    else:
        img = Image.open('./images/base_upscaled.png').convert('RGB')

    draw = ImageDraw.Draw(img)
    write = ImageDraw.Draw(img)


    # Draw line at right end of progress bar and draw to the left
    color=(255,255,255)

    if isleap:
        draw.line((772,60 , (772 - int(cd_u)),60), fill=color, width=100) # 772 are the left margin 40 pixels + 732 pixels to reach the end of the bar and start from there
    else:
        draw.line((770,60 , (770 - int(cd_u)),60), fill=color, width=100) # 770 are the left margin 40 pixels + 730 pixels to reach the end of the bar and start from there


    # Print the percentage at bar center (202 pixel)
    fnt = ImageFont.truetype("./fonts/Cloude_Regular_1.02.ttf", 100)
    percent_left = ("{0:." + str(2) + "f}").format(100 - (100 * (gm / int(tm))))
    write.text((310, 10), "" + percent_left + "% Left", font=fnt, fill=(0, 0, 0))


    # Name resolution
    img_save = './to_publish/img_save_' + str(cd) + '.png'  # img_save of the current day (to publish)
    img_remove = './to_publish/img_save_' + str(pd) + '.png' # img_save of the previous day (to remove)

    # Save the image for the current day
    img.save(img_save)
    
    return img_save, img_remove