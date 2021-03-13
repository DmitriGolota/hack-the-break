"""
Member List
- Sally Poon
- Martin Gatchev
- Batchansaa Batzorig
- Subin Moon

Mar 13, 2021
"""
import pygame
import sys
import random
from pygame_functions import *


# Game functions
def draw_background():
    pass


pygame.init()

WINDOW_SIZE = (500, 500)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
clock = pygame.time.Clock()

# Game Variables
bg_surface = pygame.image.load('/assets/background.jpg')

namu_surface = 1

game_active = True

while True:
    for event in pygame.event.get():      # catch all the events that are happening right now
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if game_active:
        # Game functions ...
        pass

    # image of player
    # background image

    pygame.display.update()
    clock.tick(120)
