import pygame

from pygame.surface import Surface
from pygame.rect import Rect
from dataclasses import dataclass

from .figure import Figure
from .constants import Config, RGBColors
from .moves import pawn

pygame.font.init()


@dataclass
class Square:
    """Board square"""

    color: RGBColors = None
    width: float = Config.SQUARE_WIDTH
    height: float = Config.SQUARE_HEIGHT
    pos_x: int = None
    pos_y: int = None
    selected: bool = False

    def draw(self) -> Rect:
        obj = pygame.rect.Rect(self.pos_x, self.pos_y, self.width, self.height)
        return obj


@dataclass
class BoardRenderer:
    """Gaming surface"""

    screen: Surface
    squares: list[Square]
    figures: list[Figure]
    font = pygame.font.Font(None, Config.FONT_SIZE)

    def draw(self) -> None:
        # draw squares
        for square in self.squares:
            pygame.draw.rect(
                self.screen,
                square.color.value,
                square.draw(),
            )
            if square.selected:
                hightlight_rect = pygame.rect.Rect(
                    square.pos_x + 5,
                    square.pos_y + 5,
                    square.width - 10,
                    square.height - 10,
                )
                pygame.draw.rect(self.screen, RGBColors.GREY.value, hightlight_rect, 1)

        # draw side letters
        self._draw_letters()

        # draw top and bottom numbers
        self._draw_numbers()

    def draw_figures(self) -> None:
        for figure in self.figures:
            figure.draw(screen=self.screen)

    def _draw_letters(self) -> None:
        for row in range(Config.GRID_SIZE):
            letter = Config.LETTER_MAPPING.get(row, "")
            text = self.font.render(letter.capitalize(), True, RGBColors.WHITE.value)

            # draw on the right side
            text_rect_right = text.get_rect(
                center=(
                    (Config.BOARD_MARGIN_Y + Config.BOARD_WIDTH * 2 // 2) + 15,
                    (row * Config.SQUARE_HEIGHT + Config.SQUARE_WIDTH // 2) + 30,
                )
            )
            self.screen.blit(text, text_rect_right)

            # draw on the left side
            text_rect_left = text.get_rect(
                center=(
                    Config.BOARD_MARGIN_Y // 2,
                    (row * Config.SQUARE_HEIGHT + Config.SQUARE_WIDTH // 2) + 30,
                )
            )
            self.screen.blit(text, text_rect_left)

    def _draw_numbers(self) -> None:
        number_mapping = {v: str(k + 1) for k, v in Config.LETTER_MAPPING.items()}

        for col in range(Config.GRID_SIZE):
            number = number_mapping.get(Config.LETTER_MAPPING.get(col, ""), "")
            text = self.font.render(number, True, RGBColors.WHITE.value)

            # top numbers
            text_rect_top = text.get_rect(
                center=(
                    ((col * Config.SQUARE_HEIGHT + Config.SQUARE_WIDTH // 2) + 30),
                    Config.BOARD_MARGIN_X // 2,
                )
            )
            self.screen.blit(text, text_rect_top)

            # bottom numbers
            text_rect_bottom = text.get_rect(
                center=(
                    ((col * Config.SQUARE_HEIGHT + Config.SQUARE_WIDTH // 2) + 30),
                    (Config.BOARD_MARGIN_X + Config.BOARD_HEIGHT * 2 // 2) + 15,
                )
            )
            self.screen.blit(text, text_rect_bottom)


@dataclass
class BoardInteraction:
    figures: list[Figure]
    squares: list[Square]

    def get_obj_by_coordinates(
        self, obj_list: list, mouse_x: float, mouse_y: float
    ) -> Figure | Square:
        result = None

        for obj in obj_list:
            if (
                obj.pos_x < mouse_x < obj.pos_x + obj.width
                and obj.pos_y < mouse_y < obj.pos_y + obj.height
            ):
                result = obj

        return result

    def select_figure(self, figure: Figure) -> Figure:
        self.unselect_all(self.figures)
        self.unselect_all(self.squares)

        if figure is not None:
            figure.selected = True

            print(f"Selected: {figure}")

        return figure

    def highlight_figure_move(
        self,
        mouse_x: float,
        mouse_y: float,
        figure: Figure,
    ) -> list[Square]:
        if figure is not None:
            if figure.name == "PAWN":
                pawn.highlight_move(mouse_x, mouse_y, figure, self)
                pawn.highlight_attack(mouse_x, mouse_y, figure, self)

    def move_figure(self, figure: Figure, square: Square) -> None:       
            
        if square.selected:
            figure.pos_x = square.pos_x
            figure.pos_y = square.pos_y
            figure.selected = False
            figure.moved = True

        self.unselect_all(self.squares)
        

    def unselect_all(self, lst: list) -> None:
        for x in lst:
            if x.selected:
                x.selected = False


def define_squares_position() -> list[Square]:
    squares_list = []

    for row in range(Config.GRID_SIZE):
        for col in range(Config.GRID_SIZE):
            square_x = col * Config.SQUARE_WIDTH + Config.BOARD_MARGIN_X
            square_y = row * Config.SQUARE_HEIGHT + Config.BOARD_MARGIN_Y

            # fill squares with colors
            square_color = (
                RGBColors.DARK_YELLOW if (row + col) % 2 == 0 else RGBColors.WHITE
            )
            # fill up the square object data
            square = Square()
            square.color = square_color
            square.pos_x = square_x
            square.pos_y = square_y
            squares_list.append(square)

    return squares_list
