#!/usr/bin/python3
"""Define a class BaseGeometry based on Task 6."""


class BaseGeometry:
    """Represent BaseGeometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Args:
               value (int): The value to validate
               name (str): Always a string
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if type(value) <= 0:
            raise ValueError("{} must be greater than 0".format(name))
