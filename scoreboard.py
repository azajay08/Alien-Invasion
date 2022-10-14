import pygame.font
import shelve

black = (0, 0, 0)
white_smoke = (245,245,245)
light_cyan = (0,238,238)
dark_cyan = (0,139,139)
deep_pink = (255,20,147)
dark_pink = (139,10,80)
purple = (155,48,255)
yellow = (255,165,0)
red = (240, 8, 8)

font_path = "Python_work/alien_invasion/robot-9000-font/Robot9000.ttf"

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
		self.hs_text_colour = deep_pink
		self.level_text_colour = dark_cyan
		self.lives_text_colour = red
		self.font_score = pygame.font.Font(font_path, 24)
		self.font_h_score = pygame.font.Font(font_path, 24)
		self.font_level = pygame.font.Font(font_path, 24)
		self.font_lives = pygame.font.Font(font_path, 24)

		# Prepare the inital score image
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_lives()

	def prep_score(self):
		"""Turn score into rendered image"""
		rounded_score = round(self.stats.score -1)
		score_str = "Score{:,}".format(rounded_score)
		self.score_image = self.font_score.render(score_str, True,
						self.text_colour, self.settings.bg_colour)
		
		# Display the score at the top right of the screen.

		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def prep_high_score(self):
		"""Turn high score into rendered image"""
		high_score = round(self.stats.high_score, -1)
		high_score_str = "High Score:{:,}".format(high_score)
		self.high_score_image = self.font_h_score.render(high_score_str, True,
							self.hs_text_colour, self.settings.bg_colour)
		
		# Center the high score at the top of the screen
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.left = self.screen_rect.left + 20
		self.high_score_rect.top = 20

	def prep_level(self):
		"""Turn the level into a rendered image"""
		level_v = str(self.stats.level)
		level_str = "Level:{:}".format(level_v)
		self.level_image = self.font_level.render(level_str, True,
						self.level_text_colour, self.settings.bg_colour)
		# Position the level below the score
		self.level_rect = self.level_image.get_rect()
		self.level_rect.top = self.score_rect.top
		self.level_rect.centerx = self.screen_rect.centerx

	def prep_lives(self):
		"""Turn lives into rendered image"""
		lives = str(self.stats.ships_left)
		lives_str = "Lives:{:}".format(lives)
		self.lives_image = self.font_lives.render(lives_str, True,
						self.lives_text_colour, self.settings.bg_colour)

		# Position the lives below the score

		self.lives_rect = self.lives_image.get_rect()
		self.lives_rect.right = self.score_rect.right
		self.lives_rect.top = self.score_rect.bottom + 10

	def show_score(self):
		"""Draw score and level to the screen."""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.screen.blit(self.lives_image, self.lives_rect)

	def check_high_score(self):
		"""Check to see if there is a new high score"""



		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			hs = shelve.open('score.txt')
			hs['score'] = self.stats.high_score
			hs.close()
			self.prep_high_score()
		
