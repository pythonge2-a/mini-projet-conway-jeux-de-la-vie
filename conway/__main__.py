import pygame
import time
import numpy as np
from game_of_life import GameOfLife
from graphics import GameDisplay, COLOR_BG
from interface import Button, Slider


SPACESHIPL = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1]
]

SPACESHIPM = [
    [0, 1, 1, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 1, 1, 0]
]

SPACESHIPB = [
    [0, 0, 0, 1, 1, 0],
    [1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0]
]

FACTORYA = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
def main():
    
    pygame.init()

    # Configurations
    width, height = 1200, 800
    cell_size = 10
    rows, cols = height // cell_size, width // cell_size

    GRID_MASK = pygame.Rect(0, 0, 220, height)
    
    # Initialisation jeu et affichage
    game = GameOfLife(rows, cols)
    display = GameDisplay(width, height, cell_size)

    font = pygame.font.Font(None, 24)

    reset_button = Button(
        x=10, y=10, width=120, height=40,
        text="Reset",
        font=font,
        color=(200, 50, 50),
        text_color=(255, 255, 255),
        action=game.reset
    )

    spaceshipl_button = Button(
        x=10, y=330, width=160, height=40,
        text="Small spaceship",
        font=font,
        color=(50, 50, 200),
        text_color=(255, 255, 255),
        action=lambda: game.add_spaceship(SPACESHIPL)
    )

    spaceshipm_button = Button(
        x=10, y=380, width=160, height=40,
        text="Medium spaceship",
        font=font,
        color=(0, 128, 0),
        text_color=(255, 255, 255),
        action=lambda: game.add_spaceship(SPACESHIPM)
    )

    spaceshipb_button = Button(
        x=10, y=430, width=160, height=40,
        text="Big spaceship",
        font=font,
        color=(255, 128, 0),
        text_color=(255, 255, 255),
        action=lambda: game.add_spaceship(SPACESHIPB)
    )

    factorya_button = Button(
        x=10, y=480, width=160, height=40,
        text="Small ship factory",
        font=font,
        color=(128, 0, 128),
        text_color=(255, 255, 255),
        action=lambda: game.add_spaceship(FACTORYA)
    )

    buttons = [reset_button, spaceshipl_button, spaceshipm_button, spaceshipb_button, factorya_button]

    # Créer les sliders
    sliders = [
        Slider(x=10, y=90, width=200, min_val=10, max_val=500, start_val=100, label="Frequency (Hz)", font=font),
        Slider(x=10, y=140, width=200, min_val=0, max_val=8, start_val=3, label="Born Min", font=font),
        Slider(x=10, y=190, width=200, min_val=0, max_val=8, start_val=3, label="Born Max", font=font),
        Slider(x=10, y=240, width=200, min_val=0, max_val=8, start_val=2, label="Survive Min", font=font),
        Slider(x=10, y=290, width=200, min_val=0, max_val=8, start_val=3, label="Survive Max", font=font)
    ]

    # Fond en couleur des sliders + boutons
    bg_zone_x = 0
    bg_zone_y = 0
    bg_zone_width = 220
    bg_zone_height = 800
    bg_zone_color = (47, 79, 79)

    # Variables initiales
    frequency = sliders[0].get_value()
    born_min = sliders[1].get_value()
    born_max = sliders[2].get_value()
    survive_min = sliders[3].get_value()
    survive_max = sliders[4].get_value()

    running = False

    # Boucle principale
    while True:
        display.screen.fill(COLOR_BG)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running = not running

            for button in buttons:
                button.handle_event(event)

            for slider in sliders:
                slider.handle_event(event)

            # Gestion du mask
            if GRID_MASK.collidepoint(pygame.mouse.get_pos()):
                if event.type in [pygame.MOUSEBUTTONDOWN, pygame.MOUSEMOTION]:
                    for slider in sliders:
                        # Interaction sur les sliders autorisé
                        if slider.contains_point(event.pos):
                            break  
                    else:
                        # Interaction sur zone 
                        continue
                continue

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                # Evite le spawn des cellules vivantes lorsqu'on sort de la fenêtre
                if 0 <= pos[0] < width and 0 <= pos[1] < height:
                    for slider in sliders:
                        # Excepter les clicks sur les sliders
                        if not slider.contains_point(pos): 
                            game.toggle_cell(pos[1] // cell_size, pos[0] // cell_size)

        # Valeurs initiales des sliders
        frequency = sliders[0].get_value()
        born_min = sliders[1].get_value()
        born_max = sliders[2].get_value()
        survive_min = sliders[3].get_value()
        survive_max = sliders[4].get_value()

        if born_min > born_max:
            born_min = born_max
            sliders[1].value = born_min
            sliders[1].handle_x = sliders[1].get_handle_pos()
        if survive_min > survive_max:
            survive_min = survive_max
            sliders[3].value = survive_min
            sliders[3].handle_x = sliders[3].get_handle_pos()

        if running:
            cells = list(game.update(with_progress=True, born_min=born_min, born_max=born_max, survive_min=survive_min, survive_max=survive_max))
        else:
            cells = [(row, col, state) for (row, col), state in np.ndenumerate(game.grid)]

        display.draw_cells(cells, running)
        display.draw_grid()
        pygame.draw.rect(display.screen, bg_zone_color, (bg_zone_x, bg_zone_y, bg_zone_width, bg_zone_height))


        # Dessiner les boutons
        for button in buttons:
            button.draw(display.screen)

        # Dessiner les sliders
        for slider in sliders:
            slider.draw(display.screen)

        display.refresh()


        if running:
            time.sleep(1/frequency)

if __name__ == '__main__':
    main()
