from ..constants import Config
from ..figure import Figure


def highlight_attack(
    mouse_x: float, mouse_y: float, figure: Figure, board_interaction
) -> None:
    # down attack move calculation
    for i in range(Config.GRID_SIZE):
        square_obj = board_interaction.get_obj_by_coordinates(
            obj_list=board_interaction.squares,
            mouse_x=mouse_x,
            mouse_y=mouse_y + (Config.SQUARE_HEIGHT * i + Config.SQUARE_HEIGHT),
        )
        figure_obj = board_interaction.get_obj_by_coordinates(
            obj_list=board_interaction.figures,
            mouse_x=mouse_x,
            mouse_y=mouse_y + (Config.SQUARE_HEIGHT * i + Config.SQUARE_HEIGHT),
        )

        if square_obj is not None and figure_obj is not None:
            if figure_obj.color != figure.color:
                square_obj.selected = True
                break

    # up attack move calculation
    for i in range(Config.GRID_SIZE):
        square_obj = board_interaction.get_obj_by_coordinates(
            obj_list=board_interaction.squares,
            mouse_x=mouse_x,
            mouse_y=mouse_y - (Config.SQUARE_HEIGHT * i + Config.SQUARE_HEIGHT),
        )
        figure_obj = board_interaction.get_obj_by_coordinates(
            obj_list=board_interaction.figures,
            mouse_x=mouse_x,
            mouse_y=mouse_y - (Config.SQUARE_HEIGHT * i + Config.SQUARE_HEIGHT),
        )

        if square_obj is not None and figure_obj is not None:
            if figure_obj.color != figure.color:
                square_obj.selected = True
                break

    # left attack move calculation
    for i in range(Config.GRID_SIZE):
        square_obj = board_interaction.get_obj_by_coordinates(
            obj_list=board_interaction.squares,
            mouse_x=mouse_x - (Config.SQUARE_HEIGHT * i + Config.SQUARE_HEIGHT),
            mouse_y=mouse_y,
        )
        figure_obj = board_interaction.get_obj_by_coordinates(
            obj_list=board_interaction.figures,
            mouse_x=mouse_x - (Config.SQUARE_HEIGHT * i + Config.SQUARE_HEIGHT),
            mouse_y=mouse_y,
        )

        if square_obj is not None and figure_obj is not None:
            if figure_obj.color != figure.color:
                square_obj.selected = True
                break

    # right attack move calculation
    for i in range(Config.GRID_SIZE):
        square_obj = board_interaction.get_obj_by_coordinates(
            obj_list=board_interaction.squares,
            mouse_x=mouse_x + (Config.SQUARE_HEIGHT * i + Config.SQUARE_HEIGHT),
            mouse_y=mouse_y,
        )
        figure_obj = board_interaction.get_obj_by_coordinates(
            obj_list=board_interaction.figures,
            mouse_x=mouse_x + (Config.SQUARE_HEIGHT * i + Config.SQUARE_HEIGHT),
            mouse_y=mouse_y,
        )

        if square_obj is not None and figure_obj is not None:
            if figure_obj.color != figure.color:
                square_obj.selected = True
                break


def highlight_move(
    mouse_x: float, mouse_y: float, figure: Figure, board_interaction
) -> None:
    for i in range(Config.GRID_SIZE):
        # down moves
        square_obj = board_interaction.get_obj_by_coordinates(
            obj_list=board_interaction.squares,
            mouse_x=mouse_x,
            mouse_y=mouse_y + (Config.SQUARE_HEIGHT * i),
        )

        figure_obj = board_interaction.get_obj_by_coordinates(
            obj_list=board_interaction.figures,
            mouse_x=mouse_x,
            mouse_y=mouse_y + (Config.SQUARE_HEIGHT * i),
        )
        if square_obj is not None:
            if figure_obj is None:
                square_obj.selected = True

        # up moves
        square_obj = board_interaction.get_obj_by_coordinates(
            obj_list=board_interaction.squares,
            mouse_x=mouse_x,
            mouse_y=mouse_y - (Config.SQUARE_HEIGHT * i),
        )

        figure_obj = board_interaction.get_obj_by_coordinates(
            obj_list=board_interaction.figures,
            mouse_x=mouse_x,
            mouse_y=mouse_y - (Config.SQUARE_HEIGHT * i),
        )
        if square_obj is not None:
            if figure_obj is None:
                square_obj.selected = True

        # left moves
        square_obj = board_interaction.get_obj_by_coordinates(
            obj_list=board_interaction.squares,
            mouse_x=mouse_x - (Config.SQUARE_HEIGHT * i),
            mouse_y=mouse_y,
        )

        figure_obj = board_interaction.get_obj_by_coordinates(
            obj_list=board_interaction.figures,
            mouse_x=mouse_x - (Config.SQUARE_HEIGHT * i),
            mouse_y=mouse_y,
        )
        if square_obj is not None:
            if figure_obj is None:
                square_obj.selected = True

        # right up
        square_obj = board_interaction.get_obj_by_coordinates(
            obj_list=board_interaction.squares,
            mouse_x=mouse_x + (Config.SQUARE_HEIGHT * i),
            mouse_y=mouse_y,
        )

        figure_obj = board_interaction.get_obj_by_coordinates(
            obj_list=board_interaction.figures,
            mouse_x=mouse_x + (Config.SQUARE_HEIGHT * i),
            mouse_y=mouse_y,
        )
        if square_obj is not None:
            if figure_obj is None:
                square_obj.selected = True
