from PIL import Image
from PIL import ImageDraw
from os import remove

import datetime

current_date: str
current_day: str
previous_day: str
name_save: str
name_delete: str

# Doing the numbers
current_date = datetime.datetime.now()
current_day = current_date.strftime("%j")
previous_day = int(current_day) - 1


#  Generating the ProgressBar
# Open template and get drawing context
img = Image.open('base.png').convert('RGB')
draw = ImageDraw.Draw(img)

# Cyan-ish fill colour
color=(98,211,245)

# Draw circle at right end of progress bar
x, y, diam = 254, 8, 34
draw.ellipse([x,y,x+diam,y+diam], fill=color)

# Flood-fill from extreme left of progress bar area to behind circle
ImageDraw.floodfill(img, xy=(14,24), value=color, thresh=40)

# Name resolution
name_save = 'test' + str(current_day) + '.png'
name_delete = 'test' + str(previous_day) + '.png'

# Saving current to publish and deleting previous (if exists)
img.save(name_save)
try:
    remove(name_delete)
except FileNotFoundError:
    exit()


