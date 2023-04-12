#!/usr/bin/python3
"""Check if object is an instance of a class that is inherited."""


def is_kind_of_class(obj, a_class):
    """Class with two instances.

    Args:
        obj (any): The object to be checked.
        a_class (any): Match with the obj.

    Return:
        if obj is instance or an inherited instance of a class - True.
        Else - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
