import numpy as np

class GameOfLife:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = np.zeros((rows, cols))

    def update(self, with_progress=False, born_min=3, born_max=3, survive_min=2, survive_max=3):
        updated_grid = np.zeros((self.rows, self.cols))
        for row in range(self.rows):
            for col in range(self.cols):
                alive = np.sum(self.grid[row-1:row+2, col-1:col+2]) - self.grid[row, col]

                if self.grid[row, col] == 1:
                    if alive < survive_min or alive > survive_max:
                        if with_progress:
                            yield (row, col, 0)
                    else:
                        updated_grid[row, col] = 1
                        if with_progress:
                            yield (row, col, 1)
                else:
                    if alive >= born_min and alive <= born_max:
                        updated_grid[row, col] = 1
                        if with_progress:
                            yield (row, col, 1)

        self.grid = updated_grid

    def toggle_cell(self, row, col):
        if row < 0 or row >= self.rows:
            row = 0 if row <= 0 else self.rows-1
        if col < 0 or col >= self.cols:
            col = 0 if col <= 0 else self.cols-1
        self.grid[row, col] = 1 if self.grid[row, col] == 0 else 0

    def add_pattern(self, pattern, x_offset, y_offset):
        pattern_rows = len(pattern)
        pattern_cols = len(pattern[0])

        for row in range(pattern_rows):
            for col in range(pattern_cols):
                x = x_offset + row
                y = y_offset + col
                if 0 <= x < self.rows and 0 <= y < self.cols:
                    self.grid[x, y] = pattern[row][col]

    def add_spaceship(self, spaceship):
        
        x_offset = self.rows // 2 - len(spaceship) // 2
        y_offset = self.cols // 2 - len(spaceship[0]) // 2
        self.add_pattern(spaceship, x_offset, y_offset)

    def reset(self):
        self.grid = np.zeros((self.rows, self.cols))
