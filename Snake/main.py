import pygame
from snake import Snake
from apple import Apple

# Настройки окна
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
BLACK = (0, 0, 0)

# Инициализация
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Изгиб Питона')
clock = pygame.time.Clock()

# Создаем экземпляры классов
snake = Snake()
apple = Apple()

# Главный игровой цикл
while True:
    clock.tick(144)  # Частота обновления экрана
    screen.fill(BLACK)
    
    # Обработка событий и движения
    snake.handle_keys()   # Обрабатываем нажатия клавиш
    snake.move()          # Перемещаем змейку

    # Если змейка съела яблоко
    if snake.get_head_position() == apple.position:
        snake.length += 1
        apple.randomize_position(snake)  # Передаем объект snake в метод randomize_position
        snake.increase_score()  # Увеличиваем счёт при поедании яблока

    # Отображение объектов
    snake.draw(screen)
    apple.draw(screen)
    snake.draw_score(screen)  # Отображение счёта

    pygame.display.update()
