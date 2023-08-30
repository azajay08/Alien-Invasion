import pygame.font
import os

dark_cyan = (0,139,139)
light_cyan = (0,238,238)
deep_pink = (255,20,147)
purple = (155,48,255)
dark_pink = (139,10,80)

font_path = os.path.dirname(os.path.abspath(__file__))
retro_font = os.path.join(font_path, 'fonts', 'Robot9000.ttf')

class Button:

	def __init__(self, ai_game, msg):
		"""Init button attributes"""
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		# Set dimensions and props of button
		self.width, self.height = 400, 100
		self.button_colour = deep_pink
		self.text_colour = light_cyan
		self.font = pygame.font.Font(retro_font, 78)

		# Build the button's rect object and center it
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		# The button message needs to be prepped only once
		self._prep_msg(msg)

	def _prep_msg(self, msg):
		"""Turn msg into rendered image and center text on the button"""
		self.msg_image = self.font.render(msg, True, self.text_colour, self.button_colour)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		"""Draw blank button and then draw message"""
		self.screen.fill(self.button_colour, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
