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
		"""Sets up a party 
		for x in range(self._size) :
			self._party.append(Person(self.getName())) """
			
		self._party.append(Person("Iowa Smith"))
		self._party.append(Person("Dorthy"))
		self._party.append(Person("Larry Fills"))
		self._party.append(Person("Laureen Kraft"))
		self._party.append(Person("Jeb the Forest Man"))
		
	
	def getName (self) :
		""" Get a name for each party person"""
		name = raw_input("Enter Name: ")
		return name		
		
	def getSize (self) :
		count = 0
		for person in self.generatePerson (): 
			if not person.deadPerson () :
				count += 1
		return count		
		
	def getPartyMember(self, num) :
		""" returns the person in the party """
		return self._party[num]
		
	def displayParty (self) :
		for person in self.generatePerson() :
			person.displayPerson()
		
	def generatePerson (self) :
		""" a generator to iterate through the list of persons"""		
		for person in self._party :
			yield person	
			
	def setPartyHealth (self, num) : 
		""" sets health of all party members to the number passed in """
		for person in self.generatePerson () :
			person.setHealth (num)	
	
	def incrPartyHealth (self, num) :
		""" increments health of all party members to the number passed in """
		for person in self.generatePerson () :
			if not person.deadPerson () :
				person.incrHealth (num)	
			
	def decrPartyHealth (self, num) :
		""" decrements health of all party members to the number passed in """
		for person in self.generatePerson () :
			if not person.deadPerson () :
				person.decrHealth (num)	
			
	def updateHealth (self) :
		""" updates health of all party members to the number passed in """
		for person in self.generatePerson () :
			if not person.deadPerson () :
				person.updateHealth ()
			
	def updatePartyHealthEffect (self, num) :
		""" updates the health effect of all party members 
		to the number passed in """
		for person in self.generatePerson() :
			person.updateHealthEffect(num)
			
	def death (self) :
		"""sets every person who is dead to a Dead health title"""
		for person in self.generatePerson () :
			if person.deadPerson () :
				person.setHealthTitle ("Dead")
				
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
		
	def checkPartyDead(self):
		
		for person in self.generatePerson () :
			if not person.deadPerson () :
				return False
		return True
	
	def setDead(self) :
		self._party[:] = []
		self._size = 0
					
