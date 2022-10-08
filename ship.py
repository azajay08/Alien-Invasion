import pygame

jet_image = pygame.image.load('Python_work/alien_invasion/images/fighter_jet.bmp')
jet = pygame.transform.scale(jet_image, (60, 80))

class Ship:
	"""A class to manage the ship"""

	def __init__(self, ai_game):
		"""Initialize the ship and starting pos"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		# Load the ship image and get its rect.

		self.image = jet
		self.rect = self.image.get_rect()

		# Start each ship at the bottom.

		self.rect.midbottom = self.screen_rect.midbottom

		# Movement flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""Updates ships pos based on movement flag"""
		if self.moving_right:
			self.rect.x += 2
		if self.moving_left:
			self.rect.x -= 2
		if self.moving_up:
			self.rect.y -= 2
		if self.moving_down:
			self.rect.y += 2

	def blitme(self):
		"""Draw ship at its current location"""
		self.screen.blit(self.image, self.rect)

