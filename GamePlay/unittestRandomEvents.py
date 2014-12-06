#!/usr/bin/python
##################################
# File Name: unittestRandomEvents.py
# Author: 	 Group 3
# Date: 	 11/10/2014
# Class:	 CS360
# Assignment:Jungle Jamboree
# Purpose: 	 unittest for RandomEvents class
##################################

import unittest
from random import *
from RandomEvents import *

class testRandomEvents(unittest.TestCase) :
	
	def setUp (self) :
		""" sets up a party and the random events """
		self.events = RandomEvents()
		self.party = Party()
		self.party.updateFood(100)
		
	def test_randNum (self) :
		""" tests that the random number generated is between 0 and 100 inclusive """
		self.events.randNum()
		self.assertIn(self.events.getRandNum(), range(0,100))
		
	def test_eventFoundFood (self) :
		""" test that the correct amount of food is added to the party  """
		self.events.setRandNum(70)
		originalFood = self.party.getFood()
		
		self.events.eventFoundFood(self.party)
		
		self.assertEqual(self.party.getFood(), originalFood + 35)
		
	def test_eventLostFood (self) :
		""" test that the correct amount of food is removed to the party  """
		self.events.setRandNum(80)
		originalFood = self.party.getFood()
		
		self.events.eventLostFood(self.party)
		
		self.assertEqual(self.party.getFood(), originalFood - 40)
		
"""
suite = unittest.TestLoader().loadTestsFromTestCase(testRandomEvents)
unittest.TextTestRunner(verbosity=2).run(suite)
"""
