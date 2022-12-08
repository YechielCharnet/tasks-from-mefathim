import pygame as pg

class Settings():
	def __init__(self):
		
		#screen settings
		self.WIDTH, self.HEIGHT = 1250, 900
		self.IMG_SCREEN = pg.image.load('space.png')
		
		#ship settings
		self.IMG_SHIP = pg.image.load('ship.png')
		self.SHIP_SPEED = 2
		
		#ship's bullet settings
		self.SHIP_BULLET_SPEED = 2
		self.SHIP_MISSILE = pg.transform.scale(pg.image.load('Missile_s.png'), (10,35))
		
		#aliens settings
		self.IMAGE_ALIEN = pg.image.load('alien_.png')
		self.ALIEN_SPEED = 1
		self.GROUP_DROP_SPEED = 50
		self.GROUP_DIRECTION = 1
		

