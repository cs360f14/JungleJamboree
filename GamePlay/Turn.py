#!/usr/bin/python
##################################
# File Name: Turn.py
# Author: 	 Group 3
# Date: 	 11/10/2014
# Class:	 CS360
# Assignment:Jungle Jamboree
# Purpose: 	 Turn class
##################################

from Party import *
from RandomEvents import *
import os
import pygame 
from pygame.locals import *
import sys

"""
The Turn Module
"""

class Turn :
	
	def __init__(self):
		""" initializes the turn """
		self._foodLevel = 2
		self._day = 0 
		self._distance = 0
		self._distancePerDay = 5
		self._randEvent = RandomEvents()
		self._Foraged = False
		self._running = True
	
	def updateTurn(self, party, display):
		""" updates the turn """
		self._Foraged = False
		self._day += 1
		self._distance += self._distancePerDay
		self._randEvent.randNum()  #gets the random number
		self._randEvent.event(party, display)
		self.decrementFood (party)
		self.checkFood (party)
		party.updateHealth()
		self.deadMember(party, display)
		self.partyDead(party)
	
	def getDay (self) :
		""" returns the day """
		return self._day
		
	def getDistance (self) :
		""" returns the distance traveled """
		return self._distance
		
	def setDistancePerDay (self, num) :
		""" sets the distance traveled per day """
		self._distancePerDay = num	
	
	def updateDistancePerDay (self, num) :
		""" updates the distance traveled per day """ 
		self._distancePerDay += num
		
	def specialItems (self, party) :
		#if party inventory contains a machete, affects the distance per day (similar for other special items)
		pass
	
	def decrementFood (self, party) :
		""" decrements the party's food """
		size = party.getSize()
		inv = party.getInventory()
		inv.updateFood (-self._foodLevel * size)
		party.setInventory(inv)
	
	def changeFoodLevel (self, level, party) :
		""" changes food level of the party and adjusts the health effect based on the food level chosen"""
		oldFoodLevel = self._foodLevel
		newFoodLevel = level
		
		if level == 1 :
			#negative health effect (decrement to what is already the current health effect)
			if oldFoodLevel == 2 :
				party.updatePartyHealthEffect(-1)
			elif oldFoodLevel == 3 :
				party.updatePartyHealthEffect(-2)
		elif level == 2 :
			if oldFoodLevel == 1 :
				party.updatePartyHealthEffect(1)
			elif oldFoodLevel == 3 :
				party.updatePartyHealthEffect(-1)
		elif level == 3 :
			#positive health effect (increment to what is already the current health effect)
			if oldFoodLevel == 1 :
				party.updatePartyHealthEffect(2)
			elif oldFoodLevel == 2 :
				party.updatePartyHealthEffect(1)
		
		self._foodLevel = newFoodLevel
		
	def checkInventory (self, party) :
		"""displays the passed in parties inventory"""
		party.getInventory().displayInventory()
		
	def forageEvent(self, party, display) :
		if not self._Foraged :
			self._randEvent.forageEvent(party, display)	
			self._Foraged = True	
			
	def menu (self, party) :
		"""displays menu options and handles each option"""
		option = self.displayMenu(party)
		foraged = False
	
		while self._running and not foraged:
			option = self.displayOptions()
			if option == 1 :
				return True
			elif option == 2 :
				self.checkInventory(party)
				click = raw_input ("Press enter to return to menu: ")
			elif option is 3 :
				level = self.askFoodLevel()
				self.changeFoodLevel (level, party)
				click = raw_input ("Press enter to return to menu: ")
			elif option == 4 :
				self._randEvent.forageEvent(party)		
				foraged = True
			elif option == 5 :
				party.displayParty()
				click = raw_input ("Press enter to return to menu:  ")
			self.partyDead(party)
			
	def askFoodLevel (self) :
		""" asks the user what the new food ration level is """
		level = int(raw_input ("Food Level either 1 (Starving) or 2 (Adequate) or 3 (Stuffed):  "))
		while level < 1 or level > 3 :
			level = int(raw_input ("Food Level either 1 (Starving) or 2 (Adequate) or 3 (Stuffed):  "))
		return level		
			
	def displayMenu (self, party, display) :
		""" display the Menu and return the option """
		
		myFont2 = pygame.font.Font('freesansbold.ttf', 25)
		
		dayString = "DAY:  " + str(self._day)
		day = myFont2.render(dayString, 1, (255,255,255))	
		display.blit(day, (300, 270))
		
		disString = "DISTANCE:  " + str(self._distance)
		distance = myFont2.render(disString, 1, (255,255,255))	
		display.blit(distance, (300, 300))
		
		foodString = "FOOD AMOUNT:  " + str(party.getFood())
		food = myFont2.render(foodString, 1, (255,255,255))	
		display.blit(food, (300, 330))
		
		foodLevelString = "FOOD LEVEL:  " + str(self.foodLevel())
		foodLevel = myFont2.render(foodLevelString, 1, (255,255,255))	
		display.blit(foodLevel, (300, 360))
		
		
		
	def displayOptions (self) :	
		""" display menu options """
		print "Options"
		print "1. Continue"
		print "2. Check backpack"
		print "3. Change food rations"
		print "4. Forage"
		print "5. Check Party \n"

		option = int(raw_input ("What is your choice?  "))  #need to fix if a string is entered. (will break when a string entered)
		while option < 1 or option > 5 :
			option = int(raw_input ("What is your choice?  "))
			
		print ""
		
		return option
		
	def foodLevel (self) :
		""" displays the food level"""
		foodString = "Neutral"
		if 1 == self._foodLevel :
			foodString = "Starvation"
		elif 2 == self._foodLevel :
			foodString = "Adequate"
		elif 3 == self._foodLevel :
			foodString = "Stuffed"
		return foodString
		
	def checkFood (self, party) :
		if party.getFood () <= 0 :
			party.setDead ()
			
	
	def getRunning (self) :
		""" returns the status of the game """
		return self._running
		
	def partyDead(self, party):
		"""  """
		if party.checkPartyDead() :
			self._running = False
	
	def deadMember (self, party, display) :
				
		myFont = pygame.font.Font('freesansbold.ttf', 30) 
		

		
		for person in party.generatePerson() :
			if person.deadPerson() and person.getHealthTitle != "Dead":
				"""		
				personString = person.getName()+ "died."
				dPerson = myFont.render(personString , 1, (255,0,0))
				display.blit(dPerson, (350, 500))"""
				
				print person.getName(), "died.\n"
				party.death()
				person.setHealthTitle("Dead")
				person.setHealthEffect(0)

#important testing!!!!

"""

game = Turn()
party = Party()
party.setUpParty()
print "\nYou have started your journey!\n"

while (game.getRunning()) :
	game.menu(party)
	print "\n\nEnd of Day: ", game.getDay(), "\n"
	game.updateTurn(party)
	
	
print "End of the journey."

"""
