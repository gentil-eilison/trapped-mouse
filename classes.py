import pygame
from pygame.locals import *
from constants import BLACK_COLOR


class Cheese(pygame.sprite.Sprite):
    def __init__(self, center: tuple[int]):
        super().__init__()
        self.__image = pygame.image.load("sprites/cheese32.png")
        self.__rect = self.__image.get_rect()
        self.__rect.center = center

    @property
    def image(self):
        return self.__image
    
    @property
    def rect(self):
        return self.__rect


class Path(pygame.sprite.Sprite):
    def __init__(self, center: tuple[int]):
        super().__init__()
        self.__image = pygame.image.load("sprites/path48.jpg")
        self.__rect = self.__image.get_rect()
        self.__rect.center = center
    
    @property
    def image(self):
        return self.__image
    
    @property
    def rect(self):
        return self.__rect


class Wall(pygame.sprite.Sprite):
    def __init__(self, center: tuple[int]):
        super().__init__()
        self.__image = pygame.image.load("sprites/wall48.gif")
        self.__rect = self.__image.get_rect()
        self.__rect.center = center
    
    @property
    def image(self):
        return self.__image
    
    @property
    def rect(self):
        return self.__rect


class Mouse(pygame.sprite.Sprite):
    def __init__(self, center: tuple[int]):
        super().__init__()
        self.__image = pygame.image.load("sprites/mouse32.png")
        self.__rect = self.__image.get_rect()
        self.__rect.center = center
        self.__center = self.__rect.center
    
    @property
    def image(self):
        return self.__image
    
    @property
    def rect(self):
        return self.__rect

    @property
    def center(self):
        return self.__center

    def get_coordinates(self) -> tuple[int]:
        return self.__rect.centery, self.__rect.centerx

    def move_left(self) -> None:
        self.__rect.move_ip(-48, 0)

    def move_right(self) -> None:
        self.__rect.move_ip(48, 0)

    def move_top(self) -> None:
        self.__rect.move_ip(0, -48)

    def move_bottom(self) -> None:
        self.__rect.move_ip(0, 48)


class Stack:
    def __init__(self):
        self.__stack = list()
    
    def append(self, item):
        self.__stack.append(item)
    
    def pop(self):
        try:
            return self.__stack.pop()
        except IndexError:
            print("Stack is empty")
    

class Cell:
    def __init__(self, top: int, left: int, color: int, visited: bool = False, exit: bool = False):
        self.__top = top
        self.__left = left
        self.__visited = visited
        self.__exit = exit
        self.__color = color

    @property
    def color(self) -> int:
        return self.__color
    
    @property
    def top(self) -> int:
        return self.__top
    
    @property
    def left(self) -> int:
        return self.__left

    @property
    def exit(self) -> bool:
        return self.__exit
    
    @property
    def visited(self) -> bool:
        return self.__visited

    @visited.setter
    def visited(self, new_visited: bool):
        self.__visited = new_visited
    
    def can_move_to_cell(self) -> bool:
        return self.color != BLACK_COLOR and not self.visited
    
    def __str__(self):
        return f"Y: {self.top} - X: {self.left}"

    def __repr__(self):
        return f"Y: {self.top} - X: {self.left}"

