import pygame

CELL_SIZE = 20

class SnakeRenderer:
    def __init__(self, snake):
        self.snake = snake

    def draw(self, surface):
        for pos in self.snake.positions:
            rect = pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, (0, 255, 0), rect)

class AppleRenderer:
    def __init__(self, apple):
        self.apple = apple

    def draw(self, surface):
        rect = pygame.Rect(self.apple.position[0], self.apple.position[1], CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, (255, 0, 0), rect)

class ScoreRenderer:
    def __init__(self, snake):
        self.snake = snake
        self.font = pygame.font.Font(None, 36)

    def draw(self, surface):
        score_text = self.font.render(f"Score: {self.snake.get_score()}", True, (255, 255, 255))
        surface.blit(score_text, (10, 10))
