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

