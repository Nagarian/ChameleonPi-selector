#! /usr/bin/python
# -*- coding: utf-8 -*- 

from folderExplorer import FolderExplorer
import pygame
import singleton as Singleton
import os
# import IFrame

class GameChoiceMenu:#(IFrame):
	"""Cette classe va permettre de choisir un jeu en fonction de l'emulateur choisis"""

	_startpos = 250
	_itemheight = 40
	_limitpos = 900
	_listleft = -1
	_selectmarge = 50
	_selectleft = -1
	_selwidth = 700
	_visibleitems = -1

	_img_folder_icon = None
	_font_item = None
	_font_itemsel = None
	background = None
	returnSound = None

	def __init__(self, arguments=None):
		# self.title = "CHAMELEONPI"
		self.returnCode, self.emulator = arguments
		
		self.img_icon = self.emulator["image"]
		# self.img_title = None
		self.img_subtitle = None

		self.folderItems = None

		self.current = 0
		self.offset = 0
		self.nitems = 0

		if GameChoiceMenu._listleft == -1:
			GameChoiceMenu._listleft = Singleton.SCREEN_WIDTH / 2 #900
		if GameChoiceMenu._selectleft == -1:
			GameChoiceMenu._selectleft = GameChoiceMenu._listleft - GameChoiceMenu._selectmarge
		if GameChoiceMenu._visibleitems == -1:
			GameChoiceMenu._visibleitems = (GameChoiceMenu._limitpos - GameChoiceMenu._startpos) / GameChoiceMenu._itemheight

	def LoadContent(self):
		if GameChoiceMenu.background == None:
			GameChoiceMenu.background = pygame.image.load("resources/gamebackground.%dx%d.png" % (Singleton.SCREENWIDTH, Singleton.SCREENHEIGHT)).convert()
			if Singleton.CONV_X != 1 or Singleton.CONV_Y != 1:
				GameChoiceMenu.background = pygame.transform.scale( GameChoiceMenu.background, (int(GameChoiceMenu.background.get_width() * Singleton.CONV_X), int(GameChoiceMenu.background.get_height() * Singleton.CONV_Y)) )
		if GameChoiceMenu.returnSound == None:
			GameChoiceMenu.returnSound = pygame.mixer.Sound("resources/sound/navigation.ogg")

		if self.img_icon != None:
			w = 500
			h = w / float(self.img_icon.get_width()) * float(self.img_icon.get_height())
			self.img_icon = pygame.transform.scale( self.img_icon, (int(w * Singleton.CONV_X), int(h *Singleton.CONV_Y)) )

		font_title = pygame.font.Font(Singleton.FONT_NAME, int(48*Singleton.CONV_Y))
		font_subtitle = pygame.font.Font(Singleton.FONT_NAME, int(28*Singleton.CONV_Y))
		
		if GameChoiceMenu._font_item == None:
			GameChoiceMenu._font_item = pygame.font.Font(Singleton.FONT_NAME2, int(26*Singleton.CONV_Y))

		if GameChoiceMenu._font_itemsel == None:
			GameChoiceMenu._font_itemsel = pygame.font.Font(Singleton.FONT_NAME2, int(20*Singleton.CONV_Y))


		GameChoiceMenu._img_folder_icon = pygame.image.load("resources/folder.png")
		if Singleton.CONV_X != 1 or Singleton.CONV_Y != 1:
			GameChoiceMenu._img_folder_icon = pygame.transform.scale( self.emulator["romsFolder"], (int(GameChoiceMenu._img_folder_icon.get_width() * Singleton.CONV_X), int(GameChoiceMenu._img_folder_icon.get_height() *Singleton.CONV_Y)) )

		# self.img_title = font_title.render(self.title, 1, (50,50, 50))
		self.img_subtitle = font_title.render(self.emulator["name"], 1, (50,50, 50))

		self.folderItems = FolderExplorer(self.emulator["romsFolder"], self.emulator["extensionAllowed"])

	def UnloadContent(self):
		pass

	def Update(self, event):
		if (event.type == pygame.KEYDOWN and event.key == Singleton.KEY_BUT_EXIT) or (event.type == pygame.QUIT) :
			return ("RETURN", None)

		if event.type == pygame.KEYDOWN :
			if event.key == Singleton.KEY_BUT_VALIDATE :
				cpos = self.current - self.offset
				fname = self.folderItems.fileItemsAllowed[cpos]["value"]
				if os.path.isdir( fname ) :
					self.folderItems.loadFolder( fname )
				else:
					return ("EXIT", self.returnCode, self.folderItems.fileItemsAllowed[self.current]["value"])

			elif event.key == Singleton.KEY_DIR_UP :
				GameChoiceMenu.returnSound.play()
				self.current -= 1
				if self.current < self.offset:
					self.offset = self.current
	
			elif event.key == Singleton.KEY_DIR_DOWN :
				GameChoiceMenu.returnSound.play()
				self.current += 1
				if self.current - self.offset >= GameChoiceMenu._visibleitems:
					self.offset +=1

			elif event.key == Singleton.KEY_BUT_SCROLL_DOWN :
				GameChoiceMenu.returnSound.play()
				self.current += GameChoiceMenu._visibleitems
				self.offset += GameChoiceMenu._visibleitems
				if self.current - self.offset >= GameChoiceMenu._visibleitems:
					self.offset = self.current

			elif event.key == Singleton.KEY_BUT_SCROLL_UP :
				GameChoiceMenu.returnSound.play()
				self.current -= GameChoiceMenu._visibleitems
				self.offset -= GameChoiceMenu._visibleitems
			
		if self.current - self.offset >= GameChoiceMenu._visibleitems:
			self.offset = self.current
		if self.current < 0:
			self.current = 0
		if self.current >= self.folderItems.itemsAllowedCount:
			self.current = self.folderItems.itemsAllowedCount-1

		if (self.current < self.offset) or (self.current >= self.offset+GameChoiceMenu._visibleitems):
			self.offset = self.current

		if self.offset >= self.folderItems.itemsAllowedCount - GameChoiceMenu._visibleitems:
			self.offset = self.folderItems.itemsAllowedCount - GameChoiceMenu._visibleitems
		if self.offset < 0:
			self.offset = 0
		return ("CONTINUE", None)


	def Draw(self, screen):
		screen.blit( GameChoiceMenu.background, (0,0))

		if self.img_icon != None:
			self.paintElement( screen, self.img_icon, 75, ((Singleton.SCREEN_HEIGHT - self.img_icon.get_height()) / 2 ))#225,400

		# self.paintElement( screen, self.img_title, 95, 96 ) #225,146
		self.paintElement( screen, self.img_subtitle, 75 + ((self.img_icon.get_width() - self.img_subtitle.get_width()) / 2) , ((Singleton.SCREEN_HEIGHT + self.img_icon.get_height()) / 2 ) + 10  ) #225,200

		cpos = self.current - self.offset
		rectsel = pygame.Rect( GameChoiceMenu._selectleft * Singleton.CONV_X, (GameChoiceMenu._startpos + cpos * GameChoiceMenu._itemheight - 3) * Singleton.CONV_Y, GameChoiceMenu._selwidth * Singleton.CONV_X, GameChoiceMenu._itemheight * Singleton.CONV_Y - 2 )
		screen.fill((187,17,66), rectsel )

		pospaint=0

		for compta in range(0, min(GameChoiceMenu._visibleitems, self.folderItems.itemsAllowedCount )) :
			item = self.folderItems.fileItemsAllowed[compta+self.offset]
			leftpad = 0

			if os.path.isdir( item["value"] ) :
				self.paintElement( screen, GameChoiceMenu._img_folder_icon, GameChoiceMenu._listleft , GameChoiceMenu._startpos + (GameChoiceMenu._itemheight * pospaint) + 4 )
				leftpad = 50

			img_item = GameChoiceMenu._font_item.render(item["name"], 1, (50,50,50) if pospaint != cpos else (255,255,255))
			self.paintElement( screen, img_item, GameChoiceMenu._listleft + leftpad, GameChoiceMenu._startpos + (GameChoiceMenu._itemheight * pospaint), GameChoiceMenu._selwidth - GameChoiceMenu._selectmarge * 2)

			if( img_item.get_width() >= GameChoiceMenu._selwidth - GameChoiceMenu._selectmarge * 2 ):

				img_item = GameChoiceMenu._font_item.render("...", 1, (50,50,50) if pospaint != cpos else (255,255,255))
				self.paintElement( screen, img_item, GameChoiceMenu._listleft + GameChoiceMenu._selwidth - GameChoiceMenu._selectmarge * 2, GameChoiceMenu._startpos + (GameChoiceMenu._itemheight * pospaint) )
			
			pospaint += 1


		#	if FileSelector.startpos + (FileSelector.itemh * pospaint) >= FileSelector.limitpos:
		#		break

		img_item = GameChoiceMenu._font_itemsel.render("...", 1, (187,17,66))

		if self.offset + GameChoiceMenu._visibleitems < self.folderItems.itemsAllowedCount:
			self.paintElement( screen, img_item, GameChoiceMenu._selectleft ,  GameChoiceMenu._limitpos )

		if self.offset > 1:
			self.paintElement( screen, img_item, GameChoiceMenu._selectleft,  GameChoiceMenu._startpos - 30 )


		rectsel = pygame.Rect( (GameChoiceMenu._listleft + GameChoiceMenu._selwidth) * Singleton.CONV_X, GameChoiceMenu._startpos * Singleton.CONV_Y, 8 * Singleton.CONV_X, (GameChoiceMenu._limitpos - GameChoiceMenu._startpos) * Singleton.CONV_Y )
		screen.fill((220,220,220), rectsel )

		if float(self.folderItems.itemsAllowedCount - 1) > 0:
			npos = GameChoiceMenu._startpos + float(self.current) * float(GameChoiceMenu._limitpos - GameChoiceMenu._startpos) / float(self.folderItems.itemsAllowedCount - 1)
		else:
			npos = GameChoiceMenu._startpos

		pygame.draw.circle ( screen, (180, 180, 180), (int( (GameChoiceMenu._listleft + GameChoiceMenu._selwidth + 4) * Singleton.CONV_X), int(npos * Singleton.CONV_Y)), 10)


	@classmethod
	def paintElement(cls, screen, imatge, px, py, mw = 0):
		mw *= Singleton.CONV_X
		screen.blit( imatge, (px*Singleton.CONV_X, py*Singleton.CONV_Y), (0, 0, mw if mw != 0 else imatge.get_width(), imatge.get_height()) );


