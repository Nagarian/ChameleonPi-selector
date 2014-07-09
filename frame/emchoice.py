#! /usr/bin/python
# -*- coding: utf-8 -*- 

import pygame
import singleton as Singleton
from frame.screensaver import ScreenSaver
# import IFrame
# from enum import Enum

class EmulatorChoiceMenu: #(IFrame):
	"""docstring for EmulatorChoiceMenu"""
	font = None
	font2 = None
	moving_dist = Singleton.SCREENWIDTH / 2
	background = None
	color_pink = (187,17, 66)
	navigationSound = None
	validationSound = None

	def __init__(self):
		self.nom = None
		self.info = None
		self.help1 = None
		self.help2 = None

		self.isMoving = False
		self.directionMoving = Direction.none

		self.moving_start = 0
		self.moving_duration = 180

		# current moving for displaying element
		self.offsetX = 0

		self.showinfo = False
		self.current = 0

		self.emulatorItems = []
		self.emulatorCount = 0

		self.gleft = False
		self.gright= False

		self.axisval = 0

		# if pygame == None:
		# 	if pyGame == None:
		# 		raise Exception("This class need pygame to run")
		# 	pygame = pyGame

	def LoadContent(self):
		if EmulatorChoiceMenu.font == None:
			EmulatorChoiceMenu.font = pygame.font.Font(Singleton.FONT_NAME, int(100*Singleton.CONV_Y))
		if EmulatorChoiceMenu.font2 == None:
			EmulatorChoiceMenu.font2 = pygame.font.Font(Singleton.FONT_NAME2, int(22*Singleton.CONV_Y))
		if EmulatorChoiceMenu.background == None:
			EmulatorChoiceMenu.background = pygame.image.load("resources/fonstram.%dx%d.png" % (Singleton.SCREENWIDTH, Singleton.SCREENHEIGHT)).convert()
			if Singleton.CONV_X != 1 or Singleton.CONV_Y != 1:
				EmulatorChoiceMenu.background = pygame.transform.scale( EmulatorChoiceMenu.background, (int(ft.get_width() * Singleton.CONV_X), int(ft.get_height() * Singleton.CONV_Y)) )
		if EmulatorChoiceMenu.navigationSound == None:
			EmulatorChoiceMenu.navigationSound = pygame.mixer.Sound("resources/sound/navigation.ogg")
		if EmulatorChoiceMenu.validationSound == None:
			EmulatorChoiceMenu.validationSound = pygame.mixer.Sound("resources/sound/validation.ogg")
		self.loadConsole()
		
		self.nom = EmulatorChoiceMenu.font.render( self.emulatorItems[self.current]["name"], 1, (60,60, 60) )
		self.info = EmulatorChoiceMenu.font2.render( self.emulatorItems[self.current]["info"], 1, EmulatorChoiceMenu.color_pink )
		self.help1 = EmulatorChoiceMenu.font2.render("ONLINE HELP: E- Emulator , C - Computer , W - Emulator official site", 1, EmulatorChoiceMenu.color_pink)
		self.help2 = EmulatorChoiceMenu.font2.render("H - HELP , O - Extra menu", 1, EmulatorChoiceMenu.color_pink)

		pygame.DISPLAY_INFO = pygame.USEREVENT + 1
		pygame.time.set_timer(pygame.DISPLAY_INFO, 3000)

	def UnloadContent(self):
		pass

	def Update(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == Singleton.KEY_BUT_EXIT:
				return ("EXIT", 1)

			if event.key == Singleton.KEY_BUT_SHUTDOWN:
				return ("EXIT", 0)

			if event.key == Singleton.KEY_BUT_EXIT_FOR_BASH :
				return ("EXIT", 101)

			if event.key == Singleton.KEY_BUT_OPTION_MENU:
				return ("NAVIGATE", "OptionsMenu")

			if event.key == Singleton.KEY_BUT_VALIDATE or event.key == Singleton.KEY_BUT_CHOOSE_EMULATOR_1:
				EmulatorChoiceMenu.validationSound.play()
				return ("NAVIGATE", "GameChoiceMenu", (self.current + 2, self.emulatorItems[self.current]))

			if event.key == Singleton.KEY_BUT_CHOOSE_EMULATOR_2 :
				EmulatorChoiceMenu.validationSound.play()
				return ("NAVIGATE", "GameChoiceMenu", (self.current + 2 + 50, self.emulatorItems[self.current]))

			if event.key == Singleton.KEY_BUT_CHOOSE_EMULATOR_3 :
				EmulatorChoiceMenu.validationSound.play()
				return ("NAVIGATE", "GameChoiceMenu", (self.current + 2 + 70, self.emulatorItems[self.current]))

			if event.key == Singleton.KEY_BUT_HELP_EMULATOR_OFFI:
				EmulatorChoiceMenu.surf ( self.emulatorItems[self.current]["extemula"] );
			if event.key == Singleton.KEY_BUT_HELP_ENGINE:
				EmulatorChoiceMenu.surf ( self.emulatorItems[self.current]["computer"] );
			if event.key == Singleton.KEY_BUT_HELP_EMULATOR:
				EmulatorChoiceMenu.surf ( self.emulatorItems[self.current]["emula"] );

			if event.key == Singleton.KEY_BUT_HELP_CHAMELEON:
				EmulatorChoiceMenu.surf ( "file:///roms/README.html" );

			if event.key == Singleton.KEY_DIR_LEFT or event.key == Singleton.KEY_DIR_RIGHT:
				EmulatorChoiceMenu.navigationSound.play()
				if not self.isMoving:
					self.isMoving = True
					self.directionMoving = Direction.left if event.key == Singleton.KEY_DIR_LEFT else Direction.right
					self.moving_start = pygame.time.get_ticks()
				else:
					pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=event.key))


			if event.key == Singleton.KEY_BUT_SHOW_INFO:
				self.showinfo = True

		if self.isMoving:
			moving_time = pygame.time.get_ticks() - self.moving_start
			if moving_time >= self.moving_duration:
				self.offsetX = 0
				self.current = (self.current - self.directionMoving) % self.emulatorCount
				self.isMoving = False
				pygame.time.set_timer(pygame.DISPLAY_INFO, 3000)
				# erase emulator name and display info
				self.nom = EmulatorChoiceMenu.font.render( self.emulatorItems[self.current]["name"], 1, (60,60, 60) )
				self.info = EmulatorChoiceMenu.font2.render( self.emulatorItems[self.current]["info"], 1, (187,17, 66) )
			else:
				self.offsetX = EmulatorChoiceMenu.moving_dist * moving_time / self.moving_duration * self.directionMoving
			ScreenSaver.display = False
			self.showinfo = False

		if event.type == pygame.DISPLAY_INFO:
			self.showinfo = True
			pygame.time.set_timer(pygame.DISPLAY_INFO, 0)

		return ("CONTINUE", None)


	def Draw(self, screen):
		screen.blit( EmulatorChoiceMenu.background, (0,0))
		if self.isMoving == False:
			screen.blit( self.nom, (Singleton.SCREENWIDTH / 2 - self.nom.get_width() / 2, Singleton.SCREENHEIGHT - (330 * Singleton.CONV_Y)) )

		if self.showinfo:
			screen.blit( self.info, (Singleton.SCREENWIDTH - (Singleton.SCREENWIDTH / 5) - self.info.get_width(), Singleton.SCREENHEIGHT - (165 * Singleton.CONV_Y)) )

			screen.blit( self.help1, ((Singleton.SCREENWIDTH - (Singleton.SCREENWIDTH / 5) ) - self.help1.get_width(), Singleton.SCREENHEIGHT - (135 * Singleton.CONV_Y)))
			screen.blit( self.help2, ((Singleton.SCREENWIDTH - (Singleton.SCREENWIDTH / 5) ) - self.help2.get_width(), Singleton.SCREENHEIGHT - (935 * Singleton.CONV_Y)))


		self.paintElement( screen, self.emulatorItems[self.current]["image"], self.offsetX )
		self.paintElement( screen, self.emulatorItems[((self.current + 1) % self.emulatorCount)]["image"], self.offsetX + Singleton.SCREENWIDTH / 2)
		self.paintElement( screen, self.emulatorItems[((self.current - 1) % self.emulatorCount)]["image"], self.offsetX - Singleton.SCREENWIDTH / 2)


		if self.directionMoving == Direction.right:
			self.paintElement( screen, self.emulatorItems[((self.current + 2) % self.emulatorCount)]["image"], +Singleton.SCREENWIDTH)
		
		if self.directionMoving == Direction.left:
			self.paintElement( screen, self.emulatorItems[((self.current - 2) % self.emulatorCount)]["image"], - Singleton.SCREENWIDTH)


	@classmethod
	def paintElement(cls, screen, image , px ):
		#dy =  abs(imatge.get_width()/2+px) / 5 -200
		dy = Singleton.SCREENHEIGHT/2 - (100 * Singleton.CONV_Y ) - image.get_height() / 2
		dx = Singleton.SCREENWIDTH/2 - image.get_width()/2 + px

		screen.blit( image, (dx, dy) );

	@classmethod
	def surf(cls, website):
		import os
		os.system( "/usr/bin/netsurf-ch "+website+" > /opt/selector/surf.log 2>&1" )
		# import webbrowser
		# webbrowser.open(website)


	def loadConsole(self):
		items = []
		ins = open( "configuration/machines.conf", "r" )
		for line in ins:
			line = line.replace("\r\n", "")
			line = line.replace("\n", "")
			if line.startswith("#"):
				continue
			newitem = line.split("|")
			img = pygame.image.load("resources/consoles/" + newitem[1]).convert_alpha()
			if Singleton.CONV_X != 1 or Singleton.CONV_Y != 1:
				img = pygame.transform.scale( img, (int(img.get_width() * Singleton.CONV_X), int(img.get_height() *Singleton.CONV_Y)) )

			extensionAllow = []

			for x in xrange(7,len(newitem)):
				extensionAllow.append(newitem[x])

			newIt = {
				"name" : newitem[0],
				"image" : img,
				"info" : newitem[2],
				"extemula" : newitem[3],
				"computer" : newitem[4],
				"emula" : newitem[5],
				"romsFolder" : newitem[6],
				"extensionAllowed" : extensionAllow
			}

			items.append ( newIt )
		ins.close()
		self.emulatorItems = items
		self.emulatorCount = len(self.emulatorItems)


class Direction:#(Enum):
	"""Enumeration for direction we want"""
	right = -1
	left = 1
	none = 0
		