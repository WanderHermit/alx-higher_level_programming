#!/usr/bin/python3
"""

contains the MyList class.
"""


class MyList(list):
    """Print a sorted list."""

    def print_sorted(self):
        """Prints a list in a sorted order."""
        print(sorted(self))
