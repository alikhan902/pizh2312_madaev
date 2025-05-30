import random

CELL_SIZE = 20
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

class Apple:
    def __init__(self):
        self.position = (0, 0)

    def randomize_position(self, snake):
        while True:
            x = random.randint(0, (WINDOW_WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (WINDOW_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            pos = (x, y)
            if pos not in snake.positions:
                self.position = pos
                break
