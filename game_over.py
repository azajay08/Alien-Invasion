import pygame.font
import os

dark_cyan = (0,139,139)
light_cyan = (0,238,238)
deep_pink = (255,20,147)
purple = (155,48,255)
dark_pink = (139,10,80)
black = (0, 0, 0)
yellow = (255,165,0)
red = (240, 8, 8)

font_path = os.path.dirname(os.path.abspath(__file__))
retro_font = os.path.join(font_path, 'fonts', 'Robot9000.ttf')

# font_path = "Python_work/alien_invasion/robot-9000-font/Robot9000.ttf"
# test_font = "Python_work/disco-duck-font/Disco.otf"

class GameOver:

	def __init__(self, ai_game):
		"""Init button attributes"""
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.stats = ai_game.stats

		# Set dimensions and props of button
		self.width, self.height = 400, 100
		self.game_over_colour = red
		self.score_colour = yellow
		self.instructions_colour = deep_pink

		self.game_over_font = pygame.font.Font(retro_font, 100)
		self.score_font = pygame.font.Font(retro_font, 50)
		self.instructions_font = pygame.font.Font(retro_font, 30)

		self.go_rect = pygame.Rect(0, 0, self.width, self.height)
		self.go_rect.center = self.screen_rect.center
		self.go_rect.centery = self.screen_rect.centery - 200
		self.score_rect = pygame.Rect(0, 0, self.width, self.height)
		self.score_rect.center = self.screen_rect.center
		self.instructions_rect = pygame.Rect(0, 0, self.width, self.height)
		self.instructions_rect.center = self.screen_rect.center
		self.instructions_rect.centery = self.screen_rect.centery + 200

		# The button message needs to be prepped only once
		self._prep_msg()

	def _prep_msg(self):
		"""Turn msg into rendered image and center text on the button"""
		go_str = "GAME OVER!"
		rounded_score = round(self.stats.score)
		score_str = "Score:{:,}".format(rounded_score)
		instructions_str = "Press 'RETURN' to return to main menu, press 'Q' to quit"
		self.go_image = self.game_over_font.render(go_str, True, self.game_over_colour, black)
		self.go_image_rect = self.go_image.get_rect()
		self.go_image_rect.center = self.go_rect.center
		self.score_image = self.score_font.render(score_str, True, self.score_colour, black)
		self.score_image_rect = self.score_image.get_rect()
		self.score_image_rect.center = self.score_rect.center
		self.instructions_image = self.instructions_font.render(instructions_str,
			True, self.instructions_colour, black)
		self.instructions_image_rect = self.instructions_image.get_rect()
		self.instructions_image_rect.center = self.instructions_rect.center


	def draw_instructions(self):
		"""Draw blank button and then draw message"""
		# self.screen.fill(None, self.rect)
		self._prep_msg()
		self.screen.blit(self.go_image, self.go_image_rect)
		self.screen.blit(self.score_image, self.score_image_rect)
		self.screen.blit(self.instructions_image, self.instructions_image_rect)