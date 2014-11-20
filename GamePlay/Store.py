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
		pass 
