"""Timefliesbar progressbar function."""

# Contact.

# timefliesbar@protonmail.com

# ---------------------------------------------------------------------------#

# Declaring variables.

tm: int
"""total_minutes from tfb_calculus."""
gm: int
"""gone_minutes from tfb_calculus."""

percent_decimals: int
"""Decimals to show on percentages."""
length: int
"""Bar length."""
fill: str
"""Character for filled bar."""
not_fill: str
"""Character for not filled bar."""
percent_right: int
"""Percentage of year gone."""
percent_left: int
"""Percentage of year left"""
filled_length: int
"""Length for filled bar."""
not_filled_length: int
"""Length for not filled bar."""
bar: str
"""Progress bar representation."""
progressbar: str
"""Progress bar printing."""

# ---------------------------------------------------------------------------#

# Obtain gone progressbar.


def progress_bar(tm, gm, percent_decimals = 2, length=12, fill = "░", not_fill = "▓"):

    percent_right = ("{0:." + str(percent_decimals) + "f}").format(100 - (100 * (gm / int(tm))))
    percent_left = ("{0:." + str(percent_decimals) + "f}").format(100 * (gm / int(tm)))
    filled_length = int(length * gm // tm)
    not_filled_length = int(length - filled_length)
    bar = fill * filled_length + not_fill * not_filled_length

    progressbar = f"{percent_left}% Gone {bar} Left {percent_right}%"

    return progressbar
