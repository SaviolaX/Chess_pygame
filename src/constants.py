from enum import Enum


class Config:
    GRID_SIZE = 8

    BOARD_WIDTH = 700
    BOARD_HEIGHT = 700

    BOARD_MARGIN_X = 30
    BOARD_MARGIN_Y = 30

    FIGURE_WIDTH = BOARD_WIDTH / GRID_SIZE - 10
    FIGURE_HEIGHT = BOARD_WIDTH / GRID_SIZE - 10

    SQUARE_WIDTH = BOARD_WIDTH / GRID_SIZE
    SQUARE_HEIGHT = BOARD_HEIGHT / GRID_SIZE

    FONT_SIZE = 25
    LETTER_MAPPING = {
        0: "a",
        1: "b",
        2: "c",
        3: "d",
        4: "e",
        5: "f",
        6: "g",
        7: "h",
    }
    hight_pieces_mapping = [
        "ROOK",
        "KNIGHT",
        "BISHOP",
        "QUEEN",
        "KING",
        "BISHOP",
        "KNIGHT",
        "ROOK",
    ]
    low_pieces_mapping = [
        "PAWN",
        "PAWN",
        "PAWN",
        "PAWN",
        "PAWN",
        "PAWN",
        "PAWN",
        "PAWN",
    ]


class RGBColors(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREY = (128, 128, 128)
    DARK_GREY = (96, 96, 96)
    LIGHT_BLUE = (140, 185, 189)
    DARK_YELLOW = (236, 177, 89)
    LIGHT_BROWN = (182, 115, 82)


class BLACK_PIECES(Enum):
    KING = "../assets/chess_pieces/black_king.png"
    QUEEN = "../assets/chess_pieces/black_queen.png"
    ROOK = "../assets/chess_pieces/black_rook.png"
    BISHOP = "../assets/chess_pieces/black_bishop.png"
    KNIGHT = "../assets/chess_pieces/black_knight.png"
    PAWN = "../assets/chess_pieces/black_pawn.png"


class WHITE_PIECES(Enum):
    KING = "../assets/chess_pieces/white_king.png"
    QUEEN = "../assets/chess_pieces/white_queen.png"
    ROOK = "../assets/chess_pieces/white_rook.png"
    BISHOP = "../assets/chess_pieces/white_bishop.png"
    KNIGHT = "../assets/chess_pieces/white_knight.png"
    PAWN = "../assets/chess_pieces/white_pawn.png"
