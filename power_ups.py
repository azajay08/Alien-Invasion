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

		self.width, self.height = 10, 10
		self.text_colour = white
		self.square_colour = red
		self.font = pygame.font.Font(retro_font, 20)
		self.rect = pygame.Rect((randint(0 , self.screen_width)), 0, self.width, self.height)
		# self.rect.midtop = self.screen_rect.midtop
		self.letter = "P"
		self.prep_letter()
		self.y = float(self.rect.y)

	def prep_letter(self):
		self.letter_image = self.font.render(self.letter, True, self.text_colour,
			 None)
		self.letter_rect = self.letter_image.get_rect()
		self.letter_rect.center = self.rect.center

	def draw_power_up(self):
		"""Draw blank button and then draw message"""
		# self.screen.fill(self.square_colour, self.rect)
		self.prep_letter()
		pygame.draw.circle(self.screen, self.square_colour, self.rect.center, 15, 15)
		self.screen.blit(self.letter_image, self.letter_rect)

	def update(self):
		self.y += 1
		self.rect.y = self.y
		# self.letter_rect.center = self.rect.center