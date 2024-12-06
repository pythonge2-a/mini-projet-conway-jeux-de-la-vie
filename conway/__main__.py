import pygame
import time
import numpy as np
import click
from game_of_life import GameOfLife
from graphics import GameDisplay, COLOR_BG

@click.command()
@click.option("-f", "--frequency", default=100, type=float, help="fréquence de rafraîchissement du jeu en Hz")


def main(frequency):
    if frequency <= 0:
        raise ValueError("La fréquence doit être superieur à 0.")
    
    pygame.init()

    # Configurations
    width, height = 800, 600
    cell_size = 10
    rows, cols = height // cell_size, width // cell_size

    # Initialize game and display
    game = GameOfLife(rows, cols)
    display = GameDisplay(width, height, cell_size)

    running = False
    while True:
        display.screen.fill(COLOR_BG)
        display.draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                elif event.key == pygame.K_n:
                    game.reset()
                    running = False

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                game.toggle_cell(pos[1] // cell_size, pos[0] // cell_size)

        if running:
            cells = list(game.update(with_progress=True))
        else:
            cells = [(row, col, state) for (row, col), state in np.ndenumerate(game.grid)]


        display.draw_cells(cells)
        display.refresh()

        if running:
            time.sleep(1/frequency)

if __name__ == '__main__':
    main()
