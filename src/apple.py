from random import random, randint
import pygame
from src.constants import *
from src.colors import COLORS


class Apple:
    def __init__(self, cell_size: int, color):
        self.cell_size = cell_size
        self.position = (randint(0, (SCREEN_WIDTH // self.cell_size) - 1) * self.cell_size,
                         randint(0, (SCREEN_HEIGHT // self.cell_size) - 1) * self.cell_size)
        self.color = color

    def respawn(self):
        self.position = (randint(0, (SCREEN_WIDTH // self.cell_size) - 1) * self.cell_size,
                         randint(0, (SCREEN_HEIGHT // self.cell_size) - 1) * self.cell_size)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], self.cell_size, self.cell_size))
