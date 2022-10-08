import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class to manage bullets fired from ship"""

	def __init__(self, ai_game):
		"""Creat a bullet object at the ship's current pos"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.colour = self.settings.bullet_colour

		# Create a bullet rect at (0, 0) and then set current pos
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
			self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop

		# Store bullet pos as dec
		self.y = float(self.rect.y)

	def update(self):
		"""Move the bullet up"""
		# update dec pos of bullet
		self.y -= self.settings.bullet_speed
		# update rect po
		self.rect.y = self.y

	def draw_bullet(self):
		"""Draw bullet to screen"""
		pygame.draw.rect(self.screen, self.colour, self.rect)