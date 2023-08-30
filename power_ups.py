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
		self.sb = ai_game.sb

		self.width, self.height = 10, 10
		self.text_colour = white
		self.power_up_colour = red
		self.font = pygame.font.Font(retro_font, 20)
		self.rect = pygame.Rect((randint(0 , self.screen_width)), 0, self.width, self.height)
		self.letter = "P"
		self.power_up_name = "Power"
		self.prep_letter()
		self.y = float(self.rect.y)

	def prep_letter(self):
		self.letter_image = self.font.render(self.letter, True, self.text_colour,
			 None)
		self.letter_rect = self.letter_image.get_rect()
		self.letter_rect.center = self.rect.center

	def draw_power_up(self):
		"""Draw blank button and then draw message"""
		self.prep_letter()
		pygame.draw.circle(self.screen, self.power_up_colour, self.rect.center, 15, 15)
		self.screen.blit(self.letter_image, self.letter_rect)

	def update(self):
		self.y += 1
		self.rect.y = self.y

	def prep_power_up_text(self):
		self.text_image = self.font.render(self.power_up_name, True,
						self.power_up_colour, None)
		self.text_rect = self.text_image.get_rect()
		self.text_rect.right = self.sb.score_rect.left - 20
		self.text_rect.top = 20

	def draw_power_up_text(self):
		self.prep_power_up_text()
		self.screen.blit(self.text_image, self.text_rect)
		