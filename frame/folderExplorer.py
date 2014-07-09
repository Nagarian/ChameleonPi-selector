#! /usr/bin/python
# -*- coding: utf-8 -*- 

import os

class FolderExplorer:
	"""docstring for FolderExplorer"""
	def __init__(self, foldEr, extensionAllowEd):
		self.baseFolder = os.path.realpath(foldEr)
		self.extensionAllowed = extensionAllowEd
		self.fileitems = []
		self.fileItemsAllowed = []
		self.itemsCount = 0
		self.itemsAllowedCount = 0

		self.loadFolder(foldEr)

	def loadFolder(self, foldEr ):
		"""Fonction qui va lister tout les fichiers contenue dans le dossier passer en paramètres"""
		self.fileitems = []
		if os.path.realpath(foldEr) != self.baseFolder and os.path.realpath(foldEr).startswith(self.baseFolder):
			directory = os.path.abspath(os.path.join(foldEr, os.pardir))
			self.fileitems.append( {"value": directory, "name": "..", "isFolder": True} )

		for file in os.listdir(foldEr):
			try:
				filen = file.decode('utf-8')
			except Exception: 
				filen = file
			
			self.fileitems.append ( {"value": os.path.join(foldEr,filen), "name":os.path.basename(filen), "isFolder" : os.path.isdir(os.path.join(foldEr,filen)) } )
		# self.fileitems.sort()
		self.itemsCount = len(self.fileitems)
		self.getItemsAllowed()

	def getItemsAllowed(self):
		"""Fonction qui va trier les fichiers trouver dans le dossier afin de ne garder que ceux dont l'extension est autorisée"""
		titems = []
		for item in self.fileitems:
			if item["isFolder"] :
				titems.append( item )
			else :
				if len(self.extensionAllowed) == 0:
					titems.append( item )
				else:
					for x in self.extensionAllowed:
						if item["name"].upper().endswith(x.upper()):
							item["name"] = item["name"][:-len(x)]
							titems.append( item )
							break
			#titems.append( item )
		self.fileItemsAllowed = titems
		self.itemsAllowedCount = len(self.fileItemsAllowed)