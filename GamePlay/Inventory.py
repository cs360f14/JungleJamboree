#!/usr/bin/python
##################################
# File Name: Inventory.py
# Author: 	 Group 3
# Date: 	 11/10/2014
# Class:	 CS360
# Assignment:Jungle Jamboree
# Purpose: 	 Inventory class
##################################

from Item import *
import pygame 
from pygame.locals import *
import sys

"""
The Inventory Module
"""

class Inventory :
	def __init__(self):
		"""initializes the amount of money and creates a list """
		self._cash = 500
		self._food = 100
		self._items = []
		
	def getSize (self) :
		return len(self._items)
	
	def generateItem (self) :
		"""A generator for iterating through the items """
		for item in self._items :
			yield item
			
	def addItem (self, Aitem) :
		"""Adds an item to an inventory. If the item is already in the
		inventory then the quantity is increased"""
		isIn = False
		for item in self.generateItem():
			if item.getName() == Aitem.getName() :
				item.updateQuantity(Aitem.getQuantity())
				isIn = True
				break	
		if not isIn :
			self._items.append(Aitem)
			
	def returnItem (self, index) :
		"""returns the item with the passed in index"""
		if index >= len(self._items) :
			return None #maybe Exception?
		return self._items[index]
					

	def removeItem (self, rItem) :
		""" Removes an item from the inventory. If the quantity of the
		removing item is less than the amount then the item quantity is
		subtracted. If the amount is the same then the item is removed
		from the inventory. If the removing item quantity is greater
		then the item is removed from the inventory"""
		count = 0
		for item in self.generateItem() :
			if item.getName() == rItem.getName() :
				if item.getQuantity() < rItem.getQuantity() :

					item.updateQuantity(-item.getQuantity()) #still need to change
					#set to 0
					self._items.remove(item) # may not work
				else :
					item.updateQuantity(-rItem.getQuantity())
			count += 1
			
	def getFood (self) :
		"""returns the amount of food"""
		return self._food
		
	def updateFood (self, num) :
		"""updatets the amount of food"""
		self._food += num
		
	def getCash (self) :
		"""returns the amount of cash"""
		return self._cash
		
	def updateCash (self, num) :
		"""updatets the amount of cash"""
		self._cash += num
		
	def displayInventory (self, mouse, event, display) :
		"""displays the inventory in a nice fashion"""

		myFont = pygame.font.Font('freesansbold.ttf', 15) # figure out different way
		
		stringHeight = 40
		cashString = "Cash:  $" + str(self.getCash())
		cash = myFont.render(cashString, 1, (255,255,255))
		display.blit(cash, (10, stringHeight))
		stringHeight += 30
		foodString = "Food:  " + str(self.getFood())
		food = myFont.render(foodString, 1, (255,255,255))
		display.blit(food, (10, 70))
		stringHeight += 30


		count = 0
		for item in self.generateItem() :
			itemTexts = myFont.render(str(item), 1, (255, 255, 255))	
			display.blit(itemTexts, (10, stringHeight))								
			stringHeight += 30
			count += 1	
			
	def getItemSelection (self, mouse, event) :
		"""Gets the correct item or food selection from the screen"""
		myFont = pygame.font.Font('freesansbold.ttf', 15)	
		
		goodOption = False
		option = -1
		stringHeight = 70
		if pygame.mouse.get_pressed ()[2] :
			if self.checkMouse (mouse, 5, 100, stringHeight - 5, \
			stringHeight + 25) :
				option = self.getSize()
				goodOption = True
			stringHeight += 30
			option = 0	
			for item in self.generateItem () :
				if self.checkMouse (mouse, 5, 200, stringHeight - 5, \
				stringHeight + 25) :
					goodOption = True
					break;
				option += 1
				stringHeight += 30	
			if self.checkMouse (mouse, 26, 60, 550, 570) :
				option = -1	
				goodOption = True
			if not goodOption:
				option = -2	
		return option	

	def checkItemAmount (self, item, inventory, amount) :
		GoodAmount = True 
		if amount > item.getQuantity() or \
			(amount * item.getCost()) > inventory.getCash():
			GoodAmount = False
		return GoodAmount	
			
	def checkFoodAmount (self, inventory, amount) :
		GoodAmount = True
		if amount > self.getFood () or amount > inventory.getCash():
			GoodAmount = False		
		return GoodAmount	
	
	def checkMouse (self, mouse, left, right, top, bottom):
		"""Checks if the mouse pointer is located in the box passed in"""
		isIn = False
		if mouse[0]	> left and mouse[0] < right \
		and mouse[1] > top and mouse[1] < bottom :
			isIn = True
		return isIn
"""	

item1 = Item("A", 5, 5.00)
item2 = Item("B", 3, 5.00)
item3 = Item("C", 5, 20.00)
item4 = Item("D", 10, 6.00)
item5 = Item("E", 100, 1.00)
item6 = Item("B", 5, 5.00)

backpack = Inventory ()
backpack.addItem(item1)	
backpack.addItem(item2)	
backpack.addItem(item3)	
backpack.addItem(item4)	
backpack.addItem(item5)	
backpack.addItem(item6)		

backpack.displayInventory()
	
"""
