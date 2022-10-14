import pygame

class GameStats:
	"""Track the stats of the game"""

	def __init__(self, ai_game):
		"""Initialize stats"""
		# Start alien invasion in an inactive state
		self.game_active = False
		self.settings = ai_game.settings
		self.reset_stats()

		# High score should never be reset
		self.high_score = 0

		

	def reset_stats(self):
		"""Initialize stats that can change during the game"""
		self.ships_left = self.settings.ship_limit
		self.score = 0
