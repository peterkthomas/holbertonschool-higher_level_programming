#!/usr/bin/python3
"""
File: base.py
"""


class Base(object):
	"""Base: Definition for the Base class"""
	__nb_objects = 0

	def __init__(self, id=None):
		"""Initialization constructor"""
		if id is not None:
			self.id = id
		else:
			Base.__nb_objects += 1
			self.id = Base.__nb_objects
