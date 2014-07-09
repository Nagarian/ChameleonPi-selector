#! /usr/bin/python
# -*- coding: utf-8 -*- 

import pygame
import singleton as Singleton
import random

class ScreenSaver:#(IFrame):
	"""This class show you how to implement a new frame"""
	# this variable allow to stop displaying screensaver
	display = False

	def __init__(self):
		self.lastImageChange = 0
		self.picture = None
		self.realDisplay = False
		pygame.DISPLAY_SCREENSAVER = pygame.USEREVENT + 3

	def LoadContent(self):
		self.LoadImage()

	def UnloadContent(self):
		pass

	def Update(self, event):
		if event.type == pygame.KEYDOWN:
			self.realDisplay = False

			ScreenSaver.display = False

			if event.key == Singleton.KEY_BUT_SCREENSAVER:
				self.realDisplay = True

		if not ScreenSaver.display:
			pygame.time.set_timer(pygame.DISPLAY_SCREENSAVER, 0)
			pygame.time.set_timer(pygame.DISPLAY_SCREENSAVER, 300000)
			ScreenSaver.display = True

		if event.type == pygame.DISPLAY_SCREENSAVER:
			pygame.time.set_timer(pygame.DISPLAY_SCREENSAVER, 0)
			self.realDisplay = True

		if self.realDisplay:
			if pygame.time.get_ticks() > (self.lastImageChange + 15000):
				self.lastImageChange = pygame.time.get_ticks()
				self.LoadImage()

		return ("CONTINUE", None)
		
	def Draw(self, screen):
		if self.realDisplay:
			screen.fill((0,0,0))
			screen.blit( self.picture, (0 - (self.picture.get_width() - Singleton.SCREENWIDTH) / 2, 0 - (self.picture.get_height() - Singleton.SCREENHEIGHT) / 2) )

	def LoadImage(self):
		self.picture = pygame.image.load( "resources/" + "error/error"+ ( "%02d" % random.randrange( 1, 18) ) + ".png" )
		if Singleton.CONV_X != 1 or Singleton.CONV_Y != 1:
			self.picture = pygame.transform.scale( self.picture, (int(self.picture.get_width() * Singleton.CONV_X), int(self.picture.get_height() * Singleton.CONV_Y)) )