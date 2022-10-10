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
		"""Initialize the game's settings"""
		# Screen settings
		self.screen_width = 1100
		self.screen_height = 700
		self.bg_colour = black

		# ship settings
		self.ship_speed = 2

		# Bullet settings
		self.bullet_speed = 3.0
		self.bullet_width = 5
		self.bullet_height = 15
		self.bullet_colour = deep_pink
		self.bullets_allowed = 15

		# Alien settings
		self.alien_speed = 1.0
		self.fleet_drop_speed = 10
		# Fleet direction of 1 represents right: -1 left
		self.fleet_direction = 1

		# stars
		self.star_colour = white
		self.star_width = 2
		self.star_height = 2
		self.star_x = 1
		self.star_y = 1
		self.star_speed = 0.5
