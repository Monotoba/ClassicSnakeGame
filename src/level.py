class Level:
    def __init__(self, level_number, cell_size, target_length, speed, golden_apples=False, poison_apples=False):
        self.level_number: int = level_number
        self.cell_size = cell_size
        self.target_length: int = target_length
        self.speed: int = speed
        self.golden_apples: bool = golden_apples
        self.poison_apples: bool = poison_apples

# Define levels here...
LEVELS = [
    Level(level_number=1, cell_size=20, target_length=30, speed=8, golden_apples=False, poison_apples=False),
    Level(level_number=2, cell_size=20, target_length=50, speed=9, golden_apples=False, poison_apples=False),
    Level(level_number=3, cell_size=20, target_length=100, speed=10, golden_apples=False, poison_apples=False),
    Level(level_number=4, cell_size=10, target_length=150, speed=10, golden_apples=True, poison_apples=False),
    Level(level_number=5, cell_size=10, target_length=200, speed=10, golden_apples=True, poison_apples=False),
    Level(level_number=6, cell_size=10, target_length=300, speed=11, golden_apples=True, poison_apples=False),
    Level(level_number=7, cell_size=10, target_length=450, speed=11, golden_apples=True, poison_apples=True),
    Level(level_number=8, cell_size=10, target_length=700, speed=11, golden_apples=True, poison_apples=True),
    Level(level_number=9, cell_size=10, target_length=900, speed=11, golden_apples=True, poison_apples=True),
    Level(level_number=10, cell_size=10, target_length=1200, speed=12, golden_apples=True, poison_apples=True),
]
