import time
import pygame, sys
from pygame.locals import *
from constants import *

from classes import Mouse, Wall, Path, Cell, Stack, Cheese


maze_layout = [
    [1, 1, 3, 1],
    [1, 0, 0, 0],
    [1, 0, 1, 1],
    [1, 0, 2, 1],
    [1, 1, 1, 1]
]

class Game:
    def __init__(self):
        self.__display_surf = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        self.__mouse = None
        self.__frames_per_sec = pygame.time.Clock()
        self.__all_sprites = pygame.sprite.Group()
        self.__maze_cells = list()
        self.__maze_stack = Stack()
        self.__walls_sprites = pygame.sprite.Group()

    def __get_cell_by_position(self, coordinates: tuple[int]) -> Cell:
        for cell in self.__maze_cells:
            if (cell.top, cell.left) == coordinates:
                return cell
    
    def __get_mouse_current_cell(self):
        mouse_coordinates = self.__mouse.get_coordinates()
        current_cell = self.__get_cell_by_position(mouse_coordinates)
        current_cell.visited = True
        return current_cell

    def _find_next_cells(self, mouse_coordinates: tuple[int]) -> dict:
        top_cell_coordinates = mouse_coordinates[0] - 48, mouse_coordinates[1]
        bottom_cell_coordinates = mouse_coordinates[0] + 48, mouse_coordinates[1]
        left_cell_coordinates = mouse_coordinates[0], mouse_coordinates[1] - 48
        right_cell_coordinates = mouse_coordinates[0], mouse_coordinates[1] + 48

        next_cells = dict(
            top=Cell(0, 0, color=BLACK_COLOR),
            left=Cell(0, 0, color=BLACK_COLOR),
            right=Cell(0, 0, color=BLACK_COLOR),
            bottom=Cell(0, 0, color=BLACK_COLOR)
        )

        for cell in self.__maze_cells:
            if (cell.top, cell.left) == top_cell_coordinates:
                next_cells["top"] = cell
            if (cell.top, cell.left) == left_cell_coordinates:
                next_cells["left"] = cell
            if (cell.top, cell.left) == right_cell_coordinates:
                next_cells["right"] = cell
            if (cell.top, cell.left) == bottom_cell_coordinates:
                next_cells["bottom"] = cell
        return next_cells

    def run(self, maze_layout):
        pygame.init()
        self.create_maze(maze_layout)
        current_cell = self.__get_mouse_current_cell()
        self.__maze_stack.append(current_cell)
        while not current_cell.exit:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self.__display_surf.fill(Color("#2D2D2D"))

            for entity in self.__all_sprites:
                self.__display_surf.blit(entity.image, entity.rect)
                if not isinstance(entity, (Wall, Path, Cheese)):
                    next_cells = self._find_next_cells((current_cell.top, current_cell.left))
                    if next_cells["right"].can_move_to_cell():
                        self.__mouse.move_right()
                        next_cells["right"].visited = True
                        self.__maze_stack.append(next_cells["right"])
                    elif next_cells["left"].can_move_to_cell():
                        self.__mouse.move_left()
                        next_cells["left"].visited = True
                        self.__maze_stack.append(next_cells["left"])
                    elif next_cells["bottom"].can_move_to_cell():
                        self.__mouse.move_bottom()
                        next_cells["bottom"].visited = True
                        self.__maze_stack.append(next_cells["bottom"])
                    elif next_cells["top"].can_move_to_cell():
                        self.__mouse.move_top()
                        next_cells["top"].visited = True
                        self.__maze_stack.append(next_cells["top"])
                    else:
                        previous_cell = self.__maze_stack.pop()
                        self.__mouse.rect.centery, self.__mouse.rect.centerx = previous_cell.top, previous_cell.left
                    
                    current_cell = self.__get_mouse_current_cell()
            time.sleep(0.2)
            pygame.display.update()
            self.__frames_per_sec.tick(FPS)
        
    def create_maze(self, maze_layout: list[list]):

        row_position = 24
        column_position = 24
        mouse_row_position = None
        mouse_column_position = None

        for _, row_value in enumerate(maze_layout):
            for _, column_value in enumerate(row_value):
                if column_value == 1:
                    wall = Wall((column_position, row_position))
                    self.__walls_sprites.add(wall)
                    self.__all_sprites.add(wall)
                    self.__maze_cells.append(Cell(row_position, column_position, color=BLACK_COLOR))
                elif column_value == 0:
                    self.__all_sprites.add(
                        Path((column_position, row_position))
                    )
                    self.__maze_cells.append(Cell(row_position, column_position, color=WHITE_COLOR))
                elif column_value == 2:
                    mouse_row_position = row_position
                    mouse_column_position = column_position
                    self.__all_sprites.add(
                        Path((column_position, row_position))
                    )
                elif column_value == 3:
                    self.__all_sprites.add(
                        Path((column_position, row_position))
                    )
                    self.__all_sprites.add(
                        Cheese((column_position, row_position))
                    )
                    self.__maze_cells.append(Cell(row_position, column_position, exit=True, color=WHITE_COLOR))
                
                column_position += 48

            row_position += 48
            column_position = 24
        
        self.__mouse = Mouse((mouse_column_position, mouse_row_position))
        self.__all_sprites.add(self.__mouse)
        self.__maze_cells.append(Cell(left=self.__mouse.center[0], top=self.__mouse.center[1], color=WHITE_COLOR))


if __name__ == "__main__":
    game = Game()
    game.run(maze_layout)