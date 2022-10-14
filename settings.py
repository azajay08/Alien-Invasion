import pygame
import os

black = (0, 0, 0)
white = (245,245,245)
light_cyan = (0,238,238)
dark_cyan = (0,139,139)
deep_pink = (255,20,147)
dark_pink = (139,10,80)
purple = (155,48,255)
yellow = (255,165,0)
volume = 0.08


class Settings:
	"""A class to store all the settings for Alien Invasion"""

	def __init__(self):
		"""Initialize the game's static settings"""
		# Screen settings
		self.screen_width = 1100
		self.screen_height = 700
		self.bg_colour = black

		# ship settings
		
		self.ship_limit = 3

		# Bullet settings
		self.bullet_width = 5
		self.bullet_height = 15
		self.bullet_colour = deep_pink
		self.bullets_allowed = 10

		# Alien settings
		self.fleet_drop_speed = 10
		

		# stars
		self.star_colour = white
		self.star_width = 2
		self.star_height = 2
		self.star_x = 1
		self.star_y = 1
		self.star_speed = 0.5

		# How quickly game speeds up
		self.speedup_scale = 1.3
		# How quickly the alien point value increases
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

		# Sounds
		s = os.path.dirname(os.path.abspath(__file__))
		self.laser = pygame.mixer.Sound(os.path.join(s, 'sound', "laser.ogg"))
		self.laser.set_volume(volume)
		self.music = pygame.mixer.music.load(os.path.join(s, 'sound', 'synthpop.ogg'))


	def initialize_dynamic_settings(self):
		"""Init settings that change through the game"""
		self.ship_speed = 2
		self.bullet_speed = 3.0
		self.alien_speed = 1.0

		# Fleet direction of 1 represents right: -1 left
		self.fleet_direction = 1

		# Scoring
		self.alien_points = 50

	def increase_speed(self):
		"""Increase speed settings and points values"""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)