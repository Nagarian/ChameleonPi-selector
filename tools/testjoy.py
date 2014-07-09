#! /usr/bin/python

import pygame, sys
from pygame.locals import *

import pygame
import os

import random


pygame.init()
pygame.mixer.init()
pygame.font.init()

screen = pygame.display.set_mode((640, 480))


if pygame.joystick.get_count() > 0:	
	j = pygame.joystick.Joystick(0) 
	j.init()



while True:

	event = pygame.event.wait()
	
	if event.type == JOYAXISMOTION :
		print event.axis, event.value
		if event.axis == 0 and abs(event.value) < 0.5:
			pygame.time.set_timer(pygame.USEREVENT+2, 0)
			gleft = False
			gright = False


	if (event.type == KEYDOWN and (event.key == K_q or event.key == K_ESCAPE)) or (event.type == QUIT) :
		sys.exit()	

