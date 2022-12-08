import pygame as pg
import sys
from ship import Ship
from settings import Settings
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def play_game():
	pg.init()
	settings = Settings()
	
	screen = pg.display.set_mode((settings.WIDTH, settings.HEIGHT))
	pg.display.set_caption('SPACE INVADER')
	
	ship = Ship(screen, settings)
	
	aliens = Group()
	gf.alien_group(settings, screen, ship, aliens)
	
	bullets = Group()

	while True:
		gf.check_events(settings, screen, ship, bullets)
		
		ship.update()
		gf.update_bullets(settings, screen, ship, aliens, bullets)
		gf.update_aliens(aliens, ship, settings)	
		
		gf.update_screen(settings, screen, ship, aliens, bullets)
     

play_game()
