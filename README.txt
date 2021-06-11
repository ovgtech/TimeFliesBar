FLYING TIME TWITTER BOT

Purpose:
- This is my first project featuring Python3 and Twitter APIs. Also is kind of a reflection.
(Merely made with educational purposes).

How it works:
- It all focuses on a Twitter automatized account (called @timefliesbar) whose philosophy is "Time flies, make the most of it". Every day, at 12 o'clock in the morning, this profile shows us the percentage of the year that has elapsed in the shape of a reverse progress bar, unless that day is one of the symbolic moments in the course of the year (25%, 50%, 75%, 99%, 0%) when it shows a short message with no progress bar. 
- This project was devleoped with the intention to show how fast time goes, and trying to give the sensation of "lost" while showing a regresive bar instead a regular one. Everything to try to help us to relativize and understand the course of life a little bit better.
* This is quite an early version, and will support some interactions and/or better, more interesting facts or events.

INDEX

TFB.py                  - Main. Here This file is the one that calls the different functions when executed (according to a pre-established schedule) and converts the results in                             tweets. (Eventually, this functions will collapse in one single module).
TFB_CALCULUS.py         - This function calcultes necessary numbers related to dates, days, hours, minutes, etc. As well as conversions needed.
TFB_PROGRESSBAR.py      - This function generates the graphic representation of the progressbar.
TFB_MILESTONE.py        - This function gives information about representative numeric moments in the year progress.
TFB_FUNFACTS.py         - This last function expresses some interesting numbers, like minutes left in a year. (Currently not used)
