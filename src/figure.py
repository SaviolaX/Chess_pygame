import pygame
import numpy as np

from pygame.surface import Surface
from dataclasses import dataclass

from .constants import Config, WHITE_PIECES, BLACK_PIECES


@dataclass
class Figure:
    name: str
    color: str
    pos_x: float
    pos_y: float
    width: int = Config.FIGURE_WIDTH
    height: int = Config.FIGURE_HEIGHT
    selected: bool = False
    moved: bool = False

    def draw(self, screen: Surface) -> None:
        """Draws figure on the screen(board)"""
        if self.color == "black":
            piece_image = pygame.image.load(BLACK_PIECES[self.name].value)

        if self.color == "white":
            piece_image = pygame.image.load(WHITE_PIECES[self.name].value)

        piece_image = pygame.transform.scale(piece_image, (self.width, self.height))
        piece_rect = piece_image.get_rect(
            center=(
                (self.pos_x + Config.BOARD_MARGIN_X)
                + (Config.BOARD_MARGIN_X // 2)
                - 2,  # 2 - magic number, taken to align figures visually
                (self.pos_y + Config.BOARD_MARGIN_Y) + Config.BOARD_MARGIN_Y // 2,
            )
        )
        screen.blit(piece_image, piece_rect)

        if self.selected:
            pygame.draw.rect(screen, (0, 0, 0), piece_rect, 2)

    def move(self) -> None:
        """Moves figure on the screen(board)"""
        ...

    def remove(self) -> None:
        """Removes figure from the screen(board)"""
        ...


def define_figures_position(squares: list) -> list[Figure]:
    # Convert a list to 8x8 matrix
    square_matrix = np.array(squares).reshape((8, 8))

    # Define mappings for pieces
    white_high_pieces_mapping = Config.hight_pieces_mapping
    white_low_pieces_mapping = Config.low_pieces_mapping
    black_high_pieces_mapping = Config.hight_pieces_mapping
    black_low_pieces_mapping = Config.low_pieces_mapping

    # Define positions for white and black figures
    white_positions = [(0, white_high_pieces_mapping), (1, white_low_pieces_mapping)]
    black_positions = [(-1, black_high_pieces_mapping), (-2, black_low_pieces_mapping)]

    result = []

    # Loop over white and black positions
    for pos, mapping in white_positions + black_positions:
        for i, square in enumerate(square_matrix[pos]):
            figure = Figure(
                pos_x=square.pos_x,
                pos_y=square.pos_y,
                name=mapping[i],
                color="white" if pos >= 0 else "black",
            )
            result.append(figure)

    return result
