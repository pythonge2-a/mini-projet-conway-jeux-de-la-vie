## command pour faire le test: 
# Commande: pytest tests/tests_main.py

import pytest
from conway.game_of_life import GameOfLife
from conway.graphics import GameDisplay
from click.testing import CliRunner
from conway.__main__ import main

@pytest.mark.parametrize("frequency,born_min,born_max,survive_min,survive_max,expected", [
    (100, 3, 3, 2, 3, None),  # Valeurs valides
    (0, 3, 3, 2, 3, ValueError),  # Fréquence invalide
    (-1, 3, 3, 2, 3, ValueError),  # Fréquence négative
    (100, -1, 3, 2, 3, ValueError),  # born_min négatif
    (100, 3, 9, 2, 3, ValueError),  # born_max hors limite
    (100, 4, 3, 2, 3, ValueError),  # born_min > born_max
    (100, 3, 3, 4, 2, ValueError),  # survive_min > survive_max
])
def test_main_cli_options(frequency, born_min, born_max, survive_min, survive_max, expected):
    runner = CliRunner()
    args = [
        f"--frequency={frequency}",
        f"--born_min={born_min}",
        f"--born_max={born_max}",
        f"--survive_min={survive_min}",
        f"--survive_max={survive_max}"
    ]

    if expected is None:
        result = runner.invoke(main, args)
        assert result.exit_code == 0
    else:
        result = runner.invoke(main, args)
        assert result.exit_code != 0
        assert isinstance(result.exception, expected)

# Test specific logic for the game (example with toggle_cell)
def test_toggle_cell():
    rows, cols = 5, 5
    game = GameOfLife(rows, cols)
    
    assert game.grid[2][2] == 0  # Cell starts dead

    game.toggle_cell(2, 2)
    assert game.grid[2][2] == 1  # Cell toggled to alive

    game.toggle_cell(2, 2)
    assert game.grid[2][2] == 0  # Cell toggled back to dead
