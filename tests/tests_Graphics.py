## Commande pour effectuer les tests: pytest tests/tests_Graphics.py


import pytest
import pygame
from conway.game_of_life import GameOfLife
from conway.graphics import GameDisplay, COLOR_ANI, COLOR_BG, COLOR_DNI, COLOR_GRID

@pytest.fixture
def game_display():
    pygame.init()
    display = GameDisplay(200, 200, 20)  # 200x200 pixels, cellules de 20x20
    yield display
    pygame.quit()

def test_initialization(game_display):
    # Teste si l'objet GameDisplay est correctement initialisé
    assert game_display.width == 200
    assert game_display.height == 200
    assert game_display.cell_size == 20
    assert game_display.screen is not None

def test_draw_grid(game_display):
    # Mock pour tester draw_grid
    with pytest.MonkeyPatch().context() as monkeypatch:
        draw_line_calls = []

        def mock_draw_line(screen, color, start_pos, end_pos):
            draw_line_calls.append((color, start_pos, end_pos))

        monkeypatch.setattr(pygame.draw, "line", mock_draw_line)

        game_display.draw_grid()

        # Vérifie si les lignes horizontales et verticales ont été dessinées correctement
        assert len(draw_line_calls) == 20  # 10 horizontales + 10 verticales (200/20)
        for call in draw_line_calls:
            assert call[0] == COLOR_GRID  # La couleur des lignes doit correspondre

def test_draw_cells(game_display):
    # Mock pour tester draw_cells
    with pytest.MonkeyPatch().context() as monkeypatch:
        draw_rect_calls = []

        def mock_draw_rect(screen, color, rect):
            draw_rect_calls.append((color, rect))

        monkeypatch.setattr(pygame.draw, "rect", mock_draw_rect)

        cells = [(0, 0, 1), (1, 1, 0)]  # Une cellule vivante et une morte
        game_display.draw_cells(cells, running=False)

        # Vérifie si les couleurs et positions des cellules sont correctes
        assert len(draw_rect_calls) == 2
        assert draw_rect_calls[0][0] == COLOR_ANI  # Vivante (running=False)
        assert draw_rect_calls[1][0] == COLOR_BG  # Morte (running=False)

        # Teste avec `running=True`
        draw_rect_calls.clear()
        game_display.draw_cells(cells, running=True)
        assert draw_rect_calls[0][0] == COLOR_ANI  # Vivante (running=True)
        assert draw_rect_calls[1][0] == COLOR_DNI  # Morte (running=True)

def test_refresh(game_display):
    # Mock pour tester refresh
    with pytest.MonkeyPatch().context() as monkeypatch:
        flip_called = False

        def mock_flip():
            nonlocal flip_called
            flip_called = True

        monkeypatch.setattr(pygame.display, "flip", mock_flip)

        game_display.refresh()
        assert flip_called  # Vérifie si pygame.display.flip() est appelé