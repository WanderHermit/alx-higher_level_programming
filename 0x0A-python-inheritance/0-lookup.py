#!/usr/bin/python3
"""Function that returns list of attributes and methods."""


def lookup(obj):
    """Return list of available attributes."""
    return(dir(obj))
