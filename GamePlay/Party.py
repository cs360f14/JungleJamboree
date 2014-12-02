 #!/usr/bin/python
##################################
# File Name: Party.py
# Author: 	 Group 3
# Date: 	 11/10/2014
# Class:	 CS360
# Assignment:Jungle Jamboree
# Purpose: 	 Party to class to handle a group of persons
##################################

from Person import *
from Inventory import *

"""
The Party Module
"""


class Party :
	
	def __init__ (self) :
		""" initializes the size then creates a
			party list and inventory"""
		self._size = 5 # may be subject to change
		self._party = []
		self._backpack = Inventory()
		
	def setUpParty (self) :
		"""Sets up a party """
		for x in range(self._size) :
			self._party.append(Person(self.getName())) 
	
	def getName (self) :
		""" Get a name for each party person"""
		name = raw_input("Enter Name: ")
		return name		
		
	def getSize (self) :
		return self._size	
		
	def generatePerson (self) :
		""" a generator to iterate through the list of persons"""		
		for person in self._party :
			yield person	
			
	def updateHealth (self) :
		for person in self.generatePerson () :
			person.updateHealth ()		
			
	def Death (self) :
		for person in self.generatePerson () :
			if person.DeadPerson () :
				self._party.remove(person)
				self._size -= 1
				
	def setInventory (self, inventory) :
		"""sets the backpack to the passed in value """
		self._backpack = inventory
		
	def addToInventory (self, item) :
		"""adds an item to the backpack """
		self._backpack.addItem (item)
	
	def removeFromInventory (self, item) :
		"""removes an item from the backpack """
		self._backpack.removeItem (item)
		
	def getCash (self) :
		""" returns the amount of cash in the backpack"""
		return self._backpack.getCash()	
			
	def updateCash (self, num) :
		""" updates the amount of cash in the backpack"""
		self._backpack.updateCash(num)		
			
	def getFood (self) :
		""" returns the amount of cash in the backpack"""
		return self._backpack.getFood()	
			
	def updateFood (self, num) :
		""" update the amount of food in the backpack"""
		self._backpack.updateFood(num)	
		
	def getInventory (self) :
		""" returns backpack or the inventory of the party"""
		return self._backpack	
		
	def addPerson (self, person) :
		""" adds a person to the party""" #currently for unittest
		self._party.append(person)
		

			
			
	
					
