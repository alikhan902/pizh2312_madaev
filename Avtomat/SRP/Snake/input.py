import pygame

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class InputHandler:
    def __init__(self):
        self.quit = False
        self.direction = None  

    def process_events(self):
        self.direction = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit = True
                elif event.key == pygame.K_UP:
                    self.direction = UP
                elif event.key == pygame.K_DOWN:
                    self.direction = DOWN
                elif event.key == pygame.K_LEFT:
                    self.direction = LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = RIGHT
