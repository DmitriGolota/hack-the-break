import game
from pygame_functions import *
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Game Classes

class Namu(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = True
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f1.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f2.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f3.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f4.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f5.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f6.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f7.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f8.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f9.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f10.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f11.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f12.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]


    def update(self):
        if self.is_animating:
            self.current_sprite += 1

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

            self.image = self.sprites[self.current_sprite]

        # Move the sprite based on user keypresses.
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)


class NamuMamu(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = True
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f1.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f2.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f3.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f4.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f5.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f6.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f7.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f8.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f9.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f10.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f11.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f12.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f13.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f14.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f15.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f16.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f17.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f18.png"))


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.bottomright = [pos_x, pos_y]


    def update(self):
        if self.is_animating:
            self.current_sprite += 1

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

            self.image = self.sprites[self.current_sprite]
