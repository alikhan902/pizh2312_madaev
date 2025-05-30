import pygame
from snake import Snake
from apple import Apple
from renderers import SnakeRenderer, AppleRenderer, ScoreRenderer
from input import InputHandler

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Изгиб Питона")
clock = pygame.time.Clock()

snake = Snake()
apple = Apple()
apple.randomize_position(snake)

snake_renderer = SnakeRenderer(snake)
apple_renderer = AppleRenderer(apple)
score_renderer = ScoreRenderer(snake)
input_handler = InputHandler()

while True:
    clock.tick(144)
    screen.fill(BLACK)

    input_handler.process_events()
    if input_handler.quit:
        pygame.quit()
        quit()

    snake.update_direction(input_handler.direction)
    snake.move()

    if snake.get_head_position() == apple.position:
        snake.length += 1
        snake.increase_score()
        apple.randomize_position(snake)

    snake_renderer.draw(screen)
    apple_renderer.draw(screen)
    score_renderer.draw(screen)

    pygame.display.update()
