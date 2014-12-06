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
from Store import *
import sys

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
		self._store = Store ()
		self._store.setUpStore ()
		#self._party.setUpParty () #don't forget to add this not in init
		self._state = "Start"
		self._width = 800
		self._height = 600
		self._size = (self._width, self._height)
		pygame.init()
		pygame.font.init()
		self._display = pygame.display.set_mode(self._size)
		self._myFont1 = pygame.font.Font('freesansbold.ttf', 15)
		self._myFont2 = pygame.font.Font('freesansbold.ttf', 10)
		self._myFont3 = pygame.font.Font('freesansbold.ttf', 12)
		pygame.display.set_caption('Jungle Jamboree')
	
	def on_loop (self):
		self._display.blit(imgStart, (imgx,imgy))
		self._display.blit(start, (400,400))
		while(True):
			mouse = pygame.mouse.get_pos()
			for event in pygame.event.get():
				#allows you to see what the last input was in the geany output window
				print event

				#called when you hit the X
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
					
				if self._state == "Start":
					self.startButton (mouse, event)
															
				elif self._state == "Store":
					self.store (mouse, event)
										
				elif self._state == "Home":
					self.home (mouse, event)
									
				elif self._state == "Inventory":
					self.inventory (mouse, event)

			#the update for the screen		
			pygame.display.update()
			
	def startButton (self, mouse, event) :
		if event.type == MOUSEBUTTONDOWN:
			if self.checkMouse (mouse, 395, 460, 395, 415) :
				self._state = "Store"
							
	def store (self, mouse, event) :
		self._display.blit(imgStore, (imgx, imgy))
		self._display.blit(leave1, (20, 550))
		self._store.menu (self._party, self._display, mouse, event)
#		self._store.displayInventory (mouse, event, self._display)
		option = self._store.getItemSelection(mouse, event)
		
		if event.type == MOUSEBUTTONDOWN:
			if self.checkMouse (mouse, 20, 60, 550, 570) :
				self._state = "Home"
							
	def home (self, mouse, event) :
		self._display.blit(imgJungle, (imgx, imgy))
		self._display.blit(imgPerson1, (imgxP1, imgyP1))
		self._display.blit(imgPerson2, (imgxP2, imgyP2))
		self._display.blit(imgPerson3, (imgxP3, imgyP3))
		self._display.blit(imgPerson4, (imgxP4, imgyP4))
		self._display.blit(imgPerson5, (imgxP5, imgyP5))
		self._display.blit(store, (10, 225))
		self._display.blit(forage, (10, 240))
		self._display.blit(inventory, (10, 255))
		self._display.blit(party, (10, 270))
		self._display.blit(day, (170, 205))
		self._display.blit(distance, (170, 225))
		if event.type == MOUSEBUTTONDOWN:
			if self.checkMouse (mouse, 8, 45, 226, 233) :
				self._state = "Store"
		
		if event.type == MOUSEBUTTONDOWN:
			if self.checkMouse (mouse, 8, 69, 255, 265) :
				self._state = "Inventory"
		
	def inventory (self, mouse, event) :
		self._display.blit(imgInventory, (imgx, imgy))
		self._display.blit(leave2, (20, 550))
		self._party.getInventory().displayInventory(mouse, event, \
		self._display)

		if event.type == MOUSEBUTTONDOWN:
			if self.checkMouse (mouse, 26, 60, 550, 570) :
				self._state = "Home"

	def checkMouse (self, mouse, left, right, top, bottom):
		isIn = False
		if mouse[0]	> left and mouse[0] < right \
		and mouse[1] > top and mouse[1] < bottom :
			isIn = True
		return isIn
				
									
	
#setDisplay = pygame.display.set_mode((400,300))
pygame.display.set_caption('Jungle Jamboree')
imgStart = pygame.image.load('Images/StartScreen.png')
imgJungle = pygame.image.load('Images/HomeScreen.png')
imgStore = pygame.image.load('Images/Shopkeep.png')
imgInventory = pygame.image.load('Images/Inventory.png')
imgPerson1 = pygame.image.load('Images/Person1.png')
imgPerson2 = pygame.image.load('Images/Person2.png')
imgPerson3 = pygame.image.load('Images/Person3.png')
imgPerson4 = pygame.image.load('Images/Person4.png')
imgPerson5 = pygame.image.load('Images/Person5.png')
imgx = 0
imgy = 0
imgxP1 = 158
imgyP1 = 134
imgxP2 = 190
imgyP2 = 145
imgxP3 = 230
imgyP3 = 90
imgxP4 = 165
imgyP4 = 95
imgxP5 = 190
imgyP5 = 100


testGame = Game()
start = testGame._myFont3.render("START", 1, (255,255,255))
store = testGame._myFont3.render("STORE", 1, (255,255,255))
forage = testGame._myFont3.render("FORAGE", 1, (255,255,255))
inventory = testGame._myFont3.render("INVENTORY", 1, (255,255,255))
party = testGame._myFont3.render("PARTY", 1, (255,255,255))
day = testGame._myFont3.render("DAY:", 1, (255,255,255))
distance = testGame._myFont3.render("DISTANCE:", 1, (255,255,255))
funds = testGame._myFont3.render("MONEY:", 1, (255,255,255))
leave1 = testGame._myFont3.render("LEAVE", 1, (0,0,0))
leave2 = testGame._myFont3.render("LEAVE", 1, (255,255,255))
testGame.on_loop()

