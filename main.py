import sys
import pygame
import time
from settings import Settings
from ship import Ship
from bullets import Bullet
from alien import Alien
from stars import Star
from time import sleep
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from instructions import Instructions
from game_over import GameOver
from bullet_power_up import BulletPowerUp
from slow_power_up import SlowPowerUp
from life_power_up import LifePowerUp
from generator import Generator
from meteor import Meteor

fps = 120
clock = pygame.time.Clock()

class AlienInvasion:
	"""Overall class to manage game assets and behaviour"""
	def __init__(self):
		"""Initilize the game and resources"""
		pygame.init()
		pygame.mixer.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((
			self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion!")

		self.stats = GameStats(self)
		self.sb = Scoreboard(self)
		self.stars = pygame.sprite.Group()
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()
		self.meteors = pygame.sprite.Group()
		self.power_ups = pygame.sprite.Group()
		
		self.play_button = Button(self, "Play")
		self.instructions = Instructions(self)
		self.game_over = GameOver(self)
		self.generator = Generator(self)
		self.bullet_power_up = BulletPowerUp(self)
		self.slow_power_up = SlowPowerUp(self)
		self._star_launch()

# Star Functions
	def _star_launch(self):
		"""Create a new star and add it to the star group"""
		while len(self.stars) < 300:
			new_star = Star(self)
			self.stars.add(new_star)

# Game Running Functions
	def run_game(self):
		"""Start the main loop for the game"""
		while True:
			self._check_events()
	
			if self.stats.game_active == True:
				self.stats.game_run = True
				self.ship.update()
				self._update_power_up()
				self._create_meteors()
				self._update_power_up()
				self._update_meteors()
				self._update_bullets()
				self._update_aliens()
			clock.tick(fps)
			self._update_screen()

	def _update_screen(self):
		"""Update images on screen, flip to the new screen."""
		self.screen.fill(self.settings.bg_colour)
		self.stars.update()
		for star in self.stars.sprites():
			star.draw_star()
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.power_ups.update()
		for power_up in self.power_ups.sprites():
			power_up.draw_power_up()
		self.aliens.draw(self.screen)
		self.meteors.draw(self.screen)
		if self.settings.p_bullet:
			self.bullet_power_up.draw_power_up_text()
		if self.settings.p_slow:
			self.slow_power_up.draw_power_up_text()

		# Draw the score info
		self.sb.show_score()
		# Draw the play button if the game is inactive
		if not self.stats.game_active:
			if self.stats.game_run == True:
				self.game_over.draw_instructions()
			else:
				self.play_button.draw_button()
				self.instructions.draw_instructions()
		pygame.display.flip()

	def _start_game(self):
		"""Starts the game"""
		pygame.mixer.music.play(-1)
		# Reset the game settings
		self.settings.initialize_dynamic_settings()
		self.stats.reset_stats()
		self.settings.meteor_amount = self.settings.meteor_default
		self.stats.game_active = True
		self.sb.prep_score()
		self.sb.prep_level()
		self.sb.prep_lives()
		# Hides the cursor
		pygame.mouse.set_visible(False)
		# Get rid of any remaining aliens and bullets
		self.meteors.empty()
		self.aliens.empty()
		self.bullets.empty()
		# Create new fleet and centers ship
		self.ship.center_ship()
		self._kill_ship_movement()
		self._create_fleet()
		self._create_power_up()
		self.settings.p_bullet = False
		self.settings.p_slow = False

	def _prep_next_level(self):
		# Destroy existing bullets and create new fleet
		self.ship.center_ship()
		self.meteors.empty()
		self.bullets.empty()
		self._create_fleet()
		self.settings.increase_speed()
		self._create_power_up()
		# Increase level
		self.stats.level += 1
		self.sb.prep_level()

# Event Functions
	def _check_events(self):
		"""Respond to keypresses and mouse"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if self.stats.game_active == False:
				self._check_inactive_events(event)
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_inactive_events(self, event):
		# checks the key events after a restarted game
		if self.stats.game_run == True:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					self.stats.game_run = False
				elif event.key == pygame.K_ESCAPE:
					sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_pos = pygame.mouse.get_pos()
			if self.play_button.rect.collidepoint(mouse_pos):
				self._start_game()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				self._start_game()
			elif event.key == pygame.K_ESCAPE:
				sys.exit()

	def _check_keydown_events(self, event):
		"""Respond to key presses"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_d:
			self.ship.moving_right = True
		elif event.key == pygame.K_a:
			self.ship.moving_left = True
		elif event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_w:
			self.ship.moving_up = True
		elif event.key == pygame.K_s:
			self.ship.moving_down = True
		elif event.key == pygame.K_ESCAPE:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		"""Responds to key release"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False
		elif event.key == pygame.K_d:
			self.ship.moving_right = False
		elif event.key == pygame.K_a:
			self.ship.moving_left = False
		elif event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False
		elif event.key == pygame.K_w:
			self.ship.moving_up = False
		elif event.key == pygame.K_s:
			self.ship.moving_down = False

# Ship Functions
	def _ship_hit(self):
		"""Respond to ship being hit"""
		# Decrement lives_left
		if self.stats.lives_left > 1:
			self.stats.lives_left -= 1
			self.sb.prep_lives()
			# Get rid of any remaining aliens and bullets
			self.aliens.empty()
			self.bullets.empty()
			self.meteors.empty()
			# Create new fleet and center the ship
			self.ship.center_ship()
			self._create_fleet()
			# Pause.
			sleep(0.5)
		else:
			# Sets game inactive
			self.meteors.empty()
			self.aliens.empty()
			self.bullets.empty()
			self.power_ups.empty()
			self.stats.lives_left = 0
			self.sb.prep_lives()
			self.ship.center_ship()
			self._kill_ship_movement()
			self.settings.p_bullet = False
			self.settings.p_slow = False
			self.stats.game_active = False
			pygame.mouse.set_visible(True)

	def _kill_ship_movement(self):
		self.ship.moving_right = False
		self.ship.moving_left = False
		self.ship.moving_up = False
		self.ship.moving_down = False

# Bullet Fucntions
	def _update_bullets(self):
		"""Update bullet pos"""
		self.bullets.update()
			# Get rid of bullets
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)
		self._check_bullet_alien_collision()

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
			self._prep_next_level()

	def _fire_bullet(self):
		"""Create a new bullet and add it to the bullets group"""
		if len(self.bullets) < self.settings.bullet_count:
			# Plays pew pew sound everytime a bullet is fired
			pygame.mixer.Sound.play(self.settings.laser)
			new_bullet = Bullet(self, self.settings.main_gun)
			self.bullets.add(new_bullet)
			if self.settings.p_bullet == True:
				new_bullet = Bullet(self, self.settings.left_gun)
				self.bullets.add(new_bullet)
				new_bullet = Bullet(self, self.settings.right_gun)
				self.bullets.add(new_bullet)

# Power Up Functions
	def _update_power_up(self):
		collisions = pygame.sprite.spritecollide(
			self.ship, self.power_ups, False)
		if collisions:
			for power in collisions:
				self._check_power_up(power)
				self.power_ups.remove(power)
		for power in self.power_ups:
			if power.rect.bottom <= 0:
				self.power_ups.remove(power)
		if self.settings.p_slow:
			self.current_time = pygame.time.get_ticks()
			self._initiate_slow_power_up()
		if self.settings.p_bullet:
			self.current_time = pygame.time.get_ticks()
			self._initiate_bullet_power_up()

	def _create_power_up(self):
		self.generator.generate_power_up()
		self.power_ups.add(self.generator.power_up)
	
	def _check_power_up(self, power_up):
		if isinstance(power_up, LifePowerUp):
			self.stats.lives_left += 1
			self.sb.prep_lives()
		elif isinstance(power_up, SlowPowerUp):
			self.slow_timer = pygame.time.get_ticks()
			self.settings.p_slow = True
		elif isinstance(power_up, BulletPowerUp):
			self.bullet_timer = pygame.time.get_ticks()
			self.settings.p_bullet = True

	def _initiate_bullet_power_up(self):
		if not self.settings.p_bullet_init:
			self.temp_bullet_count = self.settings.bullet_count
			self.settings.bullet_count = self.settings.p_bullet_count
			self.settings.p_bullet_init = True
		if self.current_time - self.bullet_timer > 10000: 
			self.settings.p_bullet = False
			self.settings.p_bullet_init = False
			self.settings.bullet_count = self.temp_bullet_count
			
	def _initiate_slow_power_up(self):
		# self.current_time = pygame.time.get_ticks()
		slow_power_up = SlowPowerUp(self)
		slow_power_up.draw_power_up_text()
		if not self.settings.p_slow_init:
			self.temp_speed = self.settings.alien_speed
			self.settings.alien_speed /= 2
			self.settings.p_slow_init = True
		if self.current_time - self.slow_timer > 10000: 
			self.settings.p_slow = False
			self.settings.p_slow_init = False
			self.settings.alien_speed = self.temp_speed

# Meteor Fucntions
	def _check_meteor_collisions(self):
		ship_collisions = pygame.sprite.spritecollide(
			self.ship, self.meteors, False)
		if ship_collisions:
			for sprite in ship_collisions:
				self.meteors.remove(sprite)
			if self.stats.lives_left > 1:
				self.stats.lives_left -= 1
				self.sb.prep_lives()
			else:
				# Sets game inactive
				self.meteors.empty()
				self.power_ups.empty()
				self.bullets.empty()
				self.stats.lives_left = 0
				self.sb.prep_lives()
				self.ship.center_ship()
				self.stats.game_active = False
				pygame.mouse.set_visible(True)
		bullet_collisions = pygame.sprite.groupcollide(
			self.bullets, self.meteors, True, True)
		if bullet_collisions:
			for meteor in bullet_collisions:
				self.meteors.remove(meteor)
		
	def _create_meteors(self):
		while len(self.meteors) < self.settings.meteor_amount:
			m = Meteor(self)
			self.meteors.add(m)

	def _update_meteors(self):
		for meteor in self.meteors.sprites():
			meteor.update()
			if meteor.y >= self.settings.screen_height:
				self.meteors.remove(meteor)
		self._check_meteor_collisions()

# Alien Fucntions
	def _check_aliens_bottom(self):
		"""Cheack if aliens have reached the bottom"""
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				# Counts hit if aliens reach bottom
				self._ship_hit()
				break

	def _update_aliens(self):
		"""check fleet edge, update pos"""
		self._check_fleet_edges()
		self.aliens.update()
		# Looks for alien ship collisions
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()
		# Looks for aliens hitting bottom of screen
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
		# Creates alien and find number of aliens in row
		# Spacing between each alien is equal to one alien width
		alien = Alien(self)
		available_space_x = self.settings.screen_width - (2 * alien.rect.width)
		number_aliens_x = available_space_x // (2 * alien.rect.width)

		# Determine number of rows
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height -
								(7 * alien.rect.height) - ship_height)
		number_rows = available_space_y // (2 * alien.rect.height)

		# Create the fleet of aliens
		for row_number in range(number_rows):
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_number, row_number)
			
	def _create_alien(self, alien_number, row_number):
		"""Create an alien and place it in the row"""
		alien = Alien(self)
		alien.x = alien.rect.width + 2 * alien.rect.width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number + 30
		self.aliens.add(alien)

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()

