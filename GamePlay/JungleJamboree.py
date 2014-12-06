 #!/usr/bin/python
##################################
# File Name: JungleJamboree.py
# Author: 	 Group 3
# Date: 	 11/10/2014
# Class:	 CS360
# Assignment:Jungle Jamboree
# Purpose: 	 Game Logic 
##################################

from Store import *
from Turn import *
from Party import *
"""
The Jungle Jamboree Module
"""
class JungleJamboree :
	
	
	def __init__ (self) :
		self._running = True
		self._display = None
		self._party = Party()
		self._turn = Turn ()
		self._store = Store ()

	def startGame (self) :
		self._party.setUpParty ()
		self._store.setUpStore ()
		self._store.menu (self._party)
		
		

#jungle = JungleJamboree ()
#jungle.startGame ()
#main ()
