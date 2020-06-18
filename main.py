import pygame
import os 
import time
import random

pygame.init()

width, height = 750, 750
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Shooter")
FPS = 60
clock = pygame.time.Clock()

# load imgaes
enemy_ship = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
player_ship = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))
enemy_laser = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
player_laser = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))
background = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (width, height)) #scaled bg to window size.

# common properties of player and enemy ship so later we can create multiple instances of it.
class Ship:
	def __init__(self, x, y, health= 100):
		self.x = x
		self.y = y
		self.health = health
		self.ship_img = None
		self.laser_img = None
		self.lasers = []
		self.cool_down_counter = 0

	def draw(self, window):
		window.blit(self.ship_img, (self.x, self.y))

	# To get width and height of img for keeping it inside boundry all the time.
	def get_width(self):
		return self.ship_img.get_width()

	def get_height(self):
		return self.ship_img.get_height()


# Importing from parent class
class Player(Ship):
	def __init__(self, x, y, health= 100):
		super().__init__(x, y, health)
		self.ship_img = player_ship
		self.laser_img = player_laser
		self.mask = pygame.mask.from_surface(self.ship_img) #masks in pygame allows for pixel perfect collision, it masks only part of img where pixels are present and not whole img rect.
		self.max_health = health	

class Enemy(Ship):
	def __init__(self, x, y, health= 100):
		super().__init__(x, y, health)
		self.ship_img = enemy_ship
		self.laser_img = enemy_laser
		self.mask = pygame.mask.from_surface(self.ship_img)

	# as enemies would be moving downwards always.
	def move(self, vel):
		self.y += vel


def text_to_screen(msg, font_color, font_size, x, y):
	font = pygame.font.SysFont("comicsansms", font_size)
	text = font.render(msg, True, font_color)
	window.blit(text, (x, y))

def gameloop():
	run = True
	score = 0
	player_vel = 5
	player = Player(300, 600)
	while run:
		window.blit(background, (0,0))

		# Event handling loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		# Player movement handling and also keeping inside boundry.
		keys = pygame.key.get_pressed()
		if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player.x + player_vel > 0:
			player.x -= player_vel
		if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player.x + player_vel + player.get_width() < width:
			player.x += player_vel
		if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player.y + player_vel + player.get_height() < height:
			player.y += player_vel
		if (keys[pygame.K_w] or keys[pygame.K_UP]) and player.y + player_vel > 0:
			player.y -= player_vel

		player.draw(window)
		text_to_screen(f"Score: {score}", (255, 255, 255), 20, 0, 0)

		clock.tick(FPS)
		pygame.display.update()

gameloop()