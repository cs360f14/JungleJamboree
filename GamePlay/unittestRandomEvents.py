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
		self.events = RandomEvents()
		self.party = Party()
		
	def test_setRandNum (self)
		self.events.setRandNum()
		self.assertIn(self.events.getRandNum(), range(0,100)
