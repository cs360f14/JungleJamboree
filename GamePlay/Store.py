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

"""
The Store Module
""" 

class Store (Inventory):
	
	def __init__ (self) :
		Inventory.__init__(self)
		self._food = 5000
		#relationship?
		
	def menu (self, party) :
		""" displays the menu and choices"""
		print ("1. Buy items")
		print ("2. Sell items")
		print ("3. Trade")
		print ("4. Random Tips")
		print ("5. Exit")
		# menuString = "1. Buy items\n" + "2. Sell items\n" + \
		#		"3. Trade" + "4. Random Tips"
		
		option = int(raw_input ("Choose which option: "))
		while option < 1 and option > 5:
			option = int(raw_input ("Choose which option: "))
		# WORRY ABOUT EXCEPTIONS	
		if option == 1 :
			self.buy (party)
		if option == 2 :
			self.sell (party)
		if option == 3 :
			print ("Sorry I have nothing to trade")
		if option == 4 :
			print ("You should buy plenty of food the jungle is harsh")
		
	
	def buy (self, party) :	
		""" displays the stores wares and allows the party to buy items 
			from the store """
		self.displayInventory()
		
		option = self.getOption ()
		while option <= self.getSize () + 1 :
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
			option = self.getOption ()		

	def getAmountStore (self, item, party) :
		amount = int(raw_input ("Choose the amount you want to buy:"))
		while amount < 0 and amount > item.getQuantity() and \
		(amount * item.getCost()) > party.getCash():
			amount = int(raw_input ("Choose the amount you want to buy:"))
		# WORRY ABOUT EXCEPTIONS	
		return amount
		
	def getAmountParty (self, item, party) :
		amount = int(raw_input ("Choose the amount you want to sell:"))
		while amount < 0 and amount > item.getQuantity() and \
		(amount * item.getCost()) > self.getCash():
			amount = int(raw_input ("Choose the amount you want to sell:"))
		# WORRY ABOUT EXCEPTIONS	
		return amount	
		
	def getAmountStoreFood (self, party) :
		amount = int(raw_input ("Choose the amount of food:"))
		while amount < 0 and amount > self.getFood () and \
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
		while amount < 0 and amount > party.getFood () and \
		amount > self.getCash():
			amount = int(raw_input ("Choose the amount of food:"))
		# WORRY ABOUT EXCEPTIONS	
		return amount			
		
	def setUpStore(self):
		"""Initalizes the items in the store"""
		pass
	
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
				amount = self.getAmountFood (party)
				self.updateFood(-amount)
				self.updateCash(amount)
				party.updateFood(amount)
				party.updateCash(-amount)
			option = self.getOption ()
