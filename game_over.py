import pygame.font
import os

deep_pink = (255,20,147)
black = (0, 0, 0)
yellow = (255,165,0)
red = (240, 8, 8)

font_path = os.path.dirname(os.path.abspath(__file__))
retro_font = os.path.join(font_path, 'fonts', 'Robot9000.ttf')

class GameOver:

	def __init__(self, ai_game):
		"""Init game over attributes"""
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.stats = ai_game.stats

		# Set dimensions and props of button
		self.width, self.height = 400, 100

		self.game_over_font = pygame.font.Font(retro_font, 100)
		self.score_font = pygame.font.Font(retro_font, 50)
		self.instructions_font = pygame.font.Font(retro_font, 30)

		self.go_rect = pygame.Rect(0, 0, self.width, self.height)
		self.go_rect.center = self.screen_rect.center
		self.go_rect.centery = self.screen_rect.centery - 150
		self.score_rect = pygame.Rect(0, 0, self.width, self.height)
		self.score_rect.center = self.screen_rect.center
		self.instructions_rect1 = pygame.Rect(0, 0, self.width, self.height)
		self.instructions_rect1.center = self.screen_rect.center
		self.instructions_rect1.centery = self.screen_rect.centery + 100
		self.instructions_rect2 = pygame.Rect(0, 0, self.width, self.height)
		self.instructions_rect2.center = self.screen_rect.center
		self.instructions_rect2.centery = self.screen_rect.centery + 200

		# The button message needs to be prepped only once
		self._prep_msg()

	def _prep_msg(self):
		"""Turn end game strings into rendered images"""
		go_str = "GAME OVER!"
		rounded_score = round(self.stats.score)
		score_str = "Score:{:,}".format(rounded_score)
		instructions_str1 = "Press 'RETURN' to return to main menu"
		instructions_str2 = "Press 'escape' to quit"
		self.go_image = self.game_over_font.render(go_str, True, red, black)
		self.go_image_rect = self.go_image.get_rect()
		self.go_image_rect.center = self.go_rect.center
		self.score_image = self.score_font.render(score_str, True, yellow, black)
		self.score_image_rect = self.score_image.get_rect()
		self.score_image_rect.center = self.score_rect.center
		self.instructions_image1 = self.instructions_font.render(instructions_str1,
			True, deep_pink, black)
		self.instructions_image_rect1 = self.instructions_image1.get_rect()
		self.instructions_image_rect1.center = self.instructions_rect1.center
		self.instructions_image2 = self.instructions_font.render(instructions_str2,
			True, deep_pink, black)
		self.instructions_image_rect2 = self.instructions_image2.get_rect()
		self.instructions_image_rect2.center = self.instructions_rect2.center


	def draw_instructions(self):
		"""Draws the images of the end game strings"""
		# self.screen.fill(None, self.rect)
		self._prep_msg()
		self.screen.blit(self.go_image, self.go_image_rect)
		self.screen.blit(self.score_image, self.score_image_rect)
		self.screen.blit(self.instructions_image1, self.instructions_image_rect1)
		self.screen.blit(self.instructions_image2, self.instructions_image_rect2)