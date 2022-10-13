black = (0, 0, 0)
white = (245,245,245)
light_cyan = (0,238,238)
dark_cyan = (0,139,139)
deep_pink = (255,20,147)
dark_pink = (139,10,80)
purple = (155,48,255)
yellow = (255,165,0)


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
		self.bullets_allowed = 15

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
		self.speedup_scale = 1.1

		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):
		"""Init settings that change through the game"""
		self.ship_speed = 2
		self.bullet_speed = 3.0
		self.alien_speed = 1.0

		# Fleet direction of 1 represents right: -1 left
		self.fleet_direction = 1

	def increase_speed(self):
		"""Increase speed settings"""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale