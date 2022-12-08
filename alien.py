import pygame as pg
from pygame.sprite import Sprite
import sys

class Alien(Sprite):
	def __init__(self, settings, screen):
		super(Alien, self).__init__()
		self.screen = screen
		self.settings = settings
		
		self.image = settings.IMAGE_ALIEN
		self.rect = self.image.get_rect()
		
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		self.x = float(self.rect.x)
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)
		
	def check_edges(self):
		screen_rect = self.screen.get_rect()
		if self.rect.bottom >= screen_rect.bottom:
			print(' GAME OVER, ALIEN GOT TO EARTH ): ')
			sys.exit()
		elif self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
		
	def update(self):
		self.x += (self.settings.ALIEN_SPEED * self.settings.GROUP_DIRECTION)
		self.rect.x = self.x
		
		
				
