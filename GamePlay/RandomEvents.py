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
from Party import *

#from random import randint

"""
The Random Events Module
"""

class RandomEvents :

	
	def __init__(self) :
		"""initializes the random events"""
		#later may want to pass in something that effects the probability of certain events
		self._rand = Random()
		self._seed = self._rand.seed()
		self._randNum = self._rand.randint(0,100)
		self._noEventRange = range(0,50)
		self._goodEventRange = range(50,75)
		self._badEventRange = range(75,100)
		
	def getRandNum (self) :
		""" returns the randomly generated number """
		return self._randNum
		
	def setRandNum (self) :
		""" generates a new random number """
		self._randNum = self._rand.randint(0,100)
	
	def event (self, party) :
		""" based on the random number, determine the event """
		if self._randNum in self._noEventRange :
			self.noEvent()
			
		elif self._randNum in self._goodEventRange :
			self.upperEventGood(party)
			
		elif self._randNum in self._badEventRange :
			self.upperEventBad(party)
		
	def noEvent (self) :
		""" no event will happen """
		print("No Event")
	
	def upperEventGood (self, party) :
		""" the possible good events """
		print("Good Event")
		self.eventFoundFood(party)
	
	def upperEventBad (self, party) :
		""" the possible bad events """
		#if the 100 was picked...
		print("Bad Event")
		self.eventLostFood(party)
		
		
	# good events! -----------------------------------------------------
	
	def eventFoundFood(self, party) :
		""" party randomly finds food """
		print "Found ", self._randNum/ 2, " Food"
		print "Party had ",	party.getFood(), "food"
		party.updateFood((self._randNum / 2))
		print "Party now has", party.getFood(), "food"
		
		# other good events:

	# bad events! ------------------------------------------------------

	def eventLostFood(self, party) :
		""" party randomly loses food """
		foodAmount = self._randNum/ 2
		print "Lost ", foodAmount, " Food"
		print "Party had ",	party.getFood(), "food"
		
		if party.getFood() - foodAmount <= 0 :
			party.updateFood(-(party.getFood()))
		else :
			party.updateFood(-(self._randNum / 2))
			
		print "Party now has", party.getFood(), "food"
		if party.getFood() == 0 :
			print "Party is dead"		#stop game loop
			
		# other bad events (got a disease, lost the machete, broke an arm)

party = Party()
test = RandomEvents()

for x in range(1,5) :
	print "Turn: ", x
	print "Random Number: ", test.getRandNum()
	test.event(party)
	test.setRandNum ()
	print ""
