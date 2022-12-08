import pygame as pg

class Ship():
	def __init__(self, screen, settings):
		self.settings = settings
		self.screen = screen
		self.rect = self.settings.IMG_SHIP.get_rect()
		
		self.screen_rect = screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += self.settings.SHIP_SPEED
		if self.moving_left and self.rect.left > 0:
			self.rect.centerx -= self.settings.SHIP_SPEED
				
	def blitme(self):
		self.screen.blit(self.settings.IMG_SHIP, self.rect)
		
		
		
