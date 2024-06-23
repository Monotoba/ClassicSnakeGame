#! /usr/bin/python3

import pygame
from src.constants import *
from src.colors import COLORS


class Snake:
    def __init__(self, cell_size=10):
        self.cell_size = cell_size
        self.segments = [(100, 100), (80, 100), (60, 100)]  # Initial segments of the snake
        self.direction = pygame.K_RIGHT  # Initial direction
        self.colors = ['YELLOW', 'BROWN', 'GREEN']

    def move(self):
        head_x, head_y = self.segments[0]

        if self.direction == pygame.K_UP:
            head_y -= self.cell_size
        elif self.direction == pygame.K_DOWN:
            head_y += self.cell_size
        elif self.direction == pygame.K_LEFT:
            head_x -= self.cell_size
        elif self.direction == pygame.K_RIGHT:
            head_x += self.cell_size

        new_head = (head_x, head_y)
        self.segments = [new_head] + self.segments[:-1]

    def grow(self, growth=1):
        while growth > 0:
            self.segments.append(self.segments[-1])
            growth -= 1

    def trim_length(self, new_length: int = 5):
        self.segments = self.segments[:new_length]

    def change_direction(self, direction):
        if direction in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
            self.direction = direction

    def draw(self, surface):
        for i, segment in enumerate(self.segments):
            seg_color_key = self.colors[i % len(self.colors)]
            seg_color = COLORS[seg_color_key]
            pygame.draw.rect(surface, seg_color, (segment[0], segment[1], self.cell_size, self.cell_size))
