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

"""
The Inventory Module
"""

class Inventory :
	def __init__(self):
		"""initializes the amount of money and creates a list """
		self._cash = 500
		self._items = []
	
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
			if isIn :
				break	
		if not isIn :
			self._items.append(Aitem)

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
			
	def displayInventory (self) :
		"""displays the inventory in a nice fashion"""
		for item in self.generateItem() :
			print(str(item))
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
