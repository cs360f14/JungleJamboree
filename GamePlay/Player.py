#!/usr/bin/python
##################################
# File Name: Player.py
# Author: 	 Group 3
# Date: 	 11/10/2014
# Class:	 CS360
# Assignment:Jungle Jamboree
# Purpose: 	 Player class
##################################

from Inventory import *

class Player :
	
	def __init__ (self, name) :
		self._name = name
		self._backpack = Inventory()
		
	def __str__ (self) :
		return self._name
