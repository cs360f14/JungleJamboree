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
		
	def getOption (self) :
		"""Gets which option of the inventory with food and exit 
		included  """
		size = self.getSize()
		option = int(raw_input ("Choose what item you want: "))
		while option < 1 or option > (size + 2) :
			option = int(raw_input ("Choose what item you want: "))
		#worry about exceptions	
		return option	
	
	def displayInventory (self) :
		"""displays the inventory in a nice fashion"""
		count = 1
		print "Backpack\n"
		
		print("Cash:  $" + str(self._cash) + "\n")
		for item in self.generateItem() :
			print(str(count) + ". " + str(item))
			count += 1
		print(str(count) + ". Food:  " + str(self._food))	
		count += 1
		#print(str(count) + ". Exit (to Exit inventory enter 0)")

	
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
