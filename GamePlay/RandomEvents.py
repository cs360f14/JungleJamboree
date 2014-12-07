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
import pygame 
from pygame.locals import *
import sys

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
		self._badEventRange = range(75,101)
		
	def getRandNum (self) :
		""" returns the randomly generated number """
		return self._randNum
		
	def randNum (self) :
		""" generates a new random number """
		self._randNum = self._rand.randint(0,100)
		
	def setRandNum (self, num) : 
		""" force random num - to force certain events """
		self._randNum = num
		
	def forageEvent (self, party, display) :
		randNum = self._rand.randint(0, 100)
		foodForaged = 0
		
		if randNum in range (0,85) :
			foodForaged = self._rand.randint(0,6)
		elif randNum in range (85,100) :
			foodForaged = 5 * party.getSize()
			
		print foodForaged, "food foraged."
		party.updateFood(foodForaged)
	
	def event (self, party, display) :
		""" based on the random number, determine the event """
		if self._randNum in self._noEventRange :
			self.noEvent(display)
			
		elif self._randNum in self._goodEventRange :
			self.upperEventGood(party, display)
			
		elif self._randNum in self._badEventRange :
			self.upperEventBad(party, display)
		
	def noEvent (self, display) :
		""" no event will happen """
		
		myFont = pygame.font.Font('freesansbold.ttf', 30) # figure out different way
		
		noEvent = myFont.render("No Event" , 1, (0,0,0))
		display.blit(noEvent, (350, 300))
	
	def upperEventGood (self, party, display) : #50-75
		""" the possible good events """
#		print("Something good happened!")
		
		#have inner ranges for different good events...
		
		if self._randNum in range(50,60) :
			self.eventFoundFood(party, display)
		elif self._randNum in range(60, 75):
			self.eventFoundGoodHerb(party, display)
	
	def upperEventBad (self, party, display) : #75-100
		""" the possible bad events """
		#have inner ranges for different bad events
		
		
#		print("Oooo... something bad happened...")
		
		if self._randNum in range(75,80) :
			self.eventLostFood(party, display)
		elif self._randNum in range(80, 85):
			self.eventFoundBadHerb(party, display)
		elif self._randNum in range (85, 93) :
			self.eventBrokeArm(party, display)
		elif self._randNum in range (93, 100) :
			self.eventBrokeLeg(party, display)
		elif self._randNum == 100 :
			self.eventTigerAttack(party, display)

		
	# good events! -----------------------------------------------------
	
	def eventFoundFood (self, party, display) :
		""" party randomly finds food - based on random number """
		
		"""
		myFont = pygame.font.Font('freesansbold.ttf', 30) # figure out different way
		
		Food = myFont.render( "You found food!" , 1, (0,0,0))
		display.blit(noEvent, (350, 300))
		"""
		
		print "You found food!"
		party.updateFood((self._randNum / 1))
		print (self._randNum / 1), " food has been added to your inventory."
		
	def eventFoundGoodHerb (self, party, display) :
		""" party randomly finds a herb with healing effects """
		
		print "You found a healing herb!"
		print "All party members health has been increased"
		party.incrPartyHealth(10)
		party.updatePartyHealthEffect(1)
	
		# other good events:
	
	
	
	# bad events! ------------------------------------------------------

	def eventLostFood(self, party, display) : 
		""" party randomly loses food """
		foodAmount = self._randNum / 4
		
		if foodAmount % 2 == 0 :
			print "Bugs got into some food! You had to leave some behind."
		else :
				
			randPartyMember = self.getRandomPartyMember(party)	
			print randPartyMember.getName(), "snacked on some food during the night." 
			randPartyMember.incrHealth(10)
			
		print "You lost ", foodAmount, "food."
		
		if party.getFood() - foodAmount <= 0 :
			party.updateFood(-(party.getFood()))
		else :
			party.updateFood(-foodAmount)
		
		if party.getFood() == 0 :
			party.setDead()			#stop game loop
			print "All party members are dead."
		else :
			pass
	
	def eventFoundBadHerb (self, party, display) :
		""" party randomly finds a herb with negative effects """
		
		print "You found a poisonous herb!"
		print "All party members health has been decreased"
		party.decrPartyHealth(10)
		
	def eventBrokeArm (self, party, display) :
		""" party member randomly breaks an arm """
		effect = "Broken Arm"
		
		randPartyMember = self.getRandomPartyMember(party)	
		print randPartyMember.getName(), "broke an arm. Lost 50 health."
		randPartyMember.decrHealth(50)
		randPartyMember.updateHealthEffect(-2)
		
		if randPartyMember.getHealthTitle() == "Healthy" :
			randPartyMember.setHealthTitle(effect)
		elif randPartyMember.getHealthTitle() == "Broken Leg" :
			effect = "Broken arm and broken leg"
			randPartyMember.setHealthTitle(effect)
		else :
			randPartyMember.setHealthTitle(effect)			
			
		
	def eventBrokeLeg (self, party, display) :
		""" party member randomly breaks an arm """
		effect = "Broken Leg"
		
		randPartyMember = self.getRandomPartyMember(party)
		print randPartyMember.getName(), "broke a leg. Lost 70 health."
		randPartyMember.decrHealth(70)
		randPartyMember.updateHealthEffect(-5)
		
		if randPartyMember.getHealthTitle() == "Healthy" :
			randPartyMember.setHealthTitle(effect)
		elif randPartyMember.getHealthTitle() == "Broken Arm" :
			effect = "Broken arm and broken leg"
			randPartyMember.setHealthTitle(effect)
		else :
			randPartyMember.setHealthTitle(effect)
	
	def eventTigerAttack (self, party, display) :
		""" the whole party dies """
		
		print "A wild tiger visciously killed the party. \n"
		party.setDead()
		
	# other bad events (got a disease, lost the machete, broke an arm)
	
	def getRandomPartyMember (self, party) :
		
		if not party.checkPartyDead() :
			randPartyMember = self._rand.randint(0, party.getSize()-1)
			while party.getPartyMember(randPartyMember).deadPerson() :
				randPartyMember = self._rand.randint(0, party.getSize()-1)
			return party.getPartyMember(randPartyMember)

"""
party = Party()
party.setUpParty()
test = RandomEvents()

for x in range(1,11) :
	print "Turn: ", x
	print "Random Number: ", test.getRandNum()
	test.event(party)
	test.randNum ()
	print ""
	continueTest = raw_input ("Press any key to continue:  ")
	print ""

party.displayParty()
party.getInventory().displayInventory()
"""
