""" TimeFliesBar Graphic. """

# ---------------------------------------------------------------------------#
# Contact.
# ovgpcomms@outlook.com
# ---------------------------------------------------------------------------#


# Imports
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from calendar import isleap


# Variables
cy: str # Current year.
cd_u: str # Current day upscaled to fit 1:2 ratio.
cp_l: str # Current percent left.
cd: str # Current day.
pd: str # Previous day. 

img_save: str # Name for the current image to save and publish.
img_remove: str # Name for the previous and now useless image.


# Graphic Progress Bar Function
def drawbar(cy, cd_u, cp_l, cd, pd):

    # Open base image to get drawing context
    if isleap(cy):
        img = Image.open('./images/base_leap_upscaled.png').convert('RGB')
    elif not isleap(cy):
        img = Image.open('./images/base_upscaled.png').convert('RGB')
    else:
        pass

    draw = ImageDraw.Draw(img)
    write = ImageDraw.Draw(img)

    # Draw line at right end of progress bar and draw to the left
    color=(255,255,255)

    # Draw the current progress bar upscaled. Day to Pixel = 1:2
    if isleap(cy):
        draw.line((772,60 , (772 - int(cd_u)),60), fill=color, width=100) # 772 are the left margin 40 pixels + 732 pixels to reach the end of the bar and start from there
    elif not isleap(cy):
        draw.line((770,60 , (770 - int(cd_u)),60), fill=color, width=100) # 770 are the left margin 40 pixels + 730 pixels to reach the end of the bar and start from there
    else:
        pass

    # Print the percentage at bar center (202 pixel)
    fnt = ImageFont.truetype("./fonts/Cloude_Regular_1.02.ttf", 100)
    write.text((310, 10), "" + str(cp_l) + "% Left", font=fnt, fill=(0, 0, 0))

    # Name resolution
    img_save = './__graphics__/day_' + str(cd) + '.png'  # progressbar_day of the current day (to publish)
    img_remove = './__graphics__/day_' + str(pd) + '.png' # img_save of the previous day (to remove)

    # Save the image for the current day
    img.save(img_save)
    
    return img_save, img_remove