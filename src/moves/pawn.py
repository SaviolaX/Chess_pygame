from ..constants import Config
from ..figure import Figure


def highlight_attack(
    mouse_x: float, mouse_y: float, figure: Figure, board_interaction
) -> None:
    if figure.color == "black":
        left_diagonal_square = board_interaction.get_obj_by_coordinates(
            obj_list=board_interaction.squares,
            mouse_x=mouse_x - Config.SQUARE_WIDTH,
            mouse_y=mouse_y - Config.SQUARE_HEIGHT,
        )

        left_diagonal_figure = board_interaction.get_obj_by_coordinates(
            obj_list=board_interaction.figures,
            mouse_x=mouse_x - Config.SQUARE_WIDTH,
            mouse_y=mouse_y - Config.SQUARE_HEIGHT,
        )

        if left_diagonal_figure is not None:
            if left_diagonal_figure.color != figure.color:
                left_diagonal_square.selected = True

        right_diagonal_square = board_interaction.get_obj_by_coordinates(
            obj_list=board_interaction.squares,
            mouse_x=mouse_x + Config.SQUARE_WIDTH,
            mouse_y=mouse_y - Config.SQUARE_HEIGHT,
        )

        right_diagonal_figure = board_interaction.get_obj_by_coordinates(
            obj_list=board_interaction.figures,
            mouse_x=mouse_x + Config.SQUARE_WIDTH,
            mouse_y=mouse_y - Config.SQUARE_HEIGHT,
        )

        if right_diagonal_figure is not None:
            if right_diagonal_figure.color != figure.color:
                right_diagonal_square.selected = True

    if figure.color == "white":
        left_diagonal_square = board_interaction.get_obj_by_coordinates(
            obj_list=board_interaction.squares,
            mouse_x=mouse_x - Config.SQUARE_WIDTH,
            mouse_y=mouse_y + Config.SQUARE_HEIGHT,
        )

        left_diagonal_figure = board_interaction.get_obj_by_coordinates(
            obj_list=board_interaction.figures,
            mouse_x=mouse_x - Config.SQUARE_WIDTH,
            mouse_y=mouse_y + Config.SQUARE_HEIGHT,
        )

        if left_diagonal_figure is not None:
            if left_diagonal_figure.color != figure.color:
                left_diagonal_square.selected = True

        right_diagonal_square = board_interaction.get_obj_by_coordinates(
            obj_list=board_interaction.squares,
            mouse_x=mouse_x + Config.SQUARE_WIDTH,
            mouse_y=mouse_y + Config.SQUARE_HEIGHT,
        )

        right_diagonal_figure = board_interaction.get_obj_by_coordinates(
            obj_list=board_interaction.figures,
            mouse_x=mouse_x + Config.SQUARE_WIDTH,
            mouse_y=mouse_y + Config.SQUARE_HEIGHT,
        )

        if right_diagonal_figure is not None:
            if right_diagonal_figure.color != figure.color:
                right_diagonal_square.selected = True


def highlight_move(
    mouse_x: float, mouse_y: float, figure: Figure, board_interaction
) -> None:
    if figure.moved is False:
        pawn_moves = [Config.SQUARE_HEIGHT, (Config.SQUARE_HEIGHT * 2)]
    else:
        pawn_moves = [
            Config.SQUARE_HEIGHT,
        ]

    if figure.color == "black":
        for move in pawn_moves:
            square_obj = board_interaction.get_obj_by_coordinates(
                obj_list=board_interaction.squares,
                mouse_x=mouse_x,
                mouse_y=mouse_y - move,  # go up
            )

            figure_obj = board_interaction.get_obj_by_coordinates(
                obj_list=board_interaction.figures,
                mouse_x=mouse_x,
                mouse_y=mouse_y - move,
            )

            if figure_obj is None:
                square_obj.selected = True

    if figure.color == "white":
        for move in pawn_moves:
            square_obj = board_interaction.get_obj_by_coordinates(
                obj_list=board_interaction.squares,
                mouse_x=mouse_x,
                mouse_y=mouse_y + move,  # go down
            )

            figure_obj = board_interaction.get_obj_by_coordinates(
                obj_list=board_interaction.figures,
                mouse_x=mouse_x,
                mouse_y=mouse_y + move,
            )

            if figure_obj is None:
                square_obj.selected = True
