import pygame
import os
from pygame.sprite import Sprite
from random import randint

red = (240, 8, 8)
black = (0, 0, 0)
white = (245,245,245)
font_path = os.path.dirname(os.path.abspath(__file__))
retro_font = os.path.join(font_path, 'fonts', 'Robot9000.ttf')
class PowerUp(Sprite):
	"""A class that represents a power up"""
	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = self.screen.get_rect()
		self.screen_width = self.settings.screen_width

		self.width, self.height = 15, 15
		self.text_colour = white
		self.square_colour = red
		self.font = pygame.font.Font(retro_font, 20)
		self.rect = pygame.Rect((randint(0 , self.screen_width)), 0, self.width, self.height)
		# self.rect.midtop = self.screen_rect.midtop
		self.letter = "P"
		self.prep_power_up()

	def prep_power_up(self):
		self.power_up_image = self.font.render(self.letter, True, self.text_colour,
			 None)
		self.power_up_rect = self.power_up_image.get_rect()
		self.power_up_rect.center = self.rect.center

	def draw_power_up(self):
		"""Draw blank button and then draw message"""
		# self.screen.fill(self.square_colour, self.rect)
		pygame.draw.circle(self.screen, self.square_colour, self.rect.center, 15, 15)
		self.screen.blit(self.power_up_image, self.power_up_rect)