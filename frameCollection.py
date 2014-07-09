#! /usr/bin/python
# -*- coding: utf-8 -*- 

class FrameManager:
	""" Collection of frame was managed by this class """
	def __init__(self):
		self.collection = []

	def push(self, frame):
		# if issubclass(frame, IFrame) :
			frame.LoadContent()
			self.collection.append(frame)
		# else:
			# raise Exception("Invalid Class")

	def pop(self, boolean=True):
		frm = self.collection.pop()
		if boolean:
			frm.UnloadContent()
		return frm

	def peek(self):
		return self.collection[len(self.collection) - 1]

	def Update(self, event):
		return self.peek().Update(event)

	def Draw(self, screen):
		return self.peek().Draw(screen)