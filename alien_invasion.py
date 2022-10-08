import sys
import pygame
from settings import Settings
from ship import Ship

# make the squares eventually pink and light pink, cyan and light cyan
# black background, white and yellow text

# black (0, 0, 0) - #000000
# white smoke (245,245,245) - #F5F5F5
# dark cyan (0,139,139) - #008B8B
# light cyan (0,238,238) - #00EEEE
# deep pink (255,20,147) - #FF1493
# dark pink (139,10,80) - #8B0A50
# purple (155,48,255) - #9B30FF
# dark yellow (255,165,0) - #FFA500

black = (0, 0, 0)
white_smoke = (245,245,245)
light_cyan = (0,238,238)
dark_cyan = (0,139,139)
deep_pink = (255,20,147)
dark_pink = (139,10,80)
purple = (155,48,255)
yellow = (255,165,0)


class AlienInvasion:
	"""Overall class to manage game assets and behaviour"""

	def __init__(self):
		"""Initilize the game and resources"""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((
			self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion!")

		self.ship = Ship(self)

	def run_game(self):
		"""Start the main loop for the game"""
		while True:
			self._check_events()
			self.ship.update()
			self._update_screen()
			
	def _check_events(self):
		"""responf to keypresses and mouse"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					self.ship.moving_right = True
				elif event.key == pygame.K_LEFT:
					self.ship.moving_left = True
				elif event.key == pygame.K_UP:
					self.ship.moving_up = True
				elif event.key == pygame.K_DOWN:
					self.ship.moving_down = True
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					self.ship.moving_right = False
				elif event.key == pygame.K_LEFT:
					self.ship.moving_left = False
				elif event.key == pygame.K_UP:
					self.ship.moving_up = False
				elif event.key == pygame.K_DOWN:
					self.ship.moving_down = False

	def _update_screen(self):
		"""Update images on screen, flip to the new screen."""
		self.screen.fill(self.settings.bg_colour)
		self.ship.blitme()

		pygame.display.flip()

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()

