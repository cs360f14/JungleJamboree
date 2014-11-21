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
		#Buy
		#Sell
		#Trade
		#Random Tips
		#Maybe Minigame
		pass	
	
	def buy (self, party) :	
		""" displays the stores wares and allows the party to buy items 
			from the store """
		self.displayInventory()
		
		option = self.getOption ()
		item = self.returnItem (option - 1)	
		amount = getAmount (self, item, party)
		item.updateQuantity(-amount)
		self.removeItem(item)
		self.updateCash(amount * item.getCost())
		party.addToInventory(item)
		party.updateCash(-amount * item.getCost())
		
	def getOption (self) :
		size = self.getSize()
		option = int(raw_input ("Choose what you want to buy"))
		while option < 1 and option > (size + 1) :
			option = int(raw_input ("Choose what you want to buy"))
		#worry about exceptions	
		return option	
		
	def getAmount (self, item, party) :
		amount = int(raw_input ("Choose the amount you want to buy"))
		while amount < 0 and amount > item.getQuantity() and \
		(amount * item.getCost()) < party.getCash():
			amount = int(raw_input ("Choose the amount you want to buy"))
		# WORRY ABOUT EXCEPTIONS	
		return amount
		
	def setUpStore(self):
		pass

