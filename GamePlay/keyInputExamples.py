#!/usr/bin/python
##################################
# File Name: KeyInputExamples.py
# Author: 	 Group 3
# Date: 	 11/10/2014
# Class:	 CS360
# Assignment:Jungle Jamboree
# Purpose: 	 To test keyinput
##################################

import pygame 
import sys
from pygame.locals import *

#initalizes
pygame.init ()
#colors
white = (255,255,255)
black = (0,0,0)
bg = black

#frams per second and resolution
fps = 30
dispWidth = 800
dispHeight = 600
cellSize = 5

#directions
UP = 'up'
DOWN = 'down'
RIGHT = 'right'
LEFT = 'left'


def msgSurface(text, textColor):
	smallText = pygame.font.Font('freesansbold.ttf',20)
	largeText = pygame.font.Font('freesansbold.ttf', 150)
	
	titleTextSurf, titleTextRect = makeTextObjs(text, largeText, textColor)
	titleTextRect.center = (int(dispWidth/2), int(dispHeight/2)
	setDisplay.blit(titleTextSurf,titleTextRect)
	
	typeTextSurf, typeTextRect = makeTextObjs('Press key to continue', smallText, white)
	typeTextRect.center = (int(dispWidth/2), int(dispHeight/2) + 120)
	setDisplay.blit(typTextSurf, typTextRect)
	pygame.display.update ()
	fpsTime.tick()
	
	while whatNext() == None:
		for event in pygame.event.get([QUIT]):
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		
		pygame.display.update()
		fpsTime.tick()
		
	runGame()


#gameloops
def runGame():
	startx = 3
	starty = 3
	coords = [{'x':startx, 'y':starty}]
	direction = RIGHT
	
	while True:
		for event in pygame.event.get ():
			print event
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
				
			#Good for programming to use elif
			elif event.type == KEYDOWN:
				if event.key == (K_LEFT):
					direction = LEFT
				elif event.key == (K_RIGHT):
					direction = RIGHT
				elif event.key == (K_UP):
					direction = UP
				elif event.key == (K_DOWN):
					direction = DOWN
					
			if direction == UP:
				#newCell = new dictionary values from cell from coords
				newCell = {'x':coords[0]['x'], 'y':coords[0]['y'] -1}
				
			elif direction == DOWN:
				newCell = {'x':coords[0]['x'], 'y':coords[0]['y'] +1}
				
			elif direction == LEFT:
				newCell = {'x':coords[0]['x'] -1, 'y':coords[0]['y']}
				
			elif direction == RIGHT:
				newCell = {'x':coords[0]['x'] +1, 'y':coords[0]['y']}
				
			del coords[-1]
			
			# Adds it to the coords dictionary
			coords.insert(0, newCell)
			setDisplay.fill(bg)
			drawCell(coords)
			pygame.display.update()
			fpsTime.tick(fps)
			
			if(newCell['x'] < 0 or newCell['y'] < 0 or newCell['x'] > dispWidth or newCell['y'] > dispHeight):
				print 'You are off Screen'
			
#function to draw the cell to screen			
def drawCell(coords):
	for coord in coords:
		x = coord['x']*cellSize
		y = coord['y']*cellSize
		makeCell = pygame.Rect(x,y,cellSize,cellSize)
		pygame.draw.rect(setDisplay, white, makeCell)
		
while True:
	global fpsTime
	global setDisplay
	
	fpsTime = pygame.time.Clock()
	setDisplay = pygame.display.set_mode((dispWidth,dispHeight))
	pygame.display.set_caption('My First controllable object')
	runGame ()
	
