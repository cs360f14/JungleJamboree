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
from Turn import *
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
		self._turn = Turn()
		self._store = Store ()
		self._store.setUpStore ()
		self._party.setUpParty () 
		self._state = "Start"
		self._width = 800
		self._height = 600
		self._size = (self._width, self._height)
		pygame.init()
		pygame.font.init()
		self._display = pygame.display.set_mode(self._size)
		self._myFont1 = pygame.font.Font('freesansbold.ttf', 15)
		self._myFont2 = pygame.font.Font('freesansbold.ttf', 25)
		self._myFont3 = pygame.font.Font('freesansbold.ttf', 12)
		pygame.display.set_caption('Jungle Jamboree')
	
	def on_loop (self):
		self._display.blit(imgStart, (0,0))
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
					
				if self._party.checkPartyDead () :
					self._state == "GameOver"
					self.gameOver ()
					
				if self._state == "GameOver":
					self.gameOver ()
					
				elif self._state == "Start":
					self.startButton (mouse, event)
															
				elif self._state == "Store":
					self.store (mouse, event)
										
				elif self._state == "Home":
					self.home (mouse, event)
									
				elif self._state == "Inventory":
					self.inventory (mouse, event)
					
				elif self._state == "Party":
					self.party (mouse, event)
					
				elif self._state == "Forage":
					self.forage (mouse, event)
					
				elif self._state == "Travel":
					self.travel (mouse, event)
					pass

			#the update for the screen		
			pygame.display.update()
			
	def startButton (self, mouse, event) :
		if event.type == MOUSEBUTTONDOWN:
			if self.checkMouse (mouse, 395, 460, 395, 415) :
				self._state = "Store"
				
	def travel (self, mouse, event) :
		self._display.blit(imgTravel, (0, 0))
		self._display.blit(leave1, (20, 550))
		self._turn.updateTurn(self._party, self._display)
		pygame.display.update()
		
		waitEvent = pygame.event.wait()
			
		while not (waitEvent.type == MOUSEBUTTONDOWN and  \
		self.checkMouse (mouse, 20, 60, 550, 570)) :
			mouse = pygame.mouse.get_pos()	
			waitEvent = pygame.event.wait()
			
		self._state = "Home"	
							
	def store (self, mouse, event) :
		self._display.blit(imgStore, (0, 0))
		self._display.blit(leave1, (20, 550))
		self._store.menu (self._party, self._display, mouse, event)
		option = self._store.getItemSelection(mouse, event)
		if event.type == MOUSEBUTTONDOWN:
			if self.checkMouse (mouse, 20, 60, 550, 570) :
				self._state = "Home"
							
	def home (self, mouse, event) :

		self.displayHome (mouse, event)
		if event.type == MOUSEBUTTONDOWN:
			if self.checkMouse (mouse, 8, 95, 380, 405) :
				self._state = "Store"
		
		if event.type == MOUSEBUTTONDOWN:
			if self.checkMouse (mouse, 8, 160, 410, 435) :
				self._state = "Forage"
				
		if event.type == MOUSEBUTTONDOWN:
			if self.checkMouse (mouse, 8, 160, 440, 465) :
				self._state = "Inventory"
				
		if event.type == MOUSEBUTTONDOWN:
			if self.checkMouse (mouse, 8, 95, 470, 500) :
				self._state = "Party"
				
		if event.type == MOUSEBUTTONDOWN:			
			if self.checkMouse (mouse, 8, 95, 500, 535) :
				self._state = "Travel"
	
	def displayHome (self, mouse, event) :
		self._display.blit(imgJungle, (0, 0))
		explorersDead = []
		for person in self._party.generatePerson():
			explorersDead.append(person.getHealthTitle ())
		if not explorersDead[0] == "Dead":	
			self._display.blit(imgPerson1, (281, 400))
		if not explorersDead[1] == "Dead":
			self._display.blit(imgPerson2, (386, 407))
		if not explorersDead[2] == "Dead":
			self._display.blit(imgPerson3, (200, 380))
		if not explorersDead[3] == "Dead":
			self._display.blit(imgPerson4, (145, 400))
		if not explorersDead[4] == "Dead":
			self._display.blit(imgPerson5, (563, 440))
		self._display.blit(store, (10, 380))
		self._display.blit(forage, (10, 410))
		self._display.blit(inventory, (10, 440))
		self._display.blit(party, (10, 470))
		
		travelFont = self._myFont2.render("TRAVEL", 1, (255,255,255))	
		self._display.blit(travelFont, (10, 500))
		self._turn.displayMenu(self._party, self._display)
		"""		
		dayString = "DAY:  " + str(self._turn.getDay())
		day = self._myFont2.render(dayString, 1, (255,255,255))	
		self._display.blit(day, (300, 270))
		
		disString = "DISTANCE:  " + str(self._turn.getDistance())
		distance = self._myFont2.render(disString, 1, (255,255,255))	
		self._display.blit(distance, (300, 300))
		
		foodString = "FOOD AMOUNT:  " + str(self._party.getFood())
		food = self._myFont2.render(foodString, 1, (255,255,255))	
		self._display.blit(food, (300, 330))
		"""				
	def forage (self, mouse, event) :
		self._display.blit(imgForage, (0, 0))
		self._display.blit(leave1, (750, 575))
		self._turn.forageEvent(self._party, self._display)
		if event.type == MOUSEBUTTONDOWN:
			if self.checkMouse (mouse, 750, 800, 550, 600) :
				self._state = "Home"
		
	def inventory (self, mouse, event) :
		self._display.blit(imgInventory, (0, 0))
		self._display.blit(leave2, (20, 550))
		self._party.getInventory().displayInventory(mouse, event, \
		self._display)

		if event.type == MOUSEBUTTONDOWN:
			if self.checkMouse (mouse, 20, 60, 550, 570) :
				self._state = "Home"

	def checkMouse (self, mouse, left, right, top, bottom):
		isIn = False
		if mouse[0]	> left and mouse[0] < right \
		and mouse[1] > top and mouse[1] < bottom :
			isIn = True
		return isIn

		
	def party (self, mouse, event):
		explorers = []
		explorersStatus = []
		explorersHealth = []
		for person in self._party.generatePerson():
			explorers.append(testGame._myFont2.render(person.getName(), 1, (0,0,0)))
			explorersStatus.append(testGame._myFont2.render(person.getHealthTitle (), 1, (0,0,0)))
			explorersHealth.append(testGame._myFont2.render(str(person.getHealth ()), 1, (0,0,0)))

		self._display.blit(imgParty, (0, 0))
		self._display.blit(imgPerson1, (15, 15))
		self._display.blit(explorers[0], (100, 30))
		self._display.blit(explorersStatus[0], (100, 55))
		self._display.blit(explorersHealth[0], (100, 80))
		self._display.blit(imgPerson2, (15, 215))
		self._display.blit(explorers[1], (100, 230))
		self._display.blit(explorersStatus[1], (100, 255))
		self._display.blit(explorersHealth[1], (100, 280))
		self._display.blit(imgPerson3, (15, 415))
		self._display.blit(explorers[2], (100, 430))
		self._display.blit(explorersStatus[2], (100, 455))
		self._display.blit(explorersHealth[2], (100, 480))
		self._display.blit(imgPerson4, (400, 15))
		self._display.blit(explorers[3], (490, 30))
		self._display.blit(explorersStatus[3], (490, 55))
		self._display.blit(explorersHealth[3], (490, 80))
		self._display.blit(imgPerson5, (400, 215))
		self._display.blit(explorers[4], (490, 230))
		self._display.blit(explorersStatus[4], (490, 255))
		self._display.blit(explorersHealth[4], (490, 280))
		self._display.blit(leave1, (750, 575))
		if event.type == MOUSEBUTTONDOWN:
			if self.checkMouse (mouse, 750, 800, 550, 600) :
				self._state = "Home"
		
	def gameOver (self):
		self._display.blit(imgGameOver, (0, 0))
		mouse = pygame.mouse.get_pos()	
		print "Game Over"
		pygame.display.update ()
		waitEvent = pygame.event.wait()
		
		while not (waitEvent.type == MOUSEBUTTONDOWN ) :
			mouse = pygame.mouse.get_pos()	
			waitEvent = pygame.event.wait()
		
		
		
	
									
	
#setDisplay = pygame.display.set_mode((400,300))
pygame.display.set_caption('Jungle Jamboree')
imgStart = pygame.image.load('Images/StartScreen.png')
imgJungle = pygame.image.load('Images/HomeScreen.png')
imgStore = pygame.image.load('Images/Shopkeep.png')
imgGameOver = pygame.image.load('Images/GameOverScreen.png')
imgParty = pygame.image.load('Images/PartyScreen.png')
imgForage = pygame.image.load('Images/ForageScreen.png')
imgPerson1 = pygame.image.load('Images/Explorer1.png')
imgInventory = pygame.image.load('Images/Inventory.png')
imgPerson2 = pygame.image.load('Images/Explorer2.png')
imgPerson3 = pygame.image.load('Images/Explorer3.png')
imgPerson4 = pygame.image.load('Images/Explorer4.png')
imgPerson5 = pygame.image.load('Images/Explorer5.png')
imgTravel = pygame.image.load('Images/TravelBackground.png')
"""
imgx = 0
imgy = 0
imgxP1 = 281
imgyP1 = 400
imgxP2 = 386
imgyP2 = 407
imgxP3 = 200
imgyP3 = 380
imgxP4 = 145
imgyP4 = 400
imgxP5 = 563
imgyP5 = 440
"""

testGame = Game()
start = testGame._myFont3.render("START", 1, (255,255,255))
store = testGame._myFont2.render("STORE", 1, (255,255,255))
forage = testGame._myFont2.render("FORAGE", 1, (255,255,255))
inventory = testGame._myFont2.render("INVENTORY", 1, (255,255,255))
party = testGame._myFont2.render("PARTY", 1, (255,255,255))
#day = testGame._myFont3.render("DAY:", 1, (255,255,255))
#distance = testGame._myFont3.render("DISTANCE:", 1, (255,255,255))
funds = testGame._myFont3.render("MONEY:", 1, (255,255,255))
leave1 = testGame._myFont3.render("LEAVE", 1, (0,0,0))
leave2 = testGame._myFont3.render("LEAVE", 1, (255,255,255))
testGame.on_loop()

