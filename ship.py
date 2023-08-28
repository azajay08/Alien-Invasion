import pygame
import os


image_path = os.path.dirname(os.path.abspath(__file__))

jet_image = pygame.image.load(os.path.join(image_path, 'images', 'space.bmp'))
jet = pygame.transform.scale(jet_image, (60, 80))

class Ship:
	"""A class to manage the ship"""

	def __init__(self, ai_game):
		"""Initialize the ship and starting pos"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.settings = ai_game.settings

		# Load the ship image and get its rect.

		self.image = jet
		self.rect = self.image.get_rect()

		# Start ship at the bottom.

		self.rect.midbottom = self.screen_rect.midbottom

		# Store a number for ships position
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		# Movement flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""Updates ships pos based on movement flag"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
		if self.moving_up and self.rect.top > 0:
			self.y -= self.settings.ship_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.ship_speed

		self.rect.x = self.x
		self.rect.y = self.y

	def blitme(self):
		"""Draw ship at its current location"""
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		"""Center the ship on the screen"""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		
