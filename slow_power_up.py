import pygame
import os
# from pygame.sprite import Sprite
# from random import randint
from power_ups import PowerUp

brown = (152, 65, 28)
# font_path = os.path.dirname(os.path.abspath(__file__))
# retro_font = os.path.join(font_path, 'fonts', 'Robot9000.ttf')
class SlowPowerUp(PowerUp):
	"""A class that represents a bullet power up"""
	def __init__(self, ai_game):
		super().__init__(ai_game)
		self.square_colour = brown
		self.letter = "S"