import json
from money import *

class MoneyCollection:
    """
    Класс-контейнер для объектов Money.
    """
    def __init__(self, *args):
        """
        Инициализация объекта VectorCollection.
        :param args: Данные объекты Money, которые будут добавлены в контейнер.
        """
        self._data = list(args)
    
    def __str__(self):
        """Возвращает строковое представление всех объектов в контейнере."""
        return ', '.join(str(item) for item in self._data)
    
    def __getitem__(self, index):
        """Индексация для доступа к объектам Money в контейнере."""
        return self._data[index]
    
    def add(self, value):
        """Добавление объекта Money в контейнер."""
        if isinstance(value, Money):
            self._data.append(value)
        else:
            raise ValueError("Можно добавить только объекты Money.")
    
    def remove(self, index):
        """Удаление объекта Money по индексу из контейнера."""
        if 0 <= index < len(self._data):
            del self._data[index]
        else:
            raise IndexError("Индекс вне диапазона.")
    
    def save(self, filename):
        """Сохраняет все объекты Money в JSON-файл."""
        with open(filename, 'w') as file:
            json.dump([{'amount': item.amount} for item in self._data], file)
    
    @classmethod
    def load(cls, filename):
        """Загружает объекты Money из JSON-файла."""
        with open(filename, 'r') as file:
            data = json.load(file)
        return cls(*[Money(item['amount']) for item in data])
