#!/usr/bin/python
##################################
# File Name: unittestParty.py
# Author: 	 Group 3
# Date: 	 11/10/2014
# Class:	 CS360
# Assignment:Jungle Jamboree
# Purpose: 	 unittest for Party module
##################################

import unittest
from Party import *
"""
The Unittest for Party Module
"""

class testParty(unittest.TestCase) :
	
	def setUp (self) :
		""" sets up a party and 5 people for a party"""
		self.party = Party ()
		self.person1 = Person("Black Knight", -99)
		self.person2 = Person("Knights who say Ni", -1)
		self.person3 = Person("The Colonel", -5)
		self.person4 = Person("King Arthur", 5)
		self.person5 = Person("Brian")
		
	def test_addPerson (self) :
		""" tests that add a person works correctly"""
		self.party.addPerson(self.person1)
		isIn = False
		
		for person in self.party.generatePerson() :
			if person.getName() == self.person1.getName () :
				isIn = True
				
		self.assertTrue (isIn)	
		
	def test_removePerson (self) :
		""" tests that person2 is removed correctly and person1 is 
		still in the party"""
		self.party.addPerson(self.person1)
		self.party.addPerson(self.person2)
		Person1isIn = False
		Person2isIn = False
				
				
		self.person2.setHealthEffect (-100)
		self.person2.updateHealth ()		
		self.party.Death()
		
				
		for person in self.party.generatePerson() :
			if person.getName() == self.person1.getName () :
				Person1isIn = True
				
		for person in self.party.generatePerson() :
			if person.getName() == self.person2.getName () :
				Person2isIn = True		
				
		self.assertTrue (Person1isIn)		
		self.assertFalse (Person2isIn)
		
	def test_UpdateHealth (self) :
		"""tests that the parties health is updated correctly"""	
		self.party.updateHealth ()
		for person in self.party.generatePerson () :
			self.assertEqual (person.getHealth (), \
			100 + person.getHealthEffect ())
		
		
#not going to test getInventory, removeFromInventory, setInventory,
#getSize, getName, or setupParty or generatePerson
#Since these are all either functions that just call a single function
#or IO related or get/set fnctions
	
				
