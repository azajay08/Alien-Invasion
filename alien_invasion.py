import sys
import pygame
from settings import Settings

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

	def run_game(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			
			self.screen.fill(self.settings.bg_colour)

			pygame.display.flip()

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()

