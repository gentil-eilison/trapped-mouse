import pygame, sys
from pygame.locals import *
from constants import *

from classes import Mouse, Wall, Path


maze_layout = [
    [1, 1, 1, 1],
    [1, 2, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 1, 1]
]

maze_cells = list()


class Game:
    def __init__(self):
        self.__display_surf = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.__frames_per_sec = pygame.time.Clock()
        pygame.display.set_caption(GAME_TITLE)
        self.__all_sprites = pygame.sprite.Group()
        self.__walls_sprites = pygame.sprite.Group()
        self.__mouse = None
    
    def run(self, maze_layout):
        pygame.init()
        self.create_maze(maze_layout)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self.__display_surf.fill(Color("#2D2D2D"))    
            # self.create_maze(maze_layout)

            for entity in self.__all_sprites:
                self.__display_surf.blit(entity.image, entity.rect)
                if not isinstance(entity, (Wall, Path)):
                    entity.move()
                
            if pygame.sprite.spritecollideany(self.__mouse, self.__walls_sprites):
                pygame.display.update()
                print("pov: você bateu na parede")

            pygame.display.update()
            self.__frames_per_sec.tick(FPS)
        
    def create_maze(self, maze_layout: list[list]):

        row_position = 24
        column_position = 24
        path_row_position = 0
        path_column_position = 0
        mouse_row_position = None
        mouse_column_position = None

        for _, row_value in enumerate(maze_layout):
            for _, column_value in enumerate(row_value):
                if column_value == 1:
                    wall = Wall((column_position, row_position))
                    self.__walls_sprites.add(wall)
                    self.__all_sprites.add(wall)
                elif column_value == 0:
                    self.__all_sprites.add(
                        Path((column_position, row_position))
                    )
                elif column_value == 2:
                    mouse_row_position = row_position
                    mouse_column_position = column_position
                    self.__all_sprites.add(
                        Path((column_position, row_position))
                    )
                
                column_position += 48
                path_column_position += 48

            row_position += 48
            column_position = 24
            path_row_position += 48
            path_column_position = 0
        
        self.__mouse = Mouse((mouse_column_position, mouse_row_position))
        self.__all_sprites.add(self.__mouse)


if __name__ == "__main__":
    game = Game()
    game.run(maze_layout)