import pygame
import shelve
import os

dir_path = os.path.dirname(os.path.abspath(__file__))
score_file = os.path.join(dir_path, 'score.txt')

class GameStats:
	"""Track the stats of the game"""

	def __init__(self, ai_game):
		"""Initialize stats"""
		# Start alien invasion in an inactive state
		self.game_active = False
		self.game_run = False
		self.settings = ai_game.settings
		self.reset_stats()

		# High score should never be reset

		# self.high_score = 0
		# This will get the high score from the score.txt file
		hs = shelve.open(score_file)
		self.high_score = hs['score']
		hs.close()

		

	def reset_stats(self):
		"""Initialize stats that can change during the game"""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1
