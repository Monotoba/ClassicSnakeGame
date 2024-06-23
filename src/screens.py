import pygame
from src.constants import *
from src.colors import COLORS


class LoseScreen:
    def __init__(self, screen, colors, sound_object=None):
        self.screen = screen
        self.colors = colors
        self.game_over = False
        self.sound_object = sound_object

    def show(self):
        self.screen.fill(self.colors['BLACK'])
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over! Press Q to Quit or C to Play Again", True, self.colors['WHITE'])
        text_rect = text.get_rect(
            center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        self.wait_for_key()
        return self.game_over

    def wait_for_key(self):
        waiting = True
        game_over = False
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.game_over = True
                        waiting = False
                    elif event.key == pygame.K_c:
                        game_over = False
                        waiting = False
                    elif event.key == pygame.K_m:
                        if self.sound_object is not None:
                            self.sound_object.music_on = not self.sound_object.music_on
                    elif event.key == pygame.K_s:
                        if self.sound_object is not None:
                            self.sound_object.sound_on = not self.sound_object.sound_on


class StartScreen:
    def __init__(self,screen, colors, sound_object=None):
        self.screen = screen
        self.colors = colors
        self.game_over = False
        self.sound_object = sound_object

    def show(self) -> bool:
        self.screen.fill(self.colors['BLACK'])
        font = pygame.font.Font(None, 36)

        # List of instructions to display
        instructions = [
            "To play use cursor keys to steer snake.",
            "Eat the good apples to grow your snake.",
            "Avoid bad apples. The snake will get smaller",
            "and faster and must grow longer with each new level.",
            '----------------------------------------------------------',
            "Press C to start",
            "Press M to toggle music",
            "Press S to toggle all sound",
            "Press Q to quit"
        ]

        # Starting Y position for the first line
        start_y = SCREEN_HEIGHT / 2 - len(instructions) * 20

        # Render each line of text
        for i, line in enumerate(instructions):
            text = font.render(line, True, self.colors['WHITE'])
            text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, start_y + i * 40))
            self.screen.blit(text, text_rect)

        pygame.display.flip()
        self.wait_for_key()
        return self.game_over

    def wait_for_key(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.game_over = True
                        waiting = False
                    elif event.key == pygame.K_c:
                        waiting = False
                    elif event.key == pygame.K_m:
                        self.sound_object.music_on = not self.sound_object.music_on
                        if not self.sound_object.music_on:
                            self.sound_object.stop_background_music()
                    elif event.key == pygame.K_s:
                        self.sound_object.sound_on = not self.sound_object.sound_on
                        if not self.sound_object.sound_on:
                            self.sound_object.stop_all_sounds()



class NextLevelScreen:
    def __init__(self, screen, colors, sound_object=None, level=1):
        self.screen = screen
        self.colors = colors
        self.level_number = level
        self.game_over = False
        self.sound_object = sound_object

    def show(self) -> bool:
        self.screen.fill(self.colors['BLACK'])
        font = pygame.font.Font(None, 36)

        # List of instructions to display
        instructions = [
            "Congratulations!",
            f"You completed level {self.level_number+1}",
            "Press C to start the next level!",
            "Press Q to quit"
        ]

        # Starting Y position for the first line
        start_y = SCREEN_HEIGHT / 2 - len(instructions) * 20

        # Render each line of text
        for i, line in enumerate(instructions):
            text = font.render(line, True, self.colors['WHITE'])
            text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, start_y + i * 40))
            self.screen.blit(text, text_rect)

        pygame.display.flip()
        self.wait_for_key()
        return self.game_over

    def wait_for_key(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.game_over = True
                        waiting = False
                    elif event.key == pygame.K_c:
                        waiting = False
                    elif event.key == pygame.K_m:
                        if self.sound_object is not None:
                            self.sound_object.music_on = not self.sound_object.music_on
                            if not self.sound_object.music_on:
                                self.sound_object.stop_music()
                    elif event.key == pygame.K_s:
                        if self.sound_object is not None:
                            self.sound_object.sound_on = not self.sound_object.sound_on
                            if not self.sound_object.sound_on:
                                self.sound_object.stop_all_sound()



class WinGameScreen:
    def __init__(self, screen, colors, sound_object=None):
        self.screen = screen
        self.colors = colors
        self.game_over = False
        self.sound_object = sound_object

    def show(self) -> bool:
        self.screen.fill(self.colors['BLACK'])
        font = pygame.font.Font(None, 36)

        # List of instructions to display
        instructions = [
            "Congratulations!",
            f"You Won!",
            "",
            "Press C to restart",
            "Press Q to quit"
        ]

        # Starting Y position for the first line
        start_y = SCREEN_HEIGHT / 2 - len(instructions) * 20

        # Render each line of text
        for i, line in enumerate(instructions):
            text = font.render(line, True, self.colors['WHITE'])
            text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, start_y + i * 40))
            self.screen.blit(text, text_rect)

        pygame.display.flip()
        self.wait_for_key()
        return self.game_over

    def wait_for_key(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.game_over = True
                        waiting = False
                    elif event.key == pygame.K_c:
                        waiting = False
                    elif event.key == pygame.K_m:
                        if self.sound_object is not None:
                            self.sound_object.music_on = not self.sound_object.music_on
                    elif event.key == pygame.K_s:
                        if self.sound_object is not None:
                            self.sound_object.sound_on = not self.sound_object.sound_on



class ExitScreen:
    def __init__(self, screen, colors, sound_object=None):
        self.screen = screen
        self.colors = colors
        self.game_over = False
        self.sound_object = sound_object

    def show(self) -> bool:
        self.screen.fill(self.colors['BLACK'])
        font = pygame.font.Font(None, 36)

        # List of instructions to display
        instructions = [
            "!!! THANK YOU FOR PLAYING !!!",
            "---",
            " - ",
            "Credits",
            "====================================",
            "R. Morgan : Nostalgic Developer",
            "Markie Hensen : Unrelenting Play Tester",
            "Anonymous : Music & Sound Effects",
            "---",
            "Press any key to exit.",
        ]

        # Starting Y position for the first line
        start_y = SCREEN_HEIGHT / 2 - len(instructions) * 20

        # Render each line of text
        for i, line in enumerate(instructions):
            text = font.render(line, True, self.colors['WHITE'])
            text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, start_y + i * 40))
            self.screen.blit(text, text_rect)

        pygame.display.flip()
        self.wait_for_key()
        return self.game_over

    def wait_for_key(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        if self.sound_object is not None:
                            self.sound_object.music_on = not self.sound_object.music_on
                    elif event.key == pygame.K_s:
                        if self.sound_object is not None:
                            self.sound_object.sound_on = not self.sound_object.sound_on
                    else:
                        self.game_over = True
                        waiting = False
