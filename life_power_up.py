from power_ups import PowerUp

red = (240, 8, 8)
black = (0, 0, 0)
white = (245,245,245)
yellow = (255,165,0)

class LifePowerUp(PowerUp):
	"""A class that represents a life power up"""
	def __init__(self, ai_game):
		super().__init__(ai_game)
		self.power_up_colour = red
		self.letter = "L"