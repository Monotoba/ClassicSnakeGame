from random import randrange

import pygame
from src.snake import Snake
from src.apple import Apple
from src.constants import *
from src.colors import COLORS
from src.level import Level, LEVELS
from src.screens import NextLevelScreen, StartScreen, LoseScreen, ExitScreen, WinGameScreen
from src.sound import Sound


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Mark's Classic Snake Game")
        pygame.font.init()
        self.score: int = 0
        self.levels: list[Level] = LEVELS
        self.current_level = 0  # Is always level number - 1. Because levels list is zero index.
        self.cell_size = self.levels[self.current_level].cell_size   # Get cell size from level
        self.snake: Snake = Snake(cell_size=self.cell_size)
        self.apple: Apple = Apple(cell_size=self.cell_size, color=COLORS['RED'])
        self.golden_apple = None
        self.poison_apple = None
        self.sound_object = Sound()
        self.clock = pygame.time.Clock()
        self.reset()
        self.sound_object.sound_on = True
        self.sound_object.music_on = True
        self.sound_object.play_background_music()


    def run(self):
        start_screen = StartScreen(screen=self.screen, colors=COLORS, sound_object=self.sound_object)
        game_over = start_screen.show()
        if game_over:
            self.exit()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                        self.snake.change_direction(event.key)
                    elif event.key == pygame.K_q:
                        running = True
                    elif event.key == pygame.K_m:
                        if self.sound_object is not None:
                            self.sound_object.music_on = not self.sound_object.music_on
                    elif event.key == pygame.K_s:
                        if self.sound_object is not None:
                            self.sound_object.sound_on = not self.sound_object.sound_on

            self.snake.move()
            self.check_collisions()
            self.check_level_completion()
            self.draw()
            self.clock.tick(self.levels[self.current_level].speed)  # Control the frame rate

        pygame.quit()

    def reset(self, level: int = 0):
        self.snake = Snake(cell_size=self.levels[self.current_level].cell_size)
        self.apple = Apple(cell_size=self.cell_size, color=COLORS['RED'])
        self.current_level = level
        if self.levels[self.current_level].golden_apples:
            self.golden_apple = Apple(cell_size=self.cell_size, color=COLORS['GOLDEN'])
        if self.levels[self.current_level].poison_apples:
            self.poison_apple = Apple(cell_size=self.cell_size, color=COLORS['ROTTEN_GRN'])


    def check_collisions(self):
        # Check for collision with apple
        if self.snake.segments[0] == self.apple.position:
            self.snake.grow(growth=randrange(1, 5))
            self.apple.respawn()
            self.score = len(self.snake.segments) * 10

        # Did player eat golden apple?
        if self.levels[self.current_level].golden_apples and self.snake.segments[0] == self.golden_apple.position:
            self.sound_object.play_win_sound()
            self.snake.grow(growth=randrange(7, 15))
            self.golden_apple.respawn()
            self.score = len(self.snake.segments) * 15

        # Did player eat poison apple?
        # If so, shrink snake length, and reset score
        if self.levels[self.current_level].poison_apples and self.snake.segments[0] == self.poison_apple.position:
            self.sound_object.play_lose_sound()
            self.snake.trim_length(new_length=randrange(3, 7))
            self.poison_apple.respawn()
            self.score = len(self.snake.segments) * 10

        # Check for collision with walls
        head_x, head_y = self.snake.segments[0]
        if head_x < 0 or head_x >= SCREEN_WIDTH or head_y < 0 or head_y >= SCREEN_HEIGHT:
            self.game_over()

        # Check for collision with itself
        for pos in self.snake.segments[1:]:
            if head_x == pos[0] and head_y == pos[1]:
                self.game_over()

    def check_level_completion(self):
        if len(self.snake.segments) >= self.levels[self.current_level].target_length:
            if self.current_level >= len(self.levels):
                self.game_won()
            else:
                level_screen = NextLevelScreen(screen=self.screen, colors=COLORS, sound_object=self.sound_object, level=self.current_level)
                game_over = level_screen.show()
                if game_over:
                    self.exit()
                else:
                    self.current_level += 1
                    self.reset(self.current_level)

    def exit(self):
        exit_screen = ExitScreen(screen=self.screen, colors=COLORS, sound_object=self.sound_object)
        exit_screen.show()
        pygame.quit()
        exit(0)

    def game_won(self):
        self.sound_object.play_win_sound()
        win_screen = WinGameScreen(screen=self.screen, colors=COLORS, sound_object=self.sound_object)
        game_over = win_screen.show()
        if game_over:
            self.exit()
        else:
            self.current_level = 0
            self.score = 0
            self.reset()

    def game_over(self):
        self.sound_object.play_lose_sound()
        loose_screen = LoseScreen(screen=self.screen, colors=COLORS, sound_object=self.sound_object)
        game_over = loose_screen.show()
        if game_over:
            self.exit()
        else:
            self.reset()


    def draw(self):
        self.screen.fill(COLORS['BLACK'])
        self.snake.draw(self.screen)
        self.apple.draw(self.screen)
        if self.levels[self.current_level].golden_apples:
            self.golden_apple.draw(self.screen)
        if self.levels[self.current_level].poison_apples:
            self.poison_apple.draw(self.screen)
        self.draw_level_info()
        pygame.display.flip()

    def draw_level_info(self):
        font = pygame.font.SysFont(None, 30)
        level_text = font.render(f"Level: {self.levels[self.current_level].level_number}", True, COLORS['WHITE'])
        self.screen.blit(level_text, (10, 10))
        score_text = font.render(f"Score: {self.score}", True, COLORS['WHITE'])
        self.screen.blit(score_text, (10, 50))



if __name__ == "__main__":
    # Initialize Pygame
    pygame.init()
    # Set up the display
    # screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # pygame.display.set_caption("Mark's Classic Snake Game")

    # Run the game
    game = Game()
    game.run()
