from random import randint
import sys
import pygame
from settings import Settings
from ship import Ship
from bullets import Bullet
from alien import Alien
from stars import Star
from time import sleep
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

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
		pygame.mixer.init()
		self.settings = Settings()
		

		# self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		# self.settings.screen_width = self.screen.get_rect().width
		# self.settings.screen_height = self.screen.get_rect().height

		self.screen = pygame.display.set_mode((
			self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion!")

		# Create an instance to store game stats
		# Create scoreboard
		self.stats = GameStats(self)
		self.sb = Scoreboard(self)

		self.stars = pygame.sprite.Group()
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()
		
		self._create_fleet()
		# Make play button
		self.play_button = Button(self, "Play")

	def run_game(self):
		"""Start the main loop for the game"""
		while True:
			self._check_events()
			self._update_stars()
			if self.stats.game_active == True:
				self.ship.update()
				self._update_bullets()
				self._update_aliens()

			self._update_screen()
			

	def _check_aliens_bottom(self):
		"""Cheack if aliens have reached the bottom"""
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
			# Treat this the same as if the ship got hit
				self._ship_hit()
				break


	def _ship_hit(self):
		"""Respond to ship being hit"""
		# Decrement ships_left
		if self.stats.ships_left > 0:
			self.stats.ships_left -= 1

			# Get rid of any remaining aliens and bullets
			self.aliens.empty()
			self.bullets.empty()

			# Create new fleet and center the ship
			self._create_fleet()
			self.ship.center_ship()
			# Pause.
			sleep(0.5)
		else:
			self.stats.game_active = False
			pygame.mouse.set_visible(True)

	def _update_aliens(self):
		"""check fleet edge, update pos"""
		self._check_fleet_edges()
		self.aliens.update()

		# Look for alien ship collisions
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()
		# Look for aliens hitting bottom of screen
		self._check_aliens_bottom()

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
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number + 30
		self.aliens.add(alien)

	def _update_bullets(self):
		"""Update bullet pos"""
		self.bullets.update()
			# Get rid of bullets
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)
		self._check_bullet_alien_collision()
#print(len(self.bullets))

	def _check_bullet_alien_collision(self):
		"""Respond to bullet-alien collisions"""
		# Remove any bullets and aliens that have collided.	
		# Check for any bullets that hit - get rid 
		collisions = pygame.sprite.groupcollide(
			self.bullets, self.aliens, True, True)
		if collisions:
			for aliens in collisions.values():
				self.stats.score += self.settings.alien_points * len(aliens)
			self.sb.prep_score()
			self.sb.check_high_score()
		if not self.aliens:
			# Destroy existing belluets and create new fleet
			self.bullets.empty()
			self._create_fleet()
			self.settings.increase_speed()

			# Increase level
			self.stats.level += 1
			self.sb.prep_level()

	def _update_stars(self):
		"""Update star pos"""
		self._star_launch()
		self.stars.update()
			# Get rid of stars
		for star in self.stars.copy():
			if star.rect.bottom <= 0:
				self.stars.remove(star)
			
	def _check_events(self):
		"""Respond to keypresses and mouse"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_play_button(self, mouse_pos):
		"""Start a new game when the player clock Play."""
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		# Starts the music when the play button is pressed
		pygame.mixer.music.play(-1)
		if button_clicked and not self.stats.game_active:
			# Reset the game settings
			self.settings.initialize_dynamic_settings()
			self.stats.reset_stats()
			self.stats.game_active = True
			self.sb.prep_score()
			self.sb.prep_level()
			self.sb.prep_lives()

			# Hide the cursor
			pygame.mouse.set_visible(False)

			# Get rif of any remaining aliens and bullets
			self.aliens.empty()
			self.bullets.empty()

			# Create new fleet and center ship
			self._create_fleet()
			self.ship.center_ship()

	def _check_keydown_events(self, event):
		"""Respond to key presses"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		# elif event.key == pygame.K_UP:
		# 	self.ship.moving_up = True
		# elif event.key == pygame.K_DOWN:
		# 	self.ship.moving_down = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _fire_bullet(self):
		"""Create a new bullet and add it to the bullets group"""
		if len(self.bullets) < self.settings.bullets_allowed:
			# Plays pew pew sound everytime a bullet is fired
			pygame.mixer.Sound.play(self.settings.laser)
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _star_launch(self):
		"""Create a new star and add it to the star group"""
		if len(self.stars) < 300:
			new_star = Star(self)
			self.stars.add(new_star)
 

	def _check_keyup_events(self, event):
		"""Responds to key release"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False
		# elif event.key == pygame.K_UP:
		# 	self.ship.moving_up = False
		# elif event.key == pygame.K_DOWN:
		# 	self.ship.moving_down = False


	def _update_screen(self):
		"""Update images on screen, flip to the new screen."""
		self.screen.fill(self.settings.bg_colour)
		for star in self.stars.sprites():
			star.draw_star()
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.screen)
		# Draw the score info
		self.sb.show_score()
		# Draw the play button if the game is inactive
		if not self.stats.game_active:
			self.play_button.draw_button()

		pygame.display.flip()

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()

