import pygame
from pygame.sprite import Sprite
from random import randint

star_image = pygame.image.load('Python_work/alien_invasion/images/star.bmp')
star = pygame.transform.scale(star_image, (5, 5))

class Star(Sprite):

	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.settings = ai_game.settings

		self.image = star
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def update(self):
		self.y += self.settings.star_speed
		self.x += self.settings.star_speed
		self.rect.y = self.y
		self.rect.x = self.x