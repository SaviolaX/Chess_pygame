import pygame

from src.board import define_squares_position, BoardRenderer, BoardInteraction
from src.figure import define_figures_position
from src.constants import RGBColors


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1070, 760))
# window title
pygame.display.set_caption("Chess")

# background color
# DARK_GREY = (96, 96, 96)
screen.fill(RGBColors.LIGHT_BROWN.value)


squares_list = define_squares_position()
figures_list = define_figures_position(squares_list)


board_renderer = BoardRenderer(
    screen=screen, squares=squares_list, figures=figures_list
)
board_interaction = BoardInteraction(squares=squares_list, figures=figures_list)


captured_figures = []


class ChessGame:
    running = True
    clock = pygame.time.Clock()

    def run(self) -> None:
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # left click
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    figure_obj = board_interaction.get_obj_by_coordinates(
                        obj_list=board_interaction.figures,
                        mouse_x=mouse_x,
                        mouse_y=mouse_y,
                    )

                    selected_figure = board_interaction.select_figure(figure_obj)

                    board_interaction.highlight_figure_move(
                        mouse_x, mouse_y, selected_figure
                    )

                # right click
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    # get square
                    square_obj = board_interaction.get_obj_by_coordinates(
                        squares_list, mouse_x, mouse_y
                    )
                    # get figure
                    figure_obj = board_interaction.get_obj_by_coordinates(
                        figures_list, mouse_x, mouse_y
                    )

                    selected_figures = [
                        x for x in board_interaction.figures if x.selected is True
                    ]

                    if len(selected_figures) != 0:
                        selected_figure = selected_figures[0]

                        # capture figure
                        if figure_obj is not None:
                            if selected_figure.color != figure_obj.color:
                                captured_figures.append(figure_obj)
                                board_renderer.figures.remove(figure_obj)
                                board_interaction.move_figure(
                                    selected_figure, square_obj
                                )

                        # move figure
                        board_interaction.move_figure(selected_figure, square_obj)

                    print(f"Captured figures: {len(captured_figures)}")

            board_renderer.draw()
            board_renderer.draw_figures()

            pygame.display.flip()

            self.clock.tick(60)  # limits FPS to 60

        pygame.quit()


if __name__ == "__main__":
    game = ChessGame()
    game.run()
