import pygame
from pygame.sprite import Sprite
from random import randint


class Star(Sprite):

	def __init__(self, ai_game):
		"""Creates a star from random place or top of screen"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.colour = self.settings.star_colour
		self.screen_height = self.settings.screen_height
		self.screen_width = self.settings.screen_width

		# Using randint, it will create the stars at different x coords of the screen
		self.rect = pygame.Rect((randint(0 , self.screen_width)), (randint(0 , self.screen_height)), self.settings.star_width,
			self.settings.star_height)

		self.y = float(self.rect.y)

	def update(self):
		"""Moves star in downwards direction"""
		self.y += self.settings.star_speed

		self.rect.y = self.y
		if self.y >= self.settings.screen_height:
			self.y = 0

	def draw_star(self):
		pygame.draw.rect(self.screen, self.colour, self.rect)
