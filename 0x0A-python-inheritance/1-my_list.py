#!/usr/bin/python3
"""Class that inherits from a parent class List."""


class MyList(list):
	"""Print list in a sorterd ascending order."""

	def print_sorted(self):
		"""Prints the list."""
		print(sorted(self))
