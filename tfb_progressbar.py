""" TIMEFLIESBAR PROGRESS_BAR FUNCTION """

# Contact.

# ovgpcomms@outlook.com

# ---------------------------------------------------------------------------#

# Pass-trough variables.

tm: int
""" total_minutes from tfb_calculus. """
gm: int
""" gone_minutes from tfb_calculus. """

# Regular variables.

percent_decimals: int
""" Decimals to show on percentages. """
bar_length: int
""" Bar length. """
bar_fill: str
""" Character for filled bar. """
not_fill: str
""" Character for not filled bar. """
percent_right: int
""" Percentage of year gone. """
percent_left: int
""" Percentage of year left. """
filled_length: int
""" Length for filled bar. """
not_filled_length: int
""" Length for not filled bar. """
bar: str
""" Progress bar representation. """
progressbar: str
""" Progress bar printing. """

# ---------------------------------------------------------------------------#

# Obtain gone progressbar.

def progress_bar(tm, gm, percent_decimals = 2, bar_length=12, bar_fill = "░", not_fill = "▓"):

    percent_right = ("{0:." + str(percent_decimals) + "f}").format(100 - (100 * (gm / int(tm))))
    percent_left = ("{0:." + str(percent_decimals) + "f}").format(100 * (gm / int(tm)))
    filled_length = int(bar_length * gm // tm)
    not_filled_length = int(bar_length - filled_length)
    bar = bar_fill * filled_length + not_fill * not_filled_length

    progressbar = f"{percent_left}% Gone {bar} Left {percent_right}%"

    return progressbar
