```python
Мадаев Алихан Ахьядович
ПИЖ-б-о-23-1

Проект змейка

game.py

import pygame
from abc import ABC, abstractmethod

# Размер клетки
CELL_SIZE = 20

class GameObject(ABC):
    """
    Абстрактный базовый класс для всех объектов в игре (змейка, яблоко и другие).
    Содержит общие методы для инициализации и отрисовки объектов на экране.
    """

    def __init__(self, position, color):
        """
        Инициализация объекта.

        Args:
            position (tuple): Позиция объекта на экране (x, y).
            color (tuple): Цвет объекта в формате (R, G, B).
        """
        self.position = position
        self.color = color

    @abstractmethod
    def draw(self, surface):
        """
        Абстрактный метод для отрисовки объекта.
        Это нужно реализовать в дочерних классах.

        Args:
            surface (pygame.Surface): Поверхность, на которой рисуется объект.
        """
        pass

snake.py

import random
import pygame
from apple import Apple 
from game import GameObject

# Направления движения змейки
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

CELL_SIZE = 20
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
SPEED = 40

class Snake(GameObject):
    """
    Класс для представления змейки, её движения, увеличения длины и подсчёта очков.
    """

    def __init__(self):
        """
        Инициализирует начальное состояние змейки.
        Змейка начинается в центре экрана, имеет длину 1 и счёт 0.
        """
        self.position = (CELL_SIZE * (WINDOW_WIDTH // 2) // CELL_SIZE, CELL_SIZE * (WINDOW_HEIGHT // 2) // CELL_SIZE)
        self.positions = [self.position]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.length = 1
        self.score = 0  # Счёт змейки
        self.last_move_time = pygame.time.get_ticks()
        self.font = pygame.font.Font(None, 36)  # Шрифт для отображения счёта

    def get_head_position(self):
        """
        Возвращает текущую позицию головы змейки.

        Returns:
            tuple: Позиция головы змейки (x, y).
        """
        return self.positions[0]

    def turn(self, direction):
        """
        Меняет направление движения змейки, если оно не противоположное текущему.

        Args:
            direction (tuple): Направление (x, y), в котором должна двигаться змейка.
        """
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def move(self):
        """
        Перемещает змейку в заданном направлении, обновляет её позицию.
        Если змейка сталкивается с собой, вызывает сброс игры.
        """
        current_time = pygame.time.get_ticks()
        if current_time - self.last_move_time >= SPEED:  # Проверка времени
            cur = self.get_head_position()
            x, y = self.direction
            new_pos = ((cur[0] + (x * CELL_SIZE)) % WINDOW_WIDTH, (cur[1] + (y * CELL_SIZE)) % WINDOW_HEIGHT)
            if new_pos in self.positions[2:]:
                self.reset()  # Столкновение с телом змеи — сброс игры
            else:
                self.positions.insert(0, new_pos)
                if len(self.positions) > self.length:
                    self.positions.pop()
            self.last_move_time = current_time

    def reset(self):
        """
        Сбрасывает змейку в начальное состояние: длина 1, позиция в центре экрана, счёт 0.
        """
        self.__init__()  # Сбрасываем змейку и начинаем игру с начальной длиной

    def draw(self, surface):
        """
        Отображает змейку на экране.

        Args:
            surface (pygame.Surface): Поверхность, на которой рисуется змейка.
        """
        for pos in self.positions:
            rect = pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, (0, 255, 0), rect)

    def handle_keys(self):
        """
        Обрабатывает нажатия клавиш для управления змейкой.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)
                elif event.key == pygame.K_ESCAPE:  # Выход из игры
                    pygame.quit()
                    quit()  # Закрыть игру при нажатии Esc

    def increase_score(self):
        """
        Увеличивает счёт на 10 за каждое съеденное яблоко.
        """
        self.score += 10

    def get_score(self):
        """
        Возвращает текущий счёт змейки.

        Returns:
            int: Текущий счёт.
        """
        return self.score

    def draw_score(self, surface):
        """
        Отображает счёт на экране.

        Args:
            surface (pygame.Surface): Поверхность, на которой рисуется счёт.
        """
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        surface.blit(score_text, (10, 10))  # Отображение счёта в левом верхнем углу

apple.py

import random
import pygame
from game import GameObject

CELL_SIZE = 20
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

class Apple(GameObject):
    """
    Класс для представления яблока, его случайной генерации и отображения на экране.
    """

    def __init__(self):
        """
        Инициализирует яблоко, но не вызывает randomize_position, потому что для этого нужен объект змейки.
        """
        self.position = (0, 0)

    def randomize_position(self, snake):
        """
        Генерирует случайную позицию для яблока, проверяя, чтобы оно не попадало на тело змейки.

        Args:
            snake (Snake): Объект змейки для проверки на пересечение с её телом.
        """
        valid_position = False
        while not valid_position:
            x = random.randint(0, (WINDOW_WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (WINDOW_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            self.position = (x, y)
            valid_position = True
            # Проверка, не совпадает ли позиция яблока с телом змеи
            for pos in snake.positions:
                if self.position == pos:
                    valid_position = False  # Если яблоко попало на тело змеи, пробуем заново
                    break

    def draw(self, surface):
        """
        Отображает яблоко на экране.

        Args:
            surface (pygame.Surface): Поверхность, на которой рисуется яблоко.
        """
        rect = pygame.Rect(self.position[0], self.position[1], CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, (255, 0, 0), rect)

main.py

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
