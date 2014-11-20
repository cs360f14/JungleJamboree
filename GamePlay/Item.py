#!/usr/bin/python
##################################
# File Name: Item.py
# Author: 	 Group 3
# Date: 	 11/10/2014
# Class:	 CS360
# Assignment:Jungle Jamboree
# Purpose: 	 Item class
##################################


class Item :
	def __init__ (self, name, quantity = 1, cost = 0.00):
		self._name = name
		self._quantity = quantity
		self._cost = cost
		
	def getCost(self):
		return self._cost

	def getQuantity(self):
		return self._quantity

	def getName(self):
		return self._name
		
	def updateQuantity (self, value) :
		self._quantity = self._quantity + value
