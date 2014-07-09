#! /usr/bin/python
# -*- coding: utf-8 -*- 

import sys
import os
import pygame

import time

import singleton as Singleton
from configuration.selectorConfig import *
from frameCollection import FrameManager
from frame.gamechoice import GameChoiceMenu
from frame.emchoice import EmulatorChoiceMenu
from frame.options import OptionsMenu
from frame.screensaver import ScreenSaver

pygame.init()
pygame.mixer.init()
pygame.font.init()
pygame.mouse.set_visible( False )
pygame.key.set_repeat(200, 300)

fpsControl = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

tada = pygame.mixer.Sound("resources/sound/startup.ogg")
navigationSound = pygame.mixer.Sound("resources/sound/validation.ogg")
returnSound = pygame.mixer.Sound("resources/sound/cancel.ogg")

def drawimage( filename ):
	off = pygame.image.load(filename)
	if Singleton.CONV_X != 1 or Singleton.CONV_Y != 1:
		off = pygame.transform.scale( off, (int(off.get_width() * Singleton.CONV_X), int(off.get_height() * Singleton.CONV_Y)) )
	screen.blit( off, (0,0))

if os.path.exists("boot"):
	drawimage("resources/splash.%dx%d.png" % (Singleton.SCREENWIDTH, Singleton.SCREENHEIGHT))
	os.remove("boot")
	pygame.display.update()

tada.play()

ft = pygame.image.load("resources/fons.png").convert()

# Singleton.SCREENWIDTH = Singleton.SCREEN_WIDTH
# Singleton.SCREENHEIGHT = Singleton.SCREEN_HEIGHT
# Singleton.CONV_X = float( SCREENWIDTH ) / float( SCREEN_WIDTH )
# Singleton.CONV_Y = float( SCREENHEIGHT ) / float( SCREEN_HEIGHT )

if Singleton.CONV_X != 1 or Singleton.CONV_Y != 1:
	ft = pygame.transform.scale( ft, (int(ft.get_width() * Singleton.CONV_X), int(ft.get_height() * Singleton.CONV_Y)) )

clock = pygame.time.Clock()

frameStack = FrameManager()

frameStack.push(EmulatorChoiceMenu())

screenSave = ScreenSaver()
screenSave.LoadContent()
action = None

while True:
	event = pygame.event.poll()
	
	action = frameStack.Update(event)
	if action[0] != "CONTINUE":
		if action[0] == "EXIT":
			if len(action) == 3:
				print action[2]
			sys.exit(action[1])

		if action[0] == "RETURN":
			returnSound.play()
			frameStack.pop()

		if action[0] == "NAVIGATE":
			navigationSound.play()
			pygame.event.clear()
			newFrame = None
			if action[1] == "GameChoiceMenu":
				newFrame = GameChoiceMenu(action[2])
			elif action[1] == "OptionsMenu":
				newFrame = OptionsMenu()
			
			if newFrame != None:
				frameStack.push(newFrame)


	screenSave.Update(event)


	# screen.fill((230,230,230))
	screen.blit( ft, (0,0))


	frameStack.Draw(screen)
	screenSave.Draw(screen)

	pygame.display.update()

	fpsControl.tick(60)