import pygame as pg
import sys
from bullet import Bullet
from alien import Alien

################### alien's functions ################################
def get_number_alians(settings, alien_width):
	available_space_x = settings.WIDTH - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x
	
def get_number_rows(settings, ship_height, alien_height):
	available_space_y = (settings.HEIGHT - (3 * alien_height) - ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows
	
def create_alien(settings, screen, aliens, alien_number, row_number):
	alien = Alien(settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)


def alien_group(settings, screen, ship, aliens):
	alien = Alien(settings, screen)
	# getting coordinates to place the alien
	number_aliens_x = get_number_alians(settings, alien.rect.width)
	number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)
	# adding aliens to the alien group
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(settings, screen, aliens, alien_number, row_number)


# controling the moovement of the aliens group
def change_group_direction(settings, aliens):
	for alien in aliens.sprites():
		alien.rect.y += settings.GROUP_DROP_SPEED
	settings.GROUP_DIRECTION *= -1

def check_group_edges(settings, aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_group_direction(settings, aliens)
			break			

def update_aliens(aliens, ship, settings):
	check_group_edges(settings, aliens)
	aliens.update()
	if pg.sprite.spritecollideany(ship, aliens):
		print(" GAME OVER, SHIP WAS HIT!!! ")
		sys.exit()
#######################################################################
		
def check_events(settings, screen, ship, bullets):
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()
			
		elif event.type == pg.KEYDOWN:
			if event.key == pg.K_SPACE:
				new_bullet = Bullet(settings, screen, ship)
				bullets.add(new_bullet)

			elif event.key == pg.K_RIGHT:
				ship.moving_right = True
			elif event.key == pg.K_LEFT:
				ship.moving_left = True
		
		elif event.type == pg.KEYUP:
			if event.key == pg.K_RIGHT:
				ship.moving_right = False
			elif event.key == pg.K_LEFT:
				ship.moving_left = False			

#####################
def update_bullets(settings, screen, ship, aliens, bullets):
	collisions = pg.sprite.groupcollide(bullets, aliens, True, True)
	if len(aliens) == 0:
		bullets.empty()
		alien_group(settings, screen, ship, aliens)
	bullets.update()
	for bullet in  bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)	

######################		
def update_screen(settings, screen, ship, aliens, bullets):
	screen.blit(settings.IMG_SCREEN, (0, 0))
	
	for bullet in bullets.sprites():
		 bullet.draw_bullet()
	
	ship.blitme()
	aliens.draw(screen)
	pg.display.flip()

