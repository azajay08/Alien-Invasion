from random import randint
from power_ups import PowerUp
from bullet_power_up import BulletPowerUp
from life_power_up import LifePowerUp
from slow_power_up import SlowPowerUp

class Generator():
	"""A class that generates a power up"""
	def __init__(self, ai_game):
		self.ai = ai_game;
		self.power_up = PowerUp(self.ai)
		self.power_up_count = 3

	def generate_power_up(self):
		x = randint(1, self.power_up_count)
		if x == 1:
			self.power_up = SlowPowerUp(self.ai)
		elif x == 2:
			self.power_up = BulletPowerUp(self.ai)
		elif x == 3:
			self.power_up = LifePowerUp(self.ai)
