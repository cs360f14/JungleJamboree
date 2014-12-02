#!/usr/bin/python
##################################
# File Name: unittestPerson.py
# Author: 	 Group 3
# Date: 	 12/1/2014
# Class:	 CS360
# Assignment:Jungle Jamboree
# Purpose: 	 unittest for Person module
##################################

import unittest
from Person import *
"""
The Unittest for Person Module
"""

class testPerson(unittest.TestCase) :
	
	def setUp (self) :
		""" sets up two people"""
		self.person1 = Person("Black Knight", -100)
		self.healthEffect = -5
		self.person2 = Person("Knights who say Ni", self.healthEffect)
		self.person3 = Person("King Arthur")
		self.healthEffect2 = -55
		self.person3.setHealthEffect (self.healthEffect2)


	def test_UpdateHealthAt0 (self) :
		"""tests that updating the health of person works correctly"""
		self.person2.updateHealth ()
		self.assertEqual(self.person2.getHealth(), \
		100 + self.healthEffect)
	
	def test_UpdateHealthLessThan0 (self) :
		"""tests that updating the health of person works correctly"""
		self.person3.updateHealth ()
		self.assertEqual(self.person3.getHealth(), \
		100 + self.healthEffect2)
		self.person3.updateHealth ()
		self.assertEqual(self.person3.getHealth(), 0)
		
	def test_DeadPersonTrue (self) :
		""" tests that checking if a person is dead works correctly"""
		self.person1.updateHealth ()
		self.assertEqual(self.person1.getHealth(), 0)
		self.assertTrue(self.person1.DeadPerson())
		
	def test_DeadPersonFalse (self) :
		""" tests that checking if a person is dead works correctly"""
		self.person1.updateHealth ()
		self.assertFalse(self.person2.DeadPerson())
