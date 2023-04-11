#!/usr/bin/python3
"""Class that inherits from another class."""


class MyList(list):
    """Print a sorted list."""

    def print_sorted(self):
        """Prints a list in a sorted order."""
        print(sorted(self))
