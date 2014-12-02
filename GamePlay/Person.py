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
	
	def __init__ (self, name, healthEffect = 0) :
		""" Initializes a person which has a name and an inventory """
		self._name = name
		self._health = 100
		self._healthEffect = healthEffect
		#Stats
		#Special Effects
		
	def __str__ (self) :
		""" what is returned if str() with a person passed in """
		return self._name # May not need
		
	def getName (self) :
		"""returns Name """
		return self._name
		
	def getHealth (self) :
		return self._health
		
	def updateHealth (self) :
		if self._health + self._healthEffect > 0 :
			self._health += self._healthEffect
		elif self._health + self._healthEffect <= 0 :
			self._health = 0
			self._healthEffect = 0
			
	def updateHealthEffect (self, value) :
		self._healthEffect += value
		
	def setHealthEffect (self, value) :
		self._healthEffect = value			
		
	def DeadPerson (self) :
		return (self._health <= 0)
		
		
