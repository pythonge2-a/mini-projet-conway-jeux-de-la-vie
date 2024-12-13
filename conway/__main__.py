import pygame
import time
import numpy as np
import click
from game_of_life import GameOfLife
from graphics import GameDisplay, COLOR_BG

@click.command()
@click.option("-f", "--frequency", default=100, type=float, help="fréquence de rafraîchissement du jeu en Hz")
@click.option("-b", "--born_min", default=3, type=int, help="Nombre minimum de voisins pour qu'une cellule naisse")
@click.option("-d", "--born_max", default=3, type=int, help="Nombre maximum de voisins pour qu'une cellule naisse")
@click.option("-s", "--survive_min", default=2, type=int, help="Nombre minimum de voisins pour qu'une cellule survive")
@click.option("-m", "--survive_max", default=3, type=int, help="Nombre maximum de voisins pour qu'une cellule survive")

def main(frequency, born_min, born_max, survive_min, survive_max):
    if frequency <= 0:
        raise ValueError("La fréquence doit être superieur à 0.")
    if born_min < 0 or born_max < 0 or survive_min < 0 or survive_max < 0:
        raise ValueError("Les condition de naissance et de survie doivent être superieur ou égale à 0.")
    if born_min > 8 or born_max > 8 or survive_min > 8 or survive_max > 8:
        raise ValueError("Les condition de naissance et de survie doivent être inférieur ou égale à 8.")
    if born_min > born_max or survive_min > survive_max:
        raise ValueError("Les condition de naissance et de survie minimales doivent être inférieur ou égale aux condition maximales.")
    
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
            cells = list(game.update(with_progress=True, born_min=born_min, born_max=born_max, survive_min=survive_min, survive_max=survive_max))
        else:
            cells = [(row, col, state) for (row, col), state in np.ndenumerate(game.grid)]


        display.draw_cells(cells, running)
        display.draw_grid()
        display.refresh()

        if running:
            time.sleep(1/frequency)

if __name__ == '__main__':
    main()
