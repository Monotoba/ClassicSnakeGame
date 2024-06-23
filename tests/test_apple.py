import pygame

from src.constants import *
from src.apple import Apple

import pytest

class TestApple:

    #  Apple initializes with correct position within screen bounds
    def test_initial_position_within_bounds(self):
        apple = Apple(cell_size=20, color=(255, 0, 0))
        assert 0 <= apple.position[0] < SCREEN_WIDTH
        assert 0 <= apple.position[1] < SCREEN_HEIGHT

    #  Apple respawns to a new valid position within screen bounds
    def test_respawn_position_within_bounds(self):
        apple = Apple(cell_size=20, color=(255, 0, 0))
        apple.respawn()
        assert 0 <= apple.position[0] < SCREEN_WIDTH
        assert 0 <= apple.position[1] < SCREEN_HEIGHT

    #  Apple draws correctly on the given surface
    def test_draw_apple(self):
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        apple = Apple(cell_size=20, color=(255, 0, 0))
        apple.draw(screen)
        pygame.quit()

    #  Apple initializes with the correct color
    def test_initial_color(self):
        color = (255, 0, 0)
        apple = Apple(cell_size=20, color=color)
        assert apple.color == color

    #  Apple position is at the edge of the screen
    def test_position_at_screen_edge(self):
        apple = Apple(cell_size=20, color=(255, 0, 0))
        assert apple.position[0] % apple.cell_size == 0
        assert apple.position[1] % apple.cell_size == 0

    #  Apple respawns at the same position consecutively
    def test_respawn_same_position_consecutively(self):
        apple = Apple(cell_size=20, color=(255, 0, 0))
        initial_position = apple.position
        apple.respawn()
        assert initial_position != apple.position

    #  Apple respawns when screen dimensions are not divisible by cell size
    def test_respawn_non_divisible_screen_dimensions(self):
        global SCREEN_WIDTH, SCREEN_HEIGHT
        SCREEN_WIDTH, SCREEN_HEIGHT = 805, 605
        apple = Apple(cell_size=20, color=(255, 0, 0))
        for _ in range(100):
            apple.respawn()
            assert 0 <= apple.position[0] < SCREEN_WIDTH
            assert 0 <= apple.position[1] < SCREEN_HEIGHT

    #  Apple position remains consistent between draws if not respawned
    def test_position_consistency_between_draws(self):
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        apple = Apple(cell_size=20, color=(255, 0, 0))
        initial_position = apple.position
        apple.draw(screen)
        assert initial_position == apple.position
        pygame.quit()

    #  Apple handles large screen sizes correctly
    def test_large_screen_sizes(self):
        global SCREEN_WIDTH, SCREEN_HEIGHT
        SCREEN_WIDTH, SCREEN_HEIGHT = 5000, 3000
        apple = Apple(cell_size=20, color=(255, 0, 0))
        for _ in range(100):
            apple.respawn()
            assert 0 <= apple.position[0] < SCREEN_WIDTH
            assert 0 <= apple.position[1] < SCREEN_HEIGHT
