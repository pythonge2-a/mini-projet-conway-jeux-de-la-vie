import numpy as np

class GameOfLife:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = np.zeros((rows, cols))

    def update(self, with_progress=False):
        updated_grid = np.zeros((self.rows, self.cols))
        for row in range(self.rows):
            for col in range(self.cols):
                alive = np.sum(self.grid[row-1:row+2, col-1:col+2]) - self.grid[row, col]

                if self.grid[row, col] == 1:
                    if alive < 2 or alive > 3:
                        if with_progress:
                            yield (row, col, 0)
                    elif 2 <= alive <= 3:
                        updated_grid[row, col] = 1
                        if with_progress:
                            yield (row, col, 1)
                else:
                    if alive == 3:
                        updated_grid[row, col] = 1
                        if with_progress:
                            yield (row, col, 1)

        self.grid = updated_grid

    def toggle_cell(self, row, col):
        self.grid[row, col] = 1 if self.grid[row, col] == 0 else 0

    def reset(self):
        self.grid = np.zeros((self.rows, self.cols))
