import pygame
from pygame.sprite import Sprite

yellow = (255,165,0)

class Bullet(Sprite):
	"""A class to manage bullets fired from ship"""

	def __init__(self, ai_game, type):
		"""Creat a bullet object at the ship's current pos"""
		super().__init__()
		self.ai = ai_game
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.colour = self.settings.bullet_colour
		self.ship_rect = ai_game.ship.rect
		self.fired = False

		# Create a bullet rect at (0, 0) and then set current pos
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
			self.settings.bullet_height)
		if type == self.settings.main_gun:
			self.rect.midtop = ai_game.ship.rect.midtop
			self.y = float(self.rect.y)
			self.colour = self.settings.bullet_colour
		elif type == self.settings.left_gun:
			self.rect.midtop = ai_game.ship.rect.bottomleft
			self.y = float(self.rect.y) - 30
			self.colour = self.settings.p_bullet_colour
		elif type == self.settings.right_gun:
			self.rect.midtop = ai_game.ship.rect.bottomright
			self.y = float(self.rect.y) - 30
			self.colour = self.settings.p_bullet_colour

	def update(self):
		"""Move the bullet up"""
		# update dec position of bullet
		self.y -= self.settings.bullet_speed
		self.rect.y = self.y

	def draw_bullet(self):
		"""Draw bullet to screen"""
		pygame.draw.rect(self.screen, self.colour, self.rect)
