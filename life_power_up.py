from power_ups import PowerUp

red = (240, 8, 8)
black = (0, 0, 0)
white = (245,245,245)
yellow = (255,165,0)
# font_path = os.path.dirname(os.path.abspath(__file__))
# retro_font = os.path.join(font_path, 'fonts', 'Robot9000.ttf')
class LifePowerUp(PowerUp):
	"""A class that represents a power up"""
	def __init__(self, ai_game):
		super().__init__(ai_game)
		self.square_colour = red
		self.letter = "L"