import random
import pygame

CELL_SIZE = 20
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.position = (CELL_SIZE * (WINDOW_WIDTH // 2) // CELL_SIZE, CELL_SIZE * (WINDOW_HEIGHT // 2) // CELL_SIZE)
        self.positions = [self.position]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.length = 1
        self.score = 0
        self.last_move_time = pygame.time.get_ticks()

    def get_head_position(self):
        return self.positions[0]

    def turn(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def move(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_move_time >= 40:
            x, y = self.direction
            head = self.get_head_position()
            new_pos = ((head[0] + x * CELL_SIZE) % WINDOW_WIDTH,
                       (head[1] + y * CELL_SIZE) % WINDOW_HEIGHT)

            if new_pos in self.positions[2:]:
                self.reset()
            else:
                self.positions.insert(0, new_pos)
                if len(self.positions) > self.length:
                    self.positions.pop()
            self.last_move_time = current_time

    def reset(self):
        self.__init__()

    def increase_score(self):
        self.score += 10

    def get_score(self):
        return self.score

    def update_direction(self, new_direction):
        if new_direction and (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction