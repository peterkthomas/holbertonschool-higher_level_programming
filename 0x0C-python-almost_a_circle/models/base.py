#!/usr/bin/python3
"""
File: base.py
"""
import json

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
	
	@staticmethod
	def to_json_string(list_dictionaries):
		"""returns JSON dictionary"""
		if list_dictionaries is None or len(list_dictionaries) == 0:
			return "[]"
		return json.dumps(list_dictionaries)