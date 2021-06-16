"""TimeFliesBar"""

# Contact.

# ovgpcomms@outlook.com

# ---------------------------------------------------------------------------#

# Import functions.

from tfb_progressbar import progress_bar as P
from tfb_milestones import milestone as M

# Import variables.

from tfb_numbers import gone_minutes as gm
from tfb_numbers import total_minutes as tm

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
        print(progress_bar)

else:
    print(milestone)
    print(progress_bar)