import pygame

COLOR_BG = (10, 10, 10)
COLOR_GRID = (40, 40, 40)
COLOR_DNI = (170, 170, 170)
COLOR_ANI = (255, 255, 255)

class GameDisplay:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill(COLOR_BG)

    def draw_grid(self):
        for row in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, COLOR_GRID, (0, row), (self.width, row))
        for col in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, COLOR_GRID, (col, 0), (col, self.height))

    def draw_cells(self, cells):
        for row, col, state in cells:
            color = COLOR_ANI if state == 1 else COLOR_DNI
            pygame.draw.rect(self.screen, color, (col * self.cell_size, row * self.cell_size, self.cell_size - 1, self.cell_size - 1))

    def refresh(self):
        pygame.display.flip()
