#!/usr/bin/python
##################################
# File Name: Person.py
# Author: 	 Group 3
# Date: 	 11/10/2014
# Class:	 CS360
# Assignment:Jungle Jamboree
# Purpose: 	 Person class
##################################

from Inventory import *

"""
The Person Module
"""


class Person :
	
	def __init__ (self, name) :
		""" Initializes a person which has a name and an inventory """
		self._name = name
		#Stats
		#Special Effects
		
	def __str__ (self) :
		""" what is returned if str() with a person passed in """
		return self._name # May not need
		
	def getName (self) :
		"""returns Name """
		return self._name
		
