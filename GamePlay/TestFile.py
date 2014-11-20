#!/usr/bin/python
##################################
# File Name: TestFile.py
# Author: 	 Group 3
# Date: 	 11/10/2014
# Class:	 CS360
# Assignment:Jungle Jamboree
# Purpose: 	 To test the pygame
##################################

import pygame 
import sys
from pygame.locals import *

#initalizes
pygame.init ()
#colors
white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

yellow = (255,255,0)
cyan = (0,255,255)
purple = (255,0,255)



#creates the window, parameters for width, heigth, depth and color. measurement done in pixels
#color goes RGB, followed by an alpha, but that is optional
setDisplay = pygame.display.set_mode((400,300))

#creates the title
pygame.display.set_caption('Jungle Jamboree')

"""
#colors the background
setDisplay.fill(yellow)

#colors a single pixel
singlePixel = pygame.PixelArray(setDisplay)
singlePixel[3][3] = yellow

#draws a single line (display, color, start point, end point, width)
pygame.draw.line(setDisplay,blue,(389,200), (370,70), 4)

#draws a cirle (display, color, center of circle, radius, and an optional thickness) is no thickness is given, it auto fills
pygame.draw.circle(setDisplay, red, (50,50), 20)
pygame.draw.circle(setDisplay, red, (100,100), 20,10)

#draws a rectangle (display, color, (topleft point, total width, total height))
pygame.draw.rect(setDisplay, purple, (200,200, 22, 22))

#draw a polygon
pygame.draw.polygon(setDisplay,green, ((50,20),(30,40),(60,100),(200,100),(3,3)))
"""

#saves image into a variable
img = pygame.image.load('Images/TestBackground.png')
imgx = 0
imgy = 0

#Game loop
while True:
	setDisplay.blit(img, (imgx,imgy))
	for event in pygame.event.get():
		#allows you to see what the last input was in the geany output window
		print event
		#called when you hit the X
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	#the update for the screen		
	pygame.display.update()
