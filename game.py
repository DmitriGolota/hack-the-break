"""
Member List
- Sally
- Marti
- Chansaa
- Subin

Mar 13, 2021
"""

import pygame
import sys
import random
from pygame_functions import *



pygame.init()

WINDOW_SIZE = (500, 500)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
clock = pygame.time.Clock()

bg = pygame.image.load('/assets/background.jpg')
testSprite = newSprite("./assets/Namu1.gif", 12) # 12 is the gif frame


running = True

while running:

    for event in pygame.event.get():      # catch all the events that are happening right now
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # image of player
    # background image

    pygame.display.update()
    clock.tick(120)

def movement():

    nextFrame = clock()
    frame = 0

    while True:
        if clock() > nextFrame:
            frame = (frame + 1) % 12
            nextFrame += 120
        if keyPressed("right"):
            changeSpriteImage(testSprite, 0*12 + frame)
        elif keyPressed("down"):
            changeSpriteImage(testSprite, 1*12 + frame)
        elif keyPressed("left"):
            changeSpriteImage(testSprite, 2*12 + frame)
        elif keyPressed("right"):
            changeSpriteImage(testSprite, 3*12 + frame)
