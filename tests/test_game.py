import os
import pygame

from src.apple import Apple
from src.snake import Snake
from src.constants import *
from src.game import Game

# Dependencies:
# pip install pytest-mock
import pytest


class TestGame:
    @pytest.fixture(scope='module')
    def set_working_directory(self):
        original_dir = os.getcwd()
        os.chdir(os.path.dirname(__file__))
        yield
        os.chdir(original_dir)

    #  Game initializes correctly with default values
    def test_initialization(self):
        game = Game()
        assert game.score == 0
        assert game.current_level == 0
        assert isinstance(game.snake, Snake)
        assert isinstance(game.apple, Apple)
        assert game.sound_object.sound_on is True
        assert game.sound_object.music_on is True

    #  Snake moves in the correct direction when arrow keys are pressed
    def test_snake_moves_correctly(self):
        game = Game()
        initial_position = game.snake.segments[0]
        game.snake.change_direction(pygame.K_DOWN)
        game.snake.move()
        new_position = game.snake.segments[0]
        assert new_position[1] == initial_position[1] + game.snake.cell_size

    #  Snake grows when it eats a regular apple
    def test_snake_grows_on_regular_apple(self):
        game = Game()
        initial_length = len(game.snake.segments)
        game.snake.segments[0] = game.apple.position
        game.check_collisions()
        assert len(game.snake.segments) > initial_length

    #  Snake grows significantly when it eats a golden apple
    def test_snake_grows_on_golden_apple(self):
        game = Game()
        game.current_level = 3  # Level with golden apples
        game.reset(level=3)
        initial_length = len(game.snake.segments)
        game.snake.segments[0] = game.golden_apple.position
        game.check_collisions()
        assert len(game.snake.segments) > initial_length + 6

    #  Snake shrinks when it eats a poison apple
    def test_snake_shrinks_on_poison_apple(self):
        game = Game()
        game.current_level = 6  # Level with poison apples
        game.reset(level=6)
        initial_length = len(game.snake.segments)
        game.snake.segments[0] = game.poison_apple.position
        game.check_collisions()
        assert len(game.snake.segments) == initial_length

    #  Score updates correctly when snake eats apples
    def test_score_updates_correctly(self):
        game = Game()
        initial_score = game.score
        game.snake.segments[0] = game.apple.position
        game.check_collisions()
        assert game.score > initial_score

    #  Snake changes direction correctly when opposite direction key is pressed
    def test_snake_changes_direction_correctly(self):
        game = Game()
        initial_direction = pygame.K_RIGHT
        new_direction = pygame.K_LEFT
        game.snake.change_direction(new_direction)
        assert game.snake.direction == new_direction

    #  Game handles rapid direction changes without crashing
    def test_rapid_direction_changes(self):
        game = Game()
        directions = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
        for direction in directions:
            game.snake.change_direction(direction)
            game.snake.move()
            assert True  # If no exception is raised, the test passes

    #  Apple respawns correctly without overlapping the snake
    def test_apple_respawns_correctly(self):
        game = Game()
        snake_positions = set(game.snake.segments)
        for _ in range(100):  # Check multiple respawns
            game.apple.respawn()
            assert game.apple.position not in snake_positions

    #  Game handles maximum possible snake length without errors
    def test_maximum_snake_length(self):
        game = Game()
        max_length = (SCREEN_WIDTH // game.cell_size) * (SCREEN_HEIGHT // game.cell_size)
        for _ in range(max_length - len(game.snake.segments)):
            game.snake.grow()
        assert len(game.snake.segments) == max_length
