import sys
import pygame
from settings import Settings
from ship import Ship
from bullets import Bullet
from alien import Alien

# make the squares eventually pink and light pink, cyan and light cyan
# black background, white and yellow text

# black (0, 0, 0) - #000000
# white smoke (245,245,245) - #F5F5F5
# dark cyan (0,139,139) - #008B8B
# light cyan (0,238,238) - #00EEEE
# deep pink (255,20,147) - #FF1493
# dark pink (139,10,80) - #8B0A50
# purple (155,48,255) - #9B30FF
# dark yellow (255,165,0) - #FFA500

black = (0, 0, 0)
white_smoke = (245,245,245)
light_cyan = (0,238,238)
dark_cyan = (0,139,139)
deep_pink = (255,20,147)
dark_pink = (139,10,80)
purple = (155,48,255)
yellow = (255,165,0)


class AlienInvasion:
	"""Overall class to manage game assets and behaviour"""

	def __init__(self):
		"""Initilize the game and resources"""
		pygame.init()
		self.settings = Settings()

		# self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		# self.settings.screen_width = self.screen.get_rect().width
		# self.settings.screen_height = self.screen.get_rect().height

		self.screen = pygame.display.set_mode((
			self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion!")

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self._create_fleet()

	def run_game(self):
		"""Start the main loop for the game"""
		while True:
			self._check_events()
			self.ship.update()
			self._update_bullets()
			self._update_aliens()
			self._update_screen()
			

	def _update_aliens(self):
		"""check fleet edge, update pos"""
		self._check_fleet_edges()
		self.aliens.update()

	def _check_fleet_edges(self):
		"""Respond if any aliens reach the edge"""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		"""Drop enitre fleet and change direction"""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1

	def _create_fleet(self):
		"""Create fleet of aliens"""
		# Make alien and find number of aliens in row
		# Spacing between each alien is equal to one alien width
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_aliens_x = available_space_x // (2 * alien_width)

		# Determine number of rows
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height -
								(7 * alien_height) - ship_height)
		number_rows = available_space_y // (2 * alien_height)

		# Create the fleet of aliens
		for row_number in range(number_rows):
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_number, row_number)
			
	def _create_alien(self, alien_number, row_number):
		"""Create an alien and place it in the row"""
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		self.aliens.add(alien)

	def _update_bullets(self):
		"""Update bullet pos"""
		self.bullets.update()
			# Get rid of bullets
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)
			print(len(self.bullets))

		# Check for any bullets that hit - get rid 
		collisions = pygame.sprite.groupcollide(
			self.bullets, self.aliens, True, True)

			
			
	def _check_events(self):
		"""responf to keypresses and mouse"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		"""Respond to key presses"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _fire_bullet(self):
		"""Create a new bullet and add it to the bullets group"""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)


	def _check_keyup_events(self, event):
		"""Responds to key release"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False
		elif event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False


	def _update_screen(self):
		"""Update images on screen, flip to the new screen."""
		self.screen.fill(self.settings.bg_colour)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.screen)

		pygame.display.flip()

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()

