#! /usr/bin/python
# -*- coding: utf-8 -*- 

import os
import pygame
import singleton as Singleton

class OptionsMenu:#(IFrame):
	
	background = None
	font_Title = None
	font_SubTitle = None
	font_Item = None
	startPosition = 343
	itemHeight = 54

	def __init__(self):
		self.allOptions = None
		self.currentOptions = None
		self.current = 0
		self.title = ""
		self.titleImg = None
		self.selectorRectangle = None
		
	def LoadContent(self):
		"""Loading Resources Content"""
		#if any class resources isn't loaded, we load it
		if OptionsMenu.background == None:
			OptionsMenu.background = pygame.image.load("resources/gamebackground.%dx%d.png" % (Singleton.SCREENWIDTH, Singleton.SCREENHEIGHT)).convert()
			if Singleton.CONV_X != 1 or Singleton.CONV_Y != 1:
				OptionsMenu.background = pygame.transform.scale( OptionsMenu.background, (int(OptionsMenu.background.get_width() * Singleton.CONV_X), int(OptionsMenu.background.get_height() * Singleton.CONV_Y)) )

		if OptionsMenu.font_Title == None:
			OptionsMenu.font_Title = pygame.font.Font(Singleton.FONT_NAME, int(28*Singleton.CONV_Y))
		if OptionsMenu.font_SubTitle == None:
			OptionsMenu.font_SubTitle = pygame.font.Font(Singleton.FONT_NAME, int(48*Singleton.CONV_Y))
		if OptionsMenu.font_Item == None:
			OptionsMenu.font_Item = pygame.font.Font(Singleton.FONT_NAME2, int(32*Singleton.CONV_Y))


		self.allOptions = self.LoadConfigSchema()
		self.allOptions["imgValue"] = OptionsMenu.font_SubTitle.render(self.allOptions["name"], 1, (50,50, 50))
		self.titleImg = OptionsMenu.font_Title.render(self.title, 1, (50,50, 50))

		for item in self.allOptions["subItems"]:
			OptionsMenu.toggleElement(item)
			for subItem in item["subItems"]:
				OptionsMenu.toggleElement(subItem)

		self.currentOptions = self.allOptions

		self.selectorRectangle = pygame.Rect(
				(Singleton.SCREENWIDTH / 5) * Singleton.CONV_X - 50,
				(OptionsMenu.startPosition + (self.current * OptionsMenu.itemHeight) - 3) * Singleton.CONV_Y,
				(Singleton.SCREENWIDTH * 3 / 5) * Singleton.CONV_X + 100,
				self.itemHeight * 0.8 * Singleton.CONV_Y )
		OptionsMenu.toggleElement(self.currentOptions["subItems"][self.current], True)

	def UnloadContent(self):
		pass

	def Update(self, event):
		if event.type == pygame.QUIT :
			return ("RETURN", None)

		if event.type == pygame.KEYDOWN :
			OptionsMenu.toggleElement(self.currentOptions["subItems"][self.current])

			if event.key == Singleton.KEY_BUT_EXIT:
				if self.currentOptions["parent"] == None :
					return ("RETURN", None)
				else:
					OptionsMenu.toggleElement(self.currentOptions)
					self.currentOptions = self.currentOptions["parent"]
					self.current = 0 if not self.currentOptions.has_key("lastPositionCursor") else self.currentOptions["lastPositionCursor"]
					self.currentOptions["imgValue"] = OptionsMenu.font_SubTitle.render(self.currentOptions["name"], 1, (50,50, 50))

			if event.key == Singleton.KEY_BUT_VALIDATE :
				if len(self.currentOptions["subItems"][self.current]["subItems"]) == 0 :
					if self.currentOptions["subItems"][self.current]["value"] == 0 :
						if self.currentOptions["parent"] == None :
							return ("RETURN", None)
						OptionsMenu.toggleElement(self.currentOptions)
						self.currentOptions = self.currentOptions["parent"]
						self.current = 0 if not self.currentOptions.has_key("lastPositionCursor") else self.currentOptions["lastPositionCursor"]
						self.currentOptions["imgValue"] = OptionsMenu.font_SubTitle.render(self.currentOptions["name"], 1, (50,50, 50))
					elif self.currentOptions["subItems"][self.current]["cmd"] == None :
						return ("EXIT", self.currentOptions["subItems"][self.current]["value"])
					# else :
					#	scriptToExecute = self.currentOptions["subItems"][self.current]["cmd"]
					#	os.system(scriptToExecute)
				else:
					self.currentOptions["lastPositionCursor"] = self.current
					self.currentOptions = self.currentOptions["subItems"][self.current]
					self.currentOptions["imgValue"] = OptionsMenu.font_SubTitle.render(self.currentOptions["name"], 1, (50,50, 50))
					self.current = 0

			if event.key == Singleton.KEY_DIR_UP :
				self.current -= 1
	
			if event.key == Singleton.KEY_DIR_DOWN :
				self.current += 1

			self.current %= len(self.currentOptions["subItems"])
			OptionsMenu.toggleElement(self.currentOptions["subItems"][self.current], True)
			self.selectorRectangle = pygame.Rect(
				(Singleton.SCREENWIDTH / 5) * Singleton.CONV_X - 50,
				(OptionsMenu.startPosition + (self.current * OptionsMenu.itemHeight) - 3) * Singleton.CONV_Y,
				(Singleton.SCREENWIDTH * 3 / 5) * Singleton.CONV_X + 100,
				self.itemHeight * 0.8 * Singleton.CONV_Y )
		
		return ("CONTINUE", None)


	def Draw(self, screen):
		screen.blit( OptionsMenu.background, (0,0))

		# OptionsMenu.paintElement( screen, self.titleImg, 225, 146 )
		OptionsMenu.paintElement( screen, self.currentOptions["imgValue"], Singleton.SCREENWIDTH / 6, OptionsMenu.startPosition - 70 )

		screen.fill((187,17,66), self.selectorRectangle )

		pospaint=0
		for item in self.currentOptions["subItems"] :
			OptionsMenu.paintElement( screen, item["imgValue"], Singleton.SCREENWIDTH / 5, OptionsMenu.startPosition + (OptionsMenu.itemHeight * pospaint) )
			pospaint += 1

	def LoadConfigSchema(self):
		# load menu items
		pitems = []
		ins = open( "configuration/options.conf", "r" )
		self.title = "ChameleonPi"
		subtitle = "menu"
		main = { "value" : 0, "name" : subtitle, "subItems" : pitems, "imgValue" : None, "parent" : None }
		compta = 0
		for line in ins:
			line = line.replace("\n", "")
			line = line.replace("\r\n", "")
			if line.startswith("#"):
				continue
			elif compta == 0:
				self.title = line
			elif compta == 1:
				main["name"] = line
			else :
				newitem = line.split("|")
				if len(newitem) < 3:
					newitem.append(None)
				condition = newitem[0].startswith("    ")
				if condition or newitem[0].startswith("\t"):
					# val = newitem[0][4:] if condition else newitem[0][1:]
					pitems[-1]["subItems"].append ( { "value" : int(newitem[0]), "name" : newitem[1], "cmd" : None, "subItems" : [], "imgValue" : None, "parent" : pitems[-1] } )
				else:
					if len(pitems) > 0 and len(pitems[-1]["subItems"]) > 0:
						pitems[-1]["subItems"].append ( { "value" : 0, "name" : "<< Cancel", "cmd" : None, "subItems" : [], "imgValue" : None, "parent" : None } )
					pitems.append ( { "value" : int(newitem[0]), "name" : newitem[1], "cmd" : None, "subItems" : [], "imgValue" : None, "parent" : main } )

			compta += 1
		ins.close()
		if len(main["subItems"][-1]["subItems"]):
			main["subItems"][-1]["subItems"].append ( { "value" : 0, "name" : "<< Cancel", "cmd" : None, "subItems" : [], "imgValue" : None, "parent" : None } )
		main["subItems"].append ( { "value" : 0, "name" : "<< Cancel", "cmd" : None, "subItems" : [], "imgValue" : None, "parent" : None } )
		return main

	@classmethod
	def paintElement(cls, screen, imatge, px, py ):
		screen.blit( imatge, (px * Singleton.CONV_X, py * Singleton.CONV_Y) )

	@classmethod
	def toggleElement(cls, element, status = False):
		if status:
			color = (255,255,255)
		else:
			color = (50,50,50)
		if len(element["subItems"]) > 0:
			element["imgValue"] = OptionsMenu.font_Item.render( ">> " + element["name"], 1, color )
		else:
			element["imgValue"] = OptionsMenu.font_Item.render( element["name"], 1, color )