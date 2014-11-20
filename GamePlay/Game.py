#!/usr/bin/python
##################################
# File Name: Game.py
# Author: 	 Group 3
# Date: 	 11/10/2014
# Class:	 CS360
# Assignment:Jungle Jamboree
# Purpose: 	 Game class
##################################

import pygame 
from pygame.locals import *
from Party import *

"""
The Game Module
"""

class Game :

	def __init__(self) :
		"""sets running to true, and creates a party and begins setting
		 up a pygame display """
		self._running = True
		self._display = None
		self._party = Party()
		self._width = 640
		self._height = 400
		self._size = (self._width, self._height)
		pass
		
	def on_init (self) :
		self._party.setUpParty()
		pygame.init()
		self._running = True
		self._display = pygame.display.set_mode(self._size, pygame.HWSURFACE)
			
	def on_event (self, event):
		if event.type == pygame.QUIT:
			self._running = False
	
	def on_loop (self):
		pass
	
	def on_render (self) :
		pass			
		
	def on_cleanup (self):	
		pygame.quit ()
		
	def on_execute(self):
		if self.on_init() == False:
			self._running = False
			
		while (self._running ):
			for event in pygame.event.get ():
				self.on_event(event)
			self.on_loop()
			self.on_render()
		self.on_cleanup()			
