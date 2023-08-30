from power_ups import PowerUp

brown = (152, 65, 28)

class SlowPowerUp(PowerUp):
	"""A class that represents a bullet power up"""
	def __init__(self, ai_game):
		super().__init__(ai_game)
		self.power_up_colour = brown
		self.letter = "S"
		self.power_up_name = "Slow mo"

	def prep_power_up_text(self):
		self.text_image = self.font.render(self.power_up_name, True,
			self.power_up_colour, None)
		self.text_rect = self.text_image.get_rect()
		self.text_rect.right = self.sb.level_rect.left - 30
		self.text_rect.top = 20
		