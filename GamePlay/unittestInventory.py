#!/usr/bin/python
##################################
# File Name: unittestInventory.py
# Author: 	 Group 3
# Date: 	 11/10/2014
# Class:	 CS360
# Assignment:Jungle Jamboree
# Purpose: 	 unittest for inventory
##################################

import unittest
from Inventory import *
from Item import *

class testInventory(unittest.TestCase) :
	
	def setUp (self) :
		"""setup for the tests to run"""
		self.item1 = Item('mouse')
		self.item2 = Item('bat', 2, 5.00)
		self.testInventory = Inventory()
		
	def test_addItem (self) :
		self.testInventory.addItem(self.item1)
		
		self.assertIn(self.item1, self.testInventory._items)
	
	
	

