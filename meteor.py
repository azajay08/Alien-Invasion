import pygame
import os
from pygame.sprite import Sprite
from random import randint

path = os.path.dirname(os.path.abspath(__file__))
meteor_image = pygame.image.load(os.path.join(path, 'images', "meteor.bmp"))
meteor = pygame.transform.scale(meteor_image, (20, 40))

class Meteor(Sprite):
	"""A class to represent a single alien in the fleet"""

	def __init__(self, ai_game):
		"""Initialize the meteor and its startin pos"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		self.image = meteor

		self.rect = self.image.get_rect()
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		self.rect = pygame.Rect(randint(0 , self.settings.screen_width),
			randint(-100 , 0),self.rect.width, self.rect.height)
		speed = randint(5, 25)
		self.speed = float(speed / 10.0)
		self.y = float(self.rect.y)

	def update(self):
		"""Moves stars in downwards direction"""
		self.y += self.speed
		self.rect.y = self.y
