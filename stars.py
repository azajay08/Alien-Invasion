import pygame
from pygame.sprite import Sprite
from random import randint


class Star(Sprite):

	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.colour = self.settings.star_colour
		self.screen_height = self.settings.screen_height
		self.screen_width = self.settings.screen_width

		self.rect = pygame.Rect((randint(0 , self.screen_width)), (randint(0 , self.screen_height)), self.settings.star_width,
			self.settings.star_height)

		self.y = float(self.rect.y)

	def update(self):
		"""move star"""
		self.y += self.settings.star_speed

		self.rect.y = self.y
		if self.y >= self.settings.screen_height:
			self.y = 0

	def draw_star(self):
		pygame.draw.rect(self.screen, self.colour, self.rect)
