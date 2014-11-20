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

class Inventory :
	def __init__(self):
		self._cash = 500
		self._items = []
	
	def generateItem (self) :
		for item in self._items :
			yield item
			
	def addItem (self, Aitem) :
		isIn = False
		for item in self.generateItem() and not isIn :
			if item.getName() == Aitem.getName() :
				item.updateQuantity(Aitem.getQuantity())
				isIn = True
		if not isIn :
			self._items.append(Aitem)

	def removeItem (self, rItem) :
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
		
