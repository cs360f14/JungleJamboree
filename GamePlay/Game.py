#!/usr/bin/python
##################################
# File Name: Game.py
# Author: 	 Group 3
# Date: 	 11/10/2014
# Class:	 CS360
# Assignment:Jungle Jamboree
# Purpose: 	 Game class
##################################

# import pygame 
# from pygame.locals import *
from Player import Player

class Game :
	
	def __init__(self) :
		self._running = True
		self._party = []
		self.getParty()
		pass
	
	"""
	def __init__(self) :
		self._running = True
		self._display = None
		self._party = []
		self.getParty()
		self._width = 640
		self._height = 400
		self._size = (self._width, self._height)
		pass
		
	def on_init (self) :
			pygame.init()
			self._running = True
			self._display = pygame.display.set_mode(self.size, pygame.HWSURFACE)
			
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
	"""
	def getParty (self) :
		for x in range(1) :
			self._party.append(Player(self.getName())) 
	
	def getName (self) :
		name = raw_input("Enter Name: ")
		return name

