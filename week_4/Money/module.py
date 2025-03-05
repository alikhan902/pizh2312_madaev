import json

class Money:
    """
    Класс Money представляет денежную сумму с возможностью арифметических операций
    и сохранения/загрузки из JSON-файла.
    """
    def __init__(self, amount: float):
        """
        Инициализация объекта Money.
        :param amount: Сумма денег в виде float.
        """
        self._amount = round(amount, 2)
    
    @property
    def amount(self):
        """Геттер для получения суммы денег."""
        return self._amount
    
    @amount.setter
    def amount(self, value):
        """Сеттер для установки суммы денег."""
        if value < 0:
            raise ValueError("Сумма денег не может быть отрицательной")
        self._amount = round(value, 2)
    
    def __str__(self):
        """Возвращает строковое представление объекта Money."""
        return f"{self.amount} USD"
    
    @classmethod
    def from_string(cls, str_value: str):
        """Создает объект Money из строки."""
        return cls(float(str_value))
    
    def save(self, filename):
        """Сохраняет объект Money в JSON-файл."""
        with open(filename, 'w') as file:
            json.dump({'amount': self.amount}, file)
    
    @classmethod
    def load(cls, filename):
        """Загружает объект Money из JSON-файла."""
        with open(filename, 'r') as file:
            data = json.load(file)
        return cls(data['amount'])
    
    def __add__(self, other):
        """Позволяет складывать два объекта Money."""
        return Money(self.amount + other.amount)
    
    def __sub__(self, other):
        """Позволяет вычитать один объект Money из другого."""
        return Money(self.amount - other.amount)
    
    def __mul__(self, factor: float):
        """Позволяет умножать объект Money на число."""
        return Money(self.amount * factor)
    
