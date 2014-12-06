#!/usr/bin/python
##################################
# File Name: Store.py
# Author: 	 Group 3
# Date: 	 11/10/2014
# Class:	 CS360
# Assignment:Jungle Jamboree
# Purpose: 	 Store class
##################################

from Inventory import *
from Party import * 
import pygame 
from pygame.locals import *
import sys

"""
The Store Module
""" 

class Store (Inventory):
	
	def __init__ (self) :
		Inventory.__init__(self)
		self._food = 5000
			
		#relationship?
	
	def menu (self, party, display, mouse, event) :
		""" displays the menu and choices"""
		isInStore = True
		myFont = pygame.font.Font('freesansbold.ttf', 15)
					
		buy = myFont.render("Buy Items", 1, (0, 0, 0))
		display.blit(buy, (20, 420))
		sell = myFont.render("Sell Items", 1, (0, 0, 0))
		display.blit(sell, (20, 450))		
		trade = myFont.render("Trade", 1, (0, 0, 0))
		display.blit(trade, (20, 480))		
		tips = myFont.render("Random Tips", 1, (0, 0, 0))
		display.blit(tips, (20, 510))
		if event.type == MOUSEBUTTONDOWN:
			if self.checkMouse (mouse, 15, 100, 415, 440) :
				#self.buy (party, mouse, event, display)
				pass
			elif self.checkMouse (mouse, 15, 100, 445, 470) :	
				#self.sell (party)
				pass
			elif self.checkMouse (mouse, 15, 100, 445, 470) :	
				cantTradeString = "Sorry I have nothing to Trade."
				cantTrade = myFont.render(cantTradeString, 1, \
				(0, 0, 0))
				display.blit(buy, (480, 420))			
			elif self.checkMouse (mouse, 15, 100, 445, 470) :	
				tipString = "You should buy plenty of food for the" + \
				" jungle is Harsh"
				tip = myFont.render(tipString, 1, (0, 0, 0))
				display.blit(buy, (510, 420))				
	"""
	def getAmountStore (self, item, party) :
		amount = int(raw_input ("Choose the amount you want to buy:"))
		while amount < 0 or amount > item.getQuantity() or \
		(amount * item.getCost()) > party.getCash():
			amount = int(raw_input ("Choose the amount you want to buy:"))
		# WORRY ABOUT EXCEPTIONS	
		return amount
		
	def getAmountParty (self, item, party) :
		amount = int(raw_input ("Choose the amount you want to sell:"))
		while amount < 0 or amount > item.getQuantity() or \
		(amount * item.getCost()) > self.getCash():
			amount = int(raw_input ("Choose the amount you want to sell:"))
		# WORRY ABOUT EXCEPTIONS	
		return amount	
		
	def getAmountStoreFood (self, party) :
		amount = int(raw_input ("Choose the amount of food:"))
		while amount < 0 or amount > self.getFood () or \
		amount > party.getCash():
			amount = int(raw_input ("Choose the amount of food:"))
			if amount < 0 :
				print ("amount < 0")
			if amount > self.getFood ():
				print ("amount > self.getFood ()")		
			if 	amount > party.getCash() :
				print ("amount > party.getCash()")	
		# WORRY ABOUT EXCEPTIONS	
		return amount		
		
	def getAmountPartyFood (self, party) :
		amount = int(raw_input ("Choose the amount of food:"))
		while amount < 0 or amount > party.getFood () or \
		amount > self.getCash():
			amount = int(raw_input ("Choose the amount of food:"))
		# WORRY ABOUT EXCEPTIONS	
		return amount			
	"""		

	def setUpStore(self):
		"""Initalizes the items in the store"""
		machete = Item ("Machete", 1, 40.00)
		self.addItem (machete)
		pills = Item ("Pills", 100, 1.00)
		self.addItem(pills)
		
	def buy (self, party, mouse, event, display) : 	
		""" displays the stores wares and allows the party to buy items 
			from the store """
		amountPerItem = 1
		amountPerFood = 10
		self.displayInventory(mouse, event, display)
		option = self.getItemSelection(mouse, event)
		
		while option <= self.getSize ():
			if option < self.getSize () : #item in inventory
				item = self.returnItem (option)
				item.updateQuantity(-amountPerItem)
				self.removeItem(item)
				self.updateCash(amountPerItem * item.getCost())
				party.addToInventory(item)
				party.updateCash(-amountPerItem * item.getCost())
							
			elif option == self.getSize (): #food
				self.updateFood(-amountPerFood)
				self.updateCash(amountPerFood)
				party.updateFood(amountPerFood)
				party.updateCash(-amountPerFood)
				
			self.displayInventory(mouse, event, display)
			option = self.getItemSelection(mouse, event)		
	"""		
	def buy (self, party) :	

		self.displayInventory()
		option = self.getOption ()
		
		while option <= self.getSize () :
			
			if option <= self.getSize () : #an item in the inventory
				item = self.returnItem (option - 1)	
				amount = self.getAmountStore (item, party)
				item.updateQuantity(-amount)
				self.removeItem(item)
				self.updateCash(amount * item.getCost())
				party.addToInventory(item)
				party.updateCash(-amount * item.getCost())
				
			elif option == self.getSize () + 1 :#food
				amount = self.getAmountStoreFood (party)
				self.updateFood(-amount)
				self.updateCash(amount)
				party.updateFood(amount)
				party.updateCash(-amount)
				
			self.displayInventory()	
			option = self.getOption ()			
	"""	
	def sell (self, party):
		""" displays the parties wares and allows the party to buy items 
			from the store """
		party.getInventory().displayInventory()
		option = self.getOption ()
		while option <= self.getSize () + 1 :
			
			if option <= self.getSize () : #an item in the inventory
				item = self.returnItem (option - 1)	
				amount = self.getAmountParty (item, party)
				item.updateQuantity(amount)
				self.addItem(item)
				self.updateCash(-amount * item.getCost())
				party.removeFromInventory(item)
				party.updateCash(amount * item.getCost())
				
			elif option == self.getSize () + 1 : #food
				amount = self.getAmountPartyFood (party)
				self.updateFood(amount)
				self.updateCash(-amount)
				party.updateFood(-amount)
				party.updateCash(amount)
				
			party.getInventory().displayInventory()
			option = self.getOption ()		
	
"""


party = Party ()
store = Store ()
party.setUpParty ()
store.setUpStore ()
party.getInventory().displayInventory()
print("\n\n\n")
store.menu (party)
print("\n\n\n")
party.getInventory().displayInventory()
"""
