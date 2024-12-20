## command pour faire le test: 
# Commande: pytest tests/GameOfLife.py

import pytest
from conway.game_of_life import GameOfLife
from conway.graphics import GameDisplay
import numpy as np

@pytest.fixture
def game():
    return GameOfLife(5, 5)

def test_initial_grid(game):
    # Vérifie que la grille est initialisée avec des zéros
    assert np.array_equal(game.grid, np.zeros((5, 5)))

def test_toggle_cell(game):
    # Teste le basculement d'une cellule
    game.toggle_cell(2, 2)
    assert game.grid[2, 2] == 1
    game.toggle_cell(2, 2)
    assert game.grid[2, 2] == 0

def test_toggle_cell_out_of_bounds(game):
    # Teste le basculement des cellules en dehors des limites
    game.toggle_cell(-1, -1)
    assert game.grid[0, 0] == 1
    game.toggle_cell(5, 5)
    assert game.grid[4, 4] == 1

def test_reset_grid(game):
    # Teste la réinitialisation de la grille
    game.toggle_cell(2, 2)
    game.reset()
    assert np.array_equal(game.grid, np.zeros((5, 5)))

def test_update_no_change(game):
    # Teste une mise à jour où rien ne change (grille vide)
    initial_grid = game.grid.copy()
    game.update()
    assert np.array_equal(game.grid, initial_grid)


def test_update_survival(game):
    # Teste la survie d'une cellule
    game.toggle_cell(1, 1)
    game.toggle_cell(1, 2)
    game.toggle_cell(2, 1)
    game.toggle_cell(2, 2)
    game.update()
    assert game.grid[1, 1] == 1
    assert game.grid[2, 2] == 1

def test_update_with_progress(game):
    # Teste la mise à jour avec l'option `with_progress`
    game.toggle_cell(1, 1)
    game.toggle_cell(1, 2)
    game.toggle_cell(2, 1)
    progress = list(game.update(with_progress=True))
    assert len(progress) > 0
    assert all(len(step) == 3 for step in progress)  # Chaque étape contient (row, col, state)
