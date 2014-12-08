#!/usr/bin/python
##################################
# File Name: unittestInventory.py
# Author: 	 Group 3
# Date: 	 11/10/2014
# Project:	 Jungle Jamboree
# Purpose: 	 unittest for inventory
##################################

import unittest
from Inventory import *
from Item import *

"""
The Unittest for Inventory Module
"""

# tests not necessary for IO related functions

class testInventory(unittest.TestCase) :
	
	def setUp (self) :
		"""setup for the tests to run"""
		self.item1 = Item('mouse')
		self.item2 = Item('bat', 2, 5.00)
		self.testInventory = Inventory()
		
	def test_addItem (self) :
		""" tests that an item is added to the inventory correctly """
		self.testInventory.addItem(self.item1)
		
		self.assertIn(self.item1, self.testInventory._items)
	
	
	

