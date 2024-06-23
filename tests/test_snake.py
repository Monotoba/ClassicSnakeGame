import pygame

from colors import COLORS
from src.snake import Snake

import pytest

class TestSnake:

    #  Snake initializes with default segments and direction
    def test_initialization(self):
        snake = Snake()
        assert snake.segments == [(100, 100), (80, 100), (60, 100)]
        assert snake.direction == pygame.K_RIGHT

    #  Snake moves correctly in the current direction
    def test_move(self):
        snake = Snake()
        initial_head = snake.segments[0]
        snake.move()
        new_head = snake.segments[0]
        assert new_head == (initial_head[0] + snake.cell_size, initial_head[1])

    #  Snake grows by the specified growth amount
    def test_grow(self):
        snake = Snake()
        initial_length = len(snake.segments)
        snake.grow(3)
        assert len(snake.segments) == initial_length + 3

    #  Snake changes direction when a valid key is pressed
    def test_change_direction(self):
        snake = Snake()
        snake.change_direction(pygame.K_DOWN)
        assert snake.direction == pygame.K_DOWN

    #  Snake draws itself on the given surface with correct colors
    def test_draw(self):
        pygame.init()
        screen = pygame.display.set_mode((200, 200))
        snake = Snake()
        snake.draw(screen)
        for i, segment in enumerate(snake.segments):
            seg_color_key = snake.colors[i % len(snake.colors)]
            seg_color = COLORS[seg_color_key]
            assert screen.get_at(segment)[:3] == seg_color

    #  Snake trims its length to the specified new length
    def test_trim_length(self):
        snake = Snake()
        snake.trim_length(2)
        assert len(snake.segments) == 2

    #  Snake does not change to an invalid direction
    def test_invalid_direction(self):
        snake = Snake()
        initial_direction = snake.direction
        snake.change_direction(pygame.K_SPACE)
        assert snake.direction == initial_direction

    #  Snake grows correctly when growth amount is zero
    def test_grow_zero(self):
        snake = Snake()
        initial_length = len(snake.segments)
        snake.grow(0)
        assert len(snake.segments) == initial_length

    #  Snake trims correctly when new length is greater than current length
    def test_trim_greater_length(self):
        snake = Snake()
        initial_length = len(snake.segments)
        snake.trim_length(initial_length + 2)
        assert len(snake.segments) == initial_length

    #  Snake handles rapid direction changes without errors
    def test_rapid_direction_changes(self):
        snake = Snake()
        directions = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
        for direction in directions:
            snake.change_direction(direction)
            snake.move()
            assert True  # If no exception is raised, the test passes

    #  Snake's segments do not overlap after moving
    def test_no_overlap_after_move(self):
        snake = Snake()
        snake.move()
        segments_set = set(snake.segments)
        assert len(segments_set) == len(snake.segments)
