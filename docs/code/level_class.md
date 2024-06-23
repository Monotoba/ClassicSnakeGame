# Summary

---

The Level class is designed to represent a level in a game, encapsulating properties such as level number, cell size, target length, speed, and optional features like golden apples and poison apples.

This file also include a list of predefined levels (LEVELS) for use in the game. Players should feel free to adjust the values for each level to meet their specific use-case.

### Example Usage
```
level1 = Level(level_number=1, cell_size=20, target_length=5, speed=10, golden_apples=True, poison_apples=False)
print(level1.level_number)  # Output: 1
print(level1.golden_apples)  # Output: True
```

## Code Analysis

---

### Main functionalities
The main functionality of the Level class is to initialize and store the properties of a game level, which can be used to control the game's difficulty and features.

---

### Methods

The primary method in the Level class is the __init__ method, which initializes the class with the provided parameters.

---

### Fields
- level_number: An integer representing the level number.
- cell_size: The size of each cell in the game grid.
- target_length: An integer representing the target length to achieve in the level.
- speed: An integer representing the speed of the game.
- golden_apples: A boolean indicating whether golden apples are present in the level.
- poison_apples: A boolean indicating whether poison apples are present in the level.

---
