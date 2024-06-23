# Summary

---

The Sound class manages sound effects and background music for a game using the Pygame library. It allows toggling sound and music on or off, adjusting volumes, and playing or stopping specific sounds.

### Example Usage
```
sound = Sound()
sound.sound_on = True
sound.music_on = True
sound.play_win_sound()
sound.stop_all_sounds()
```

## Code Analysis

---

### Main functionalities
- Toggle sound effects and background music on or off.
- Adjust the volume for sound effects and background music.
- Play and stop specific sound effects and background music.

---

### Methods
- sound_on: Getter and setter for the _sound_on attribute. Stops all sounds when set to False.
- music_on: Getter and setter for the _music_on attribute. Plays or stops background music based on its value.
- play_background_music: Plays the background music on a loop if music is enabled.
- stop_background_music: Stops the background music if music is enabled.
- play_win_sound: Plays the win sound if sound is enabled.
- stop_win_sound: Stops the win sound if sound is enabled.
- play_lose_sound: Plays the lose sound if sound is enabled.
- stop_lose_sound: Stops the lose sound if sound is enabled.
- play_hit_wall_sound: Plays the hit wall sound if sound is enabled.
- stop_hit_wall_sound: Stops the hit wall sound if sound is enabled.
- stop_all_sounds: Stops all sounds and background music.

---

### Fields
- _sound_on: Boolean indicating if sound effects are enabled.
- sound_volume: Float representing the volume level for sound effects.
- _music_on: Boolean indicating if background music is enabled.
- music_volume: Float representing the volume level for background music.
- background_music: Pygame Sound object for background music.
- win_sound: Pygame Sound object for the win sound effect.
- lose_sound: Pygame Sound object for the lose sound effect.
- hit_wall_sound: Pygame Sound object for the hit wall sound effect.

---
