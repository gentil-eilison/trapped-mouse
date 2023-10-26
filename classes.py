import pygame
from pygame.locals import *


class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.__image = pygame.image.load("sprites/mouse32.png")
        self.__rect = self.__image.get_rect()
        self.__rect.center = (24, 24)
    
    @property
    def image(self):
        return self.__image
    
    @property
    def rect(self):
        return self.__rect

    def move(self):
        pressed_key = pygame.key.get_pressed()

        if self.__rect.top != 8:
            if pressed_key[K_UP]:
                self.__rect.move_ip(0, -48)

        if self.__rect.bottom != 184:
            if pressed_key[K_DOWN]:
                self.__rect.move_ip(0, 48)

        if self.__rect.left != 8:
            if pressed_key[K_LEFT]:
                self.__rect.move_ip(-48, 0)
        if self.__rect.right < 168:
            if pressed_key[K_RIGHT]:
                self.__rect.move_ip(48, 0)
