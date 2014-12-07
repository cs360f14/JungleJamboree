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
		self._storeState = ""
		self._inStore = False
			
		#relationship?
	
	def menu (self, party, display, mouse, event) :
		""" displays the menu and choices"""

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
				self._storeState = "buy"
				self._inStore = True
				
			elif self.checkMouse (mouse, 15, 100, 445, 470) :
				self._storeState = "sell"
				self._inStore = True

			elif self.checkMouse (mouse, 15, 100, 475, 500) :	
				self._storeState = "trade"
	
			elif self.checkMouse (mouse, 15, 100, 505, 530) :	
				self._storeState = "tip"
			elif self.checkMouse (mouse, 26, 60, 550, 570):
				self._storeState = "leave"	
		
						
		if self._storeState == "buy":
#			pygame.draw.rect(display, (0,255,0), (0,0, 300, 300))
			selectBuyString = "Please select the item you wish to buy."
			selectBuy = myFont.render(selectBuyString, 1, (255, 255, 255))
			display.blit(selectBuy, (450, 50))		
			self.buy (party, mouse, event, display)
		elif self._storeState == "sell" and self._inStore :	
#			pygame.draw.rect(display, (0,255,0), (0,0, 300, 300))	
			selectSellString = "Please select the item you wish to sell."
			selectSell = myFont.render(selectSellString, 1, (255, 255, 255))
			display.blit(selectSell, (450, 50))			
			self.sell (party, mouse, event, display)
			pass
		elif self._storeState == "trade" :		
			cantTradeString = "Sorry I have nothing to trade."
			cantTrade = myFont.render(cantTradeString, 1, (255, 255, 255))
			display.blit(cantTrade, (450, 50))		
		elif self._storeState == "tip" :					
			tipString1 = "You should buy plenty of food for the jungle."
			tipString2 = "The jungle is a harsh place"
			tip1 = myFont.render(tipString1, 1, (255, 255, 255))
			tip2 = myFont.render(tipString2, 1, (255, 255, 255))
			display.blit(tip1, (450, 50))
			display.blit(tip2, (450, 67))	

								


	def setUpStore(self):
		"""Initalizes the items in the store"""
		machete = Item ("Machete", 1, 40.00)
		self.addItem (machete)
		firstAidKit = Item ("First Aid Kit", 10, 20.00)
		self.addItem(firstAidKit)
		rope = Item ("Rope", 100, 5.00)
		self.addItem(rope)
		
	def buy (self, party, mouse, event, display) : 	
		""" displays the stores wares and allows the party to buy items 
			from the store """	
		amountPerItem = 1
		amountPerFood = 10
		self.displayInventory(mouse, event, display)
		
		option = self.getItemSelection(mouse, event)

		if option < self.getSize () and option >= 0 : #item in inventory
			item = self.returnItem (option)
			newItem = item.CopyItem ()
			newItem.setQuantity (amountPerItem)
			if self.checkItemAmount (item, party.getInventory(), \
			amountPerItem) :
				self.removeItem(newItem)
				self.updateCash(amountPerItem * item.getCost())
				party.addToInventory(newItem)
				party.updateCash(-amountPerItem * item.getCost())
						
		elif option == self.getSize (): #food
			if self.checkFoodAmount (party.getInventory(), \
			amountPerFood) :
				self.updateFood(-amountPerFood)
				self.updateCash(amountPerFood)
				party.updateFood(amountPerFood)
				party.updateCash(-amountPerFood)
			
		self.displayInventory(mouse, event, display)
#		self._storeState = ""


	def sell (self, party, mouse, event, display) : 	
		""" displays the parties wares and allows the party to sell 
		items to the store """	
		amountPerItem = 1
		amountPerFood = 10
		partyInv = 	party.getInventory()
		partyInv.displayInventory(mouse, event, display)
		
		option = partyInv.getItemSelection(mouse, event)
		
		if option < partyInv.getSize () and option >= 0 : #item in inventory
			item = partyInv.returnItem (option)
			newItem = item.CopyItem ()
			newItem.setQuantity (amountPerItem)
			if partyInv.checkItemAmount (item, self, amountPerItem) :
				partyInv.removeItem(newItem)
				partyInv.updateCash(amountPerItem * item.getCost())
				self.addItem(newItem)
				self.updateCash(-amountPerItem * item.getCost())
						
		elif option == self.getSize (): #food
			if partyInv.checkFoodAmount (self, amountPerFood) :
				partyInv.updateFood(-amountPerFood)
				partyInv.updateCash(amountPerFood)
				self.updateFood(amountPerFood)
				self.updateCash(-amountPerFood)
			
		partyInv.displayInventory(mouse, event, display)
#		self._storeState = ""

		
		"""
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
