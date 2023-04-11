#!/usr/bin/python3
"""Check if object is instance of an inherited class."""


def inherits_from(obj, a_class):
	"""Function to check the code.

	Args:
		obj (any): The object to check.
		a_class (any): The class to check with.

	Returns:
		if obj is an instance of an inherited class - True.
		Otherwise - False.
	"""
	if issubclass(type(obj), a_class) and type(obj) != a_class:
		return True
	return False
