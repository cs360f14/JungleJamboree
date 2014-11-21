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
import sys
from pygame.locals import *
from Player import Player

class Game :
	"""
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
		self._width = 400
		self._height = 300
		self._size = (self._width, self._height)
		pygame.init()
		self._display = pygame.display.set_mode(self._size)
		self._myFont = pygame.font.Font('freesansbold.ttf', 15)
		pygame.display.set_caption('Jungle Jamboree')
		pass
		
	def on_init (self) :
			self._running = True
			
	def on_event (self, event):
		if event.type == pygame.QUIT:
			self._running = False
	
	def on_loop (self):
		self._display.blit(img, (imgx,imgy))
		self._display.blit(start, (150,145))
		while(True):
			for event in pygame.event.get():
				#allows you to see what the last input was in the geany output window
				print event
				#called when you hit the X
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
			#the update for the screen		
			pygame.display.update()
	
	def on_render (self) :
		pass			
		
	def on_cleanup (self):	
		pygame.quit ()
		
	def on_execute(self):
		pass
	
	def getParty (self) :
		for x in range(1) :
			self._party.append(Player(self.getName())) 
	
	def getName (self) :
		name = raw_input("Enter Name: ")
		return name
		
#setDisplay = pygame.display.set_mode((400,300))
pygame.display.set_caption('Jungle Jamboree')
img = pygame.image.load('Images/TestBackground.png')
imgx = 0
imgy = 0

testGame = Game()
start = testGame._myFont.render("START", 1, (255,255,255))
#testGame.on_init()
testGame.on_loop()
