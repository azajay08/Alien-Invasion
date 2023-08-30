import pygame.font
import os

dark_cyan = (0,139,139)
light_cyan = (0,238,238)
deep_pink = (255,20,147)
purple = (155,48,255)
dark_pink = (139,10,80)
black = (0, 0, 0)

font_path = os.path.dirname(os.path.abspath(__file__))
retro_font = os.path.join(font_path, 'fonts', 'Robot9000.ttf')

# font_path = "Python_work/alien_invasion/robot-9000-font/Robot9000.ttf"
# test_font = "Python_work/disco-duck-font/Disco.otf"

class Instructions:

	def __init__(self, ai_game):
		"""Init instructions attributes"""
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		# Set dimensions and props of button
		self.width, self.height = 400, 100
		self.text1_colour = light_cyan
		self.text2_colour = deep_pink

		self.font = pygame.font.Font(retro_font, 20)

		self.rect1 = pygame.Rect(0, 0, self.width, self.height)
		self.rect1.center = self.screen_rect.center
		self.rect1.centery = self.screen_rect.centery - 150
		self.rect2 = pygame.Rect(0, 0, self.width, self.height)
		self.rect2.center = self.screen_rect.center
		self.rect2.centery = self.screen_rect.centery + 130
		self.rect3 = pygame.Rect(0, 0, self.width, self.height)
		self.rect3.center = self.screen_rect.center
		self.rect3.centery = self.screen_rect.centery + 200

		# The button message needs to be prepped only once
		self._prep_msg()

	def _prep_msg(self):
		"""Turn instructions strings into rendered images"""
		message1 = "Press 'SPACE' or click 'PLAY' to start, press 'escape' to quit"
		message2 = "Use arrow keys or 'w','a','s','d' to move, 'SPACE' to shoot"
		message3 = "Dodge or shoot the meteorites, shoot the aliens, collect power ups"
		self.msg_image1 = self.font.render(message1, True, self.text1_colour, black)
		self.msg_image_rect1 = self.msg_image1.get_rect()
		self.msg_image_rect1.center = self.rect1.center
		self.msg_image2 = self.font.render(message2, True, self.text2_colour, black)
		self.msg_image_rect2 = self.msg_image2.get_rect()
		self.msg_image_rect2.center = self.rect2.center
		self.msg_image3 = self.font.render(message3, True, self.text2_colour, black)
		self.msg_image_rect3 = self.msg_image3.get_rect()
		self.msg_image_rect3.center = self.rect3.center

	def draw_instructions(self):
		"""Draws the image of the instruction strings"""
		# self.screen.fill(None, self.rect)
		self.screen.blit(self.msg_image1, self.msg_image_rect1)
		self.screen.blit(self.msg_image2, self.msg_image_rect2)
		self.screen.blit(self.msg_image3, self.msg_image_rect3)