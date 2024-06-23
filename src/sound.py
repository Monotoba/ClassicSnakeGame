import os
import pygame


class Sound:
    def __init__(self):
        pygame.mixer.init()
        self._sound_on = False
        self.sound_volume = 0.5
        self._music_on = False
        self.music_volume = 0.5
        self.background_music = None
        self.win_sound = None
        self.lose_sound = None
        self.hit_wall_sound = None
        self.load_files()

    def load_files(self):
        # Get absolute path to assets folder
        script_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(script_dir, '..', 'assets')
        # Background music
        file_path = os.path.join(assets_dir, 'background_music.mp3')
        self.background_music = pygame.mixer.Sound(file_path)
        # Level up sound
        file_path = os.path.join(assets_dir, 'level_up.mp3')
        self.win_sound = pygame.mixer.Sound(file_path)
        # Game Over sound
        file_path = os.path.join(assets_dir, 'game_over.mp3')
        self.lose_sound = pygame.mixer.Sound(file_path)
        # Hit Wall sound
        file_path = os.path.join(assets_dir, 'game_over.mp3')
        self.hit_wall_sound = pygame.mixer.Sound(file_path)

    # Getter and Setter for sound_on
    @property
    def sound_on(self):
        return self._sound_on

    @sound_on.setter
    def sound_on(self, value):
        self._sound_on = value
        if not self._sound_on:
            self.stop_all_sounds()


    # Getter and Setter for music_on
    @property
    def music_on(self):
        return self._music_on

    @music_on.setter
    def music_on(self, value):
        self._music_on = value
        if self._music_on:
            self.play_background_music()
        else:
            self.stop_background_music()

    def play_background_music(self):
        if self._music_on:
            self.background_music.set_volume(self.music_volume)
            self.background_music.play(-1)

    def stop_background_music(self):
        if self._music_on:
            self.background_music.stop()

    def play_win_sound(self):
        if self._sound_on:
            self.win_sound.set_volume(self.sound_volume)
            self.win_sound.play()

    def stop_win_sound(self):
        if self._sound_on:
            self.win_sound.stop()

    def play_lose_sound(self):
        if self._sound_on:
            self.lose_sound.set_volume(self.sound_volume)
            self.lose_sound.play()

    def stop_lose_sound(self):
        if self._sound_on:
            self.lose_sound.stop()

    def play_hit_wall_sound(self):
        if self._sound_on:
            self.hit_wall_sound.set_volume(self.sound_volume)
            self.hit_wall_sound.play()

    def stop_hit_wall_sound(self):
        if self._sound_on:
            self.hit_wall_sound.stop()

    def stop_all_sounds(self):
        self.stop_win_sound()
        self.stop_lose_sound()
        self.stop_hit_wall_sound()
        self.stop_background_music()
