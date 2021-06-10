"""Timefliesbar fun_facts function."""

# Contact.

# timefliesbar@protonmail.com

# ---------------------------------------------------------------------------#

# Declaring variables.

tm: int
"""total_minutes from tfb_calculus."""
cy: int
"""current_year from tfb_calculus."""

decimals_in_minutes: int
"""Decimals to show on remaining minutes."""
fun_facts: str
"""Progress fun_facts printing."""

# ---------------------------------------------------------------------------#

# Obtain fun_facts.

def tfb_funfacts(rm, cy, decimals_in_minutes = 0):

    fun_facts = "There are still %s min remaining in %s." % (
        ("{0:." + str(decimals_in_minutes) + "0f}").format(rm), cy
    )

    return fun_facts