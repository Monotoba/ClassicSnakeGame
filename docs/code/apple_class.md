Summary
The Apple class represents an apple object in a game, which can be drawn on the screen and can change its position randomly within the screen boundaries.
Example Usage
```
import pygame
from random import randint

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create an apple object
apple = Apple(cell_size=20, color=(255, 0, 0))

# Draw the apple on the screen
apple.draw(screen)

# Respawn the apple at a new random position
apple.respawn()
```

## Code Analysis

---

### Main functionalities
The Apple class provides functionalities to:
1. Initialize an apple with a specific size and color.
2. Randomly position the apple within the screen boundaries.
3. Draw the apple on a given surface.
4. Respawn the apple at a new random position.
 
---

### Methods
- __init__(self, cell_size: int, color): Initializes the apple with a given cell size and color, and positions it randomly on the screen.
- respawn(self): Changes the apple's position to a new random location within the screen boundaries.
- draw(self, surface): Draws the apple as a rectangle on the provided surface.
 
### Fields
- cell_size: The size of the apple in pixels.
- position: A tuple representing the current position of the apple on the screen.
- color: The color of the apple.

---
