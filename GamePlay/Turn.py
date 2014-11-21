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

"""
The Turn Module
"""

class Turn :
	
	def __init__(self):
		""" initializes the turn """
		self._foodLevel = 2
		self._day = 0
		pass 
	
	def updateTurn(self, party):
		""" updates the turn """
		self._day += 1
		self.decrementFood (party)
		
	def decrementFood (self, party) :
		""" decrements the party's food """
		size = party.getSize()
		inv = party.getInventory()
		inv.updateFood (-self._foodLevel*size)
		party.setInventory(inv)
	
	def changeFoodLevel (self, level) :
		""" changes food level of the party """
		self._foodLevel = level

	def checkInventory (self, party) :
		"""displays te passed in parties inventory"""
		party.getInventory().displayInventory()
		
	def menu (self, party) :
		"""displays menu options and handles each option"""
		option = self.displayMenu(party)
		
		if option == 1 :
			return True
		elif option == 2 :
			self.checkInventory(party)	
		elif option == 3 :
			level = self.askFoodLevel()
			self.changeFoodLevel (level)
		elif option == 4 :
			#call hunting game and run it		
			pass
			
	def askFoodLevel (self) :
		""" asks the user what the new food ration level is """
		level = int(raw_input ("Food Level either 1 or 2 or 3 "))
		while level < 1 and level > 3 :
			level = int(raw_input ("Food Level either 1 or 2 or 3 "))
		# WORRY ABOUT EXCEPTIONS
		return level		
			
	def displayMenu (self, party) :
		""" display the Menu and return the option """
		print "Food Rations: ", self.foodLevel()
		print "Day Number:", self._day
		print "\n\n\n"
		option = self.displayOptions()
		return option
		
	def displayOptions (self) :	
		""" display menu options """
		print "Options\n\n"
		print "1. Continue"
		print "2. Check backpack"
		print "3. Change food rations"
		print "4. Hunt for food\n"

		option = raw_input ("What is your choice?  ")
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
