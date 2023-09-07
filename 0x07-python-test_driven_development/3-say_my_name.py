#!/usr/bin/python3
"""Make the code executable."""


def say_my_name(first_name, last_name=""):
    """A function that prints My name is <first name> <last name>

    first_name and last_name must be strings otherwise, raise a TypeError

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    return f"My name is {first_name} {last_name}"
