import pygame
import os 
import time
import random

pygame.init()

width, height = 750, 750
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Shooter")
FPS = 30
clock = pygame.time.Clock()

# load imgaes
enemy_ship = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
player_ship = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))
enemy_laser = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
player_laser = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))
background = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (width, height)) #scaled bg to window size.


def text_to_screen(msg, font_color, font_size, x, y):
	font = pygame.font.SysFont("comicsansms", font_size)
	text = font.render(msg, True, font_color)
	window.blit(text, (x, y))

def gameloop():
	run = True
	score = 0

	while run:
		window.blit(background, (0,0))

		# Event handling loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		text_to_screen(f"Score: {score}", (255, 255, 255), 20, 0, 0)

		clock.tick(FPS)
		pygame.display.update()

gameloop()