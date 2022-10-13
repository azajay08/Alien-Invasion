import pygame.font

black = (0, 0, 0)
white_smoke = (245,245,245)
light_cyan = (0,238,238)
dark_cyan = (0,139,139)
deep_pink = (255,20,147)
dark_pink = (139,10,80)
purple = (155,48,255)
yellow = (255,165,0)

class Scoreboard:
	"""A class to report scoring info"""

	def __init__(self, ai_game):
		"""Init scoreboard attributes"""
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		self.stats = ai_game.stats

		# Font settings for scoring info
		self.text_colour = yellow
		self.font = pygame.font.SysFont(None, 48)

		# Prepare the inital score image
		self.prep_score()

	def prep_score(self):
		"""Turn score into rendered image"""
		score_str = str(self.stats.score)
		self.score_image = self.font.render(score_str, True,
						self.text_colour, self.settings.bg_colour)
		
		# Display the score at the top right of the screen.

		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def show_score(self):
		"""Draw score to the screen."""
		self.screen.blit(self.score_image, self.score_rect)