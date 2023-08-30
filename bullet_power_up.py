from power_ups import PowerUp

orange = (255, 128, 0)

class BulletPowerUp(PowerUp):
	"""A class that represents a bullet power up"""
	def __init__(self, ai_game):
		super().__init__(ai_game)
		self.power_up_colour = orange
		self.letter = "G"
		self.power_up_name = "Guns"

	def prep_power_up_text(self):
		self.text_image = self.font.render(self.power_up_name, True,
			self.power_up_colour, None)
		self.text_rect = self.text_image.get_rect()
		self.text_rect.left = self.sb.level_rect.right + 30
		self.text_rect.top = 20