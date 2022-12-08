import pygame as pg
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self, settings, screen, ship):
		super(Bullet, self).__init__()
		self.settings = settings
		self.screen = screen
		
		self.image = self.settings.SHIP_MISSILE
		self.rect = self.image.get_rect()
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		self.y = self.rect.y
		
		self.speed = self.settings.SHIP_BULLET_SPEED
		
	def update(self):
		self.y -= self.speed
		self.rect.y = self.y
		
	def draw_bullet(self):
		self.screen.blit(self.settings.SHIP_MISSILE, self.rect)
