#!/usr/bin/python
##################################
# File Name: RandomEvents.py
# Author: 	 Group 3
# Date: 	 11/10/2014
# Class:	 CS360
# Assignment:Jungle Jamboree
# Purpose: 	 RandomEvents class
##################################

from random import *
#from random import randint

"""
The Random Events Module
"""

class RandomEvents :
	
	noEventRange = range(0,50)
	goodEventRange = range(50,75)
	badEventRange = range(75,100)
	
	def __init__(self) :
		"""initializes the random events"""
		#later may want to pass in something that effects the probability of certain events
		self._rand = Random()
		self._seed = self._rand.seed()
		self._randNum = self._rand.randint(0,100)
		
	def getRandNum (self) :
		""" returns the randomly generated number """
		return self._randNum
		
	def setRandNum (self) :
		""" generates a new random number """
		self._randNum = self._rand.randint(0,100)
	
	def testEvent (self) :
		""" based on the random number, determine the event """
		if self._randNum in noEventRange :
			noEvent()
			
		elif self._randNum in goodEventRange :
			upperEventGood()
			
		elif self._randNum in badEventRange :
			upperEventBad()
		
		
	def noEvent (self) :
		""" no event will happen """
		pass
	
	def upperEventGood (self) :
		""" the possible good events """
		pass
	
	def upperEventBad (self) :
		""" the possible bad events """
		#if the 100 was picked...
		pass


test = RandomEvents()
print test.getRandNum()
test.setRandNum ()
print test.getRandNum()
test.setRandNum ()
print test.getRandNum()
test.setRandNum ()
print test.getRandNum()
test.setRandNum ()
print test.getRandNum()
test.setRandNum ()
print test.getRandNum()
test.setRandNum ()
print test.getRandNum()
test.setRandNum ()
print test.getRandNum()

