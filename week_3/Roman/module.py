from abc import ABC, abstractmethod

class AbstractRomanNumber(ABC):
    """
    Абстрактный класс для работы с римскими числами.
    Определяет интерфейс для реализации арифметических операций и преобразований.
    """
    @abstractmethod
    def __init__(self, value):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __int__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __sub__(self, other):
        pass

    @abstractmethod
    def __mul__(self, other):
        pass

    @abstractmethod
    def __floordiv__(self, other):
        pass
    
    @abstractmethod
    def __call__(self):
        pass


class RomanConverter:
    """
    Класс для преобразования римских чисел в арабские и обратно.
    Содержит методы для конвертации римских чисел в целые и наоборот.
    """
    ROMAN_TO_INT = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    
    INT_TO_ROMAN = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    @staticmethod
    def roman_to_int(roman):
        """
        Преобразует римское число в арабское.
        :param roman: Строка римского числа.
        :return: Целое число.
        """
        result, prev_value = 0, 0
        for char in reversed(roman):
            current_value = RomanConverter.ROMAN_TO_INT[char]
            if current_value < prev_value:
                result -= current_value
            else:
                result += current_value
            prev_value = current_value
        return result

    @staticmethod
    def int_to_roman(num):
        """
        Преобразует арабское число в римское.
        :param num: Целое число.
        :return: Строка римского числа.
        """
        result = ""
        for arabic, roman in RomanConverter.INT_TO_ROMAN:
            while num >= arabic:
                result += roman
                num -= arabic
        return result


class Roman(AbstractRomanNumber):
    """
    Класс для работы с римскими числами с использованием композиции.
    Позволяет выполнять арифметические операции и преобразования между римскими и арабскими числами.
    """
    
    def __init__(self, value):
        """
        Инициализация римского числа.
        :param value: Либо строка римского числа, либо целое число.
        :raises TypeError: Если переданный аргумент не является строкой или целым числом.
        """
        self.converter = RomanConverter()  # Создаем объект-конвертер
        if isinstance(value, int):
            self.value = value
        elif isinstance(value, str):
            self.value = self.converter.roman_to_int(value)
        else:
            raise TypeError("Допустимы только строки римских чисел или целые числа")
    
    def __str__(self):
        """
        Возвращает строковое представление числа в римском формате.
        """
        return self.converter.int_to_roman(self.value)
    
    def __int__(self):
        """
        Возвращает целочисленное представление числа.
        """
        return self.value
    
    def __add__(self, other):
        """
        Складывает два римских числа.
        """
        return Roman(self.value + int(other))
    
    def __sub__(self, other):
        """
        Вычитает одно римское число из другого.
        """
        return Roman(self.value - int(other))
    
    def __mul__(self, other):
        """
        Умножает два римских числа.
        """
        return Roman(self.value * int(other))
    
    def __floordiv__(self, other):
        """
        Делит одно римское число на другое с округлением вниз.
        """
        return Roman(self.value // int(other))
    
    def __call__(self):
        """
        Возвращает целочисленное значение при вызове объекта.
        """
        return self.value
