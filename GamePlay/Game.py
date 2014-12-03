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
		#self._party.setUpParty () #don't forget to add this not in init
		self._state = "Start"
		self._width = 400
		self._height = 300
		self._size = (self._width, self._height)
		pygame.init()
		self._display = pygame.display.set_mode(self._size)
		self._myFont1 = pygame.font.Font('freesansbold.ttf', 15)
		self._myFont2 = pygame.font.Font('freesansbold.ttf', 10)
		self._myFont3 = pygame.font.Font('freesansbold.ttf', 12)
		pygame.display.set_caption('Jungle Jamboree')
	
	def on_loop (self):
		self._display.blit(imgStart, (imgx,imgy))
		self._display.blit(start, (150,145))
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
					if event.type == MOUSEBUTTONDOWN:
						if mouse[0] > 150:
							if mouse[0] < 197:
								if mouse[1] > 145:
									if mouse[1] < 157:
										print("test success")
										self._state = "Store"
										
				
				
				elif self._state == "Store":
					self._display.blit(imgStore, (imgx, imgy))
					self._display.blit(funds, (297, 279))
					self._display.blit(leave1, (20, 279))
					if event.type == MOUSEBUTTONDOWN:
						if mouse[0] > 20:
							if mouse[0] < 60:
								if mouse[1] > 279:
									if mouse[1] < 291:
										self._state = "Home"
					
					
										
				elif self._state == "Home":
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
						if mouse[0] > 8:
							if mouse[0] < 45:
								if mouse[1] > 226:
									if mouse[1] < 233:
										self._state = "Store"
										
					if event.type == MOUSEBUTTONDOWN:
						if mouse[0] > 8:
							if mouse[0] < 69:
								if mouse[1] > 255:
									if mouse[1] < 265:
										self._state = "Inventory"
										
										
				elif self._state == "Inventory":
					self._display.blit(imgInventory, (imgx, imgy))
					self._display.blit(leave2, (20, 279))
					if event.type == MOUSEBUTTONDOWN:
						if mouse[0] > 20:
							if mouse[0] < 60:
								if mouse[1] > 279:
									if mouse[1] < 291:
										self._state = "Home"
					
			#the update for the screen		
			pygame.display.update()

	
#setDisplay = pygame.display.set_mode((400,300))
pygame.display.set_caption('Jungle Jamboree')
imgStart = pygame.image.load('Images/TestBackground.png')
imgJungle = pygame.image.load('Images/JungleBackGround1.png')
imgStore = pygame.image.load('Images/ShopBackground.png')
imgInventory = pygame.image.load('Images/Backpack.png')
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
start = testGame._myFont1.render("START", 1, (255,255,255))
store = testGame._myFont2.render("STORE", 1, (255,255,255))
forage = testGame._myFont2.render("FORAGE", 1, (255,255,255))
inventory = testGame._myFont2.render("INVENTORY", 1, (255,255,255))
party = testGame._myFont2.render("PARTY", 1, (255,255,255))
day = testGame._myFont3.render("DAY:", 1, (255,255,255))
distance = testGame._myFont3.render("DISTANCE:", 1, (255,255,255))
funds = testGame._myFont3.render("MONEY:", 1, (0,0,0))
leave1 = testGame._myFont3.render("LEAVE", 1, (0,0,0))
leave2 = testGame._myFont3.render("LEAVE", 1, (255,255,255))
testGame.on_loop()

