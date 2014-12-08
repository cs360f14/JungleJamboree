#!/usr/bin/python
##################################
# File Name: RandomEvents.py
# Author: 	 Group 3
# Date: 	 11/10/2014
# Project:	 Jungle Jamboree
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
		""" party forages a random amount of food and outputs this 
			to the screen """
		
		randNum = self._rand.randint(0, 100)
		foodForaged = 0
		
		if randNum in range (0,85) :
			foodForaged = self._rand.randint(0,6)
		
		elif randNum in range (85,100) :
			foodForaged = 5 * party.getSize()
			
		myFont = pygame.font.Font('freesansbold.ttf', 30) 
		
		foragedString = str(foodForaged)  + " food foraged."
		foraged = myFont.render(foragedString , 1, (255,255,255))
		display.blit(foraged, (260, 480))	

		party.updateFood(foodForaged)
	
	def event (self, party, display) :
		""" based on the random number, determine the event """
		
		if self._randNum in self._noEventRange : #range: 0 - 50
			self.noEvent(display)
			
		elif self._randNum in self._goodEventRange : #range: 50 -75
			self.upperEventGood(party, display)
			
		elif self._randNum in self._badEventRange : #range: 75 -100
			self.upperEventBad(party, display)
		
	def noEvent (self, display) :	
		""" no event will happen - """
		
		myFont = pygame.font.Font('freesansbold.ttf', 30)
		noEvent = myFont.render("Traveled Safely" , 1, (0,0,0))
		display.blit(noEvent, (300, 350))
	
	def upperEventGood (self, party, display) :  
		""" the possible good events """
		
		# found food
		if self._randNum in range(50,60) :
			self.eventFoundFood(party, display)
		
		# found good herb
		elif self._randNum in range(60, 75):
			self.eventFoundGoodHerb(party, display)
	
	def upperEventBad (self, party, display) :
		""" the possible bad events 
		
		Based on the random number that was generated, a bad event will
		be executed."""
		
		
		# lost food		
		if self._randNum in range(75,80) :
			self.eventLostFood(party, display)
		
		# found bad herb
		elif self._randNum in range(80, 85):
			self.eventFoundBadHerb(party, display)
		
		# party swarmed by mosquitos
		elif self._randNum in range (85, 90) :
			self.eventMosquitoSwarm(party, display)
			
		# monkeys stole food
		elif self._randNum in range (90, 94) :
			self.eventMonkeyAttack(party, display)
		
		# a party member broke an arm
		elif self._randNum in range (94, 97) :
			self.eventBrokeArm(party, display)
		
		# a party member broke a leg
		elif self._randNum in range (97, 100) :
			self.eventBrokeLeg(party, display)
		
		# a wild tiger kills entire party
		elif self._randNum == 100 :
			self.eventTigerAttack(party, display)


	# ----------------------------------------------------------------
	#          function definitions for good events! 
	# ----------------------------------------------------------------
	
	
	def eventFoundFood (self, party, display) :
		""" party randomly finds food - based on random number """
		
		party.updateFood((self._randNum / 1))
	
		myFont = pygame.font.Font('freesansbold.ttf', 30) 
		
		Food = myFont.render( "You found food!" , 1, (0,0,0))
		display.blit(Food, (350, 350))
		amountString = str(self._randNum / 2) + \
		" food has been added to your inventory."
		amount = myFont.render(amountString , 2, (0,0,0))
		display.blit(amount, (150, 390))
		
	def eventFoundGoodHerb (self, party, display) :
		""" party randomly finds a herb with healing effects """
		
		myFont = pygame.font.Font('freesansbold.ttf', 30) 
		
		herb = myFont.render("You found a healing herb!" , 1, (0,0,0))
		display.blit(herb, (250, 350))
		health = "All party members health has been increased"
		healthplus = myFont.render(health , 1, (0,0,0))
		display.blit(healthplus, (100, 390))
		
		party.incrPartyHealth(10)
		party.updatePartyHealthEffect(1)
	
	# other good events may be defined here.
	
	
	# ----------------------------------------------------------------
	#           end function definitions for good events! 
	# ----------------------------------------------------------------
	
	
	# ----------------------------------------------------------------
	#            function definitions for bad events! 
	# ----------------------------------------------------------------

	def eventLostFood(self, party, display) : 
		""" party randomly loses food """
		myFont = pygame.font.Font('freesansbold.ttf', 30) 
		
		foodAmount = self._randNum / 4
		displayString = ""
		
		if foodAmount % 2 == 0 :
			displayString =  "Bugs got into some food!"
		else :
			randPartyMember = self.getRandomPartyMember(party)	
			displayString =  randPartyMember.getName() + \
			" snacked on some food." 
			randPartyMember.incrHealth(10)
			
		lostFood = "You lost " + str(foodAmount) + "food."
		
		foodDisplay = myFont.render(displayString , 1, (0,0,0))
		display.blit(foodDisplay, (150, 350))
		lostFoodDisplay = myFont.render(lostFood , 1, (0,0,0))
		display.blit(lostFoodDisplay, (200, 390))
		
		if party.getFood() - foodAmount <= 0 :
			party.updateFood(-(party.getFood()))
		else :
			party.updateFood(-foodAmount)
		
		if party.getFood() == 0 :
			party.setDead()
			Dead = \
			myFont.render( "All party members are dead.", 1, (0,0,0))
			display.blit(Dead, (250, 450))
		else :
			pass
	
	def eventFoundBadHerb (self, party, display) :
		""" party randomly finds a herb with negative effects """
		
		myFont = pygame.font.Font('freesansbold.ttf', 30) 
		
		herb = myFont.render("You found a poisonous herb!" , 1, (0,0,0))
		display.blit(herb, (250, 350))
		health = "All party members health has been decreased"
		healthminus = myFont.render(health , 1, (0,0,0))
		display.blit(healthminus, (100, 390))
		
		party.decrPartyHealth(10)
		party.updatePartyHealthEffect(-1)
		
	def eventMosquitoSwarm (self, party, display) :
		""" mosquito swarm attacks the party, negative health effect """
		
		myFont = pygame.font.Font('freesansbold.ttf', 30) 
		
		herb = myFont.render("A mosquito swarm attcked the party!" , 1, (0,0,0))
		display.blit(herb, (200, 350))
		health = "All party members health has been decreased"
		healthminus = myFont.render(health , 1, (0,0,0))
		display.blit(healthminus, (50, 390))
		
		party.decrPartyHealth(8)
		
	def eventBrokeArm (self, party, display) :
		""" party member randomly breaks an arm """
		
		effect = "Broken Arm"
		myFont = pygame.font.Font('freesansbold.ttf', 30) 
		
		randPartyMember = self.getRandomPartyMember(party)		

		armstring = randPartyMember.getName() + \
		 " broke an arm. Lost 50 health."
		arm = myFont.render(armstring, 1, (0,0,0))
		display.blit(arm, (100, 350))
		
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
		myFont = pygame.font.Font('freesansbold.ttf', 30) 
		
		randPartyMember = self.getRandomPartyMember(party)		

		legstring = randPartyMember.getName() + \
		" broke a leg. Lost 70 health."
		leg = myFont.render(legstring, 1, (0,0,0))
		display.blit(leg, (100, 350))
		
		randPartyMember.decrHealth(70)
		randPartyMember.updateHealthEffect(-5)
		
		if randPartyMember.getHealthTitle() == "Healthy" :
			randPartyMember.setHealthTitle(effect)
		elif randPartyMember.getHealthTitle() == "Broken Arm" :
			effect = "Broken arm and broken leg"
			randPartyMember.setHealthTitle(effect)
		else :
			randPartyMember.setHealthTitle(effect)
	
	def eventMonkeyAttack (self, party, display) :
		""" a wild monkey attacked the party and stole food """
		
		foodAmount = self._randNum / 4
		
		myFont = pygame.font.Font('freesansbold.ttf', 30) 
		
		message = myFont.render("A bunch of monkeys stole some food!" , 1, (0,0,0))
		display.blit(message, (250, 350))
		food = "Party food has been decreased."
		foodminus = myFont.render(food , 1, (0,0,0))
		display.blit(foodminus, (100, 390))
		
		if party.getFood() - foodAmount <= 0 :
			party.updateFood(-(party.getFood()))
		else :
			party.updateFood(-foodAmount)
		
		if party.getFood() == 0 :
			party.setDead()
			Dead = \
			myFont.render( "All party members are dead.", 1, (0,0,0))
			display.blit(Dead, (250, 450))
		else :
			pass
		
	
	def eventTigerAttack (self, party, display) :
		""" the whole party dies from the tiger attack """
		
		myFont = pygame.font.Font('freesansbold.ttf', 30) 
		
		tigerString = "A wild tiger visciously killed the party."
		tiger = myFont.render(tigerString , 1, (0,0,0))
		display.blit(tiger, (150, 350))

		party.setDead()
		
	# other bad events may be defined here
	
	
	# ----------------------------------------------------------------
	#          end of function definitions for bad events! 
	# ----------------------------------------------------------------
	
	def getRandomPartyMember (self, party) :
		""" returns a random party member (not dead members) """
		
		if not party.checkPartyDead():
			randPartyMember = \
			self._rand.randint(0, party.getInitialSize()-1)
			while party.getPartyMember(randPartyMember).deadPerson() :
				randPartyMember = \
				self._rand.randint(0, party.getInitialSize()-1)
			return party.getPartyMember(randPartyMember)
