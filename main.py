import pygame, sys
from pygame.locals import *
from constants import *


maze_layout = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 0]
]


class Game:
    def __init__(self):
        self.__display_surf = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.__frames_per_sec = pygame.time.Clock()
        pygame.display.set_caption(GAME_TITLE)
        self.__display_surf.fill(Color(200, 124, 67))
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            self.__frames_per_sec.tick(FPS)
        
    def create_maze(self, maze_layout: list[list]):
        white_square = Color(COLORS["white"])
        black_square = Color(COLORS["black"])

        row_position = 0
        column_position = 0

        for _, row_value in enumerate(maze_layout):
            for _, column_value in enumerate(row_value):
                if column_value == 1:
                    pygame.draw.rect(
                        self.__display_surf,
                        black_square,
                        Rect(column_position, row_position, 24, 24)
                    )
                else:
                    pygame.draw.rect(
                        self.__display_surf,
                        white_square,
                        Rect(column_position, row_position, 24, 24)
                    )
                
                column_position += 21

            row_position += 21
            column_position = 0


if __name__ == "__main__":
    game = Game()
    game.create_maze(maze_layout)
    game.run()