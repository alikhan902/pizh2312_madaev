Выполнил Мадаев Алихан Ахьядович
ПИЖ-б-о-23-1

Задание 1: Класс Vector3D

main.py:

from module import *
    
v1 = Vector3D(4, 1, 2)
v1.display()

v2 = Vector3D()
v2.read()

v3 = Vector3D(1, 2, 3)
v4 = v1 + v2
v4.display()

a = v4 * v3
print(a)

v4 = v1 * 10  
v4.display()

v4 = v1 @ v3 
v4.display()

module.py:

from abc import ABC, abstractmethod

class AbstractVector(ABC):
    """
    Абстрактный класс для векторов.
    Определяет интерфейс, который должны реализовать все векторные классы.
    """

    @property
    @abstractmethod
    def x(self):
        """Геттер для координаты x."""
        pass

    @x.setter
    @abstractmethod
    def x(self, value):
        """Сеттер для координаты x."""
        pass

    @property
    @abstractmethod
    def y(self):
        """Геттер для координаты y."""
        pass

    @y.setter
    @abstractmethod
    def y(self, value):
        """Сеттер для координаты y."""
        pass

    @property
    @abstractmethod
    def z(self):
        """Геттер для координаты z."""
        pass

    @z.setter
    @abstractmethod
    def z(self, value):
        """Сеттер для координаты z."""
        pass
    
    @abstractmethod
    def display(self):
        """Метод для отображения координат вектора."""
        pass
    
    @abstractmethod
    def read(self):
        """Метод для ввода координат вектора с клавиатуры."""
        pass

    @abstractmethod
    def __add__(self, other):
        """Метод для сложения векторов."""
        pass

    @abstractmethod
    def __sub__(self, other):
        """Метод для вычитания векторов."""
        pass

    @abstractmethod
    def __mul__(self, other):
        """Метод для умножения на число или скалярного произведения."""
        pass

    @abstractmethod
    def __matmul__(self, other):
        """Метод для векторного произведения."""
        pass

    @abstractmethod
    def __call__(self):
        """Делает объект вызываемым (например, для вычисления длины вектора)."""
        pass
    def __del__(self):
        """Удаляет обьект"""
        pass


class Vector3D(AbstractVector):
    """
    Класс для работы с трехмерными векторами.
    Реализует интерфейс, заданный в AbstractVector.
    """
    
    def __init__(self, x=0, y=0, z=0):
        """
        Конструктор класса Vector3D.
        :param x: Координата x
        :param y: Координата y
        :param z: Координата z
        """
        self.__x = x
        self.__y = y
        self.__z = z

    @property
    def x(self):
        """Возвращает координату x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Устанавливает координату x."""
        self.__x = value

    @property
    def y(self):
        """Возвращает координату y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Устанавливает координату y."""
        self.__y = value

    @property
    def z(self):
        """Возвращает координату z."""
        return self.__z

    @z.setter
    def z(self, value):
        """Устанавливает координату z."""
        self.__z = value

    def display(self):
        """Выводит координаты вектора."""
        print(f"({self.x}, {self.y}, {self.z})")
    
    def read(self):
        """Считывает координаты вектора с клавиатуры."""
        self.x = int(input("Введите x: "))
        self.y = int(input("Введите y: "))
        self.z = int(input("Введите z: "))

    def __add__(self, other):
        """Сложение двух векторов."""
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        """Вычитание двух векторов."""
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        """
        Умножение вектора на число или скалярное произведение двух векторов.
        :param other: Число или другой вектор
        :return: Число (скалярное произведение) или новый вектор
        """
        if isinstance(other, Vector3D):  # Скалярное произведение
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(other, (int, float)):  # Умножение на число
            return Vector3D(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError("Умножение возможно только на число или другой вектор")
    
    def __matmul__(self, other):
        """
        Векторное произведение двух векторов.
        :param other: Другой вектор
        :return: Новый вектор - результат векторного произведения
        """
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def __call__(self):
        """Возвращает длину вектора."""
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

    def __del__(self):
        """Вызывается при удалении объекта, выводит сообщение."""
        print(f"Объект Vector3D с координатами ({self.x}, {self.y}, {self.z}) удален.")


class VectorOperations:
    """
    Класс для работы с векторами (композиция).
    Содержит объект класса Vector3D и выполняет операции над ним.
    """
    
    def __init__(self, vector: Vector3D):
        """
        Конструктор класса VectorOperations.
        :param vector: Объект класса Vector3D.
        """
        self.vector = vector  # Композиция - объект вектора хранится внутри класса

    def scale(self, factor):
        """
        Масштабирование вектора.
        :param factor: Число, на которое умножается вектор.
        :return: Новый масштабированный вектор.
        """
        return Vector3D(self.vector.x * factor, self.vector.y * factor, self.vector.z * factor)

    def length(self):
        """
        Вычисляет длину вектора.
        :return: Число - длина вектора.
        """
        return (self.vector.x**2 + self.vector.y**2 + self.vector.z**2) ** 0.5
