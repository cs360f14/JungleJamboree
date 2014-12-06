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
		self._healthTitle = "Healthy"
		#Stats
		#Special Effects
		
	def __str__ (self) :
		""" what is returned if str() with a person passed in """
		return self._name # May not need
	
	def getName (self) :
		"""returns Name """
		return self._name
	
	def getHealth (self) :
		""" returns health """
		return self._health
		
	def getHealthEffect (self) :
		""" returns current health effect"""
		return self._healthEffect
	
	def getHealthTitle (self) :
		""" returns health title """ 
		return self._healthTitle
		
	def setHealthTitle (self, title) :
		""" sets the health title to the title passed in """ 
		self._healthTitle = title
		
	def updateHealtTitle (self, title) :
		""" updates the health title by adding the title passed in to the current health title """ 
		self._healthTitle = self._healthTitle + title
	
	def displayPerson (self) :
		""" displays the person's name and health """
		print self.getName()
		print "Health: ", self.getHealth()
		print "Status: ", self.getHealthTitle()
		print "Health Effect: ", self._healthEffect, "\n"
	
	def setHealth (self, num) :
		""" sets health to the num passed in """
		self._health = num
		
	def decrHealth (self, num) :
		""" decrements health by the num passed in """
		if self._health - num <= 0 :
			self._health = 0
			#person is now dead...
		else :
			self._health -= num
	
	def incrHealth (self, num) :
		""" increments health by the num passed in """
		if self._health + num >= 100 :
			self._health = 100
		else :
			self._health += num
	
	def updateHealth (self) :
		""" updates the person's health, taking into account the current health effect """
		if self._health + self._healthEffect > 100 :
			self._health = 100
		elif self._health + self._healthEffect > 0 :
			self._health += self._healthEffect
		elif self._health + self._healthEffect <= 0 :
			self._health = 0
			self._healthEffect = 0
			
	def updateHealthEffect (self, value) :
		""" increments the health effect by the value passed in """
		self._healthEffect += value
		
	def setHealthEffect (self, value) :
		""" sets the health effect to the value passed in """
		self._healthEffect = value			
		
	def deadPerson (self) :
		return (self._health <= 0)
		
		
