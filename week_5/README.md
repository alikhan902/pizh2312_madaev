Мадаев Алихан Ахьядович
ПИЖ-б-о-23-1
Неделя 5

Задание 4.3.5 Классс-контейнер

main.py

from moneyCollection import *
# Пример использования
money1 = Money(100.5)
money2 = Money(200.75)

# Создаем коллекцию
collection = MoneyCollection(money1, money2)

# Добавляем новый объект
collection.add(Money(50))

# Выводим коллекцию
print(collection)

# Сохраняем в файл
collection.save("money_collection.json")

# Загружаем из файла
loaded_collection = MoneyCollection.load("money_collection.json")
print(loaded_collection)

money.py

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


moneyCollection.py

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

Задание 4.3.6 Иерархия классов Вариант 1

main.py

from dvdplayer import *
from videoplayer import *
from audioplayer import *

audio_player = AudioPlayer("Мой аудиоплеер", "song.mp3")
audio_player.start()  # Воспроизводится аудио от Браво
audio_player.stop()   # Останавливается аудио

video_player = VideoPlayer("ВидеоПлеер")
video_player.start()  # Воспроизводится видео в разрешении 1080p
video_player.stop()   # Останавливается видео

dvd_player = DvdPlayer("DvdПлеер", dvd_disc="Фильм: Побег")
dvd_player.start()  # Воспроизводится DVD диск "Фильм: Побег"
dvd_player.stop()   # Останавливается воспроизведение DVD

player.py

# Базовый класс Плеер
class Player:
    """
    Базовый класс для всех типов плееров. Реализует основные методы управления воспроизведением.
    """
    def __init__(self, name):
        """
        Инициализация плеера.
        
        :param name: название плеера (например, 'АудиоПлеер', 'ВидеоПлеер', 'DvdПлеер')
        """
        self.name = name
        self.is_playing = False  # Флаг, который отслеживает состояние воспроизведения.

    def start(self):
        """
        Метод для начала воспроизведения. Если плеер уже воспроизводит, выводится сообщение.
        """
        if not self.is_playing:
            self.is_playing = True
            print(f"{self.name} начал воспроизведение.")
        else:
            print(f"{self.name} уже воспроизводит.")

    def stop(self):
        """
        Метод для остановки воспроизведения. Если плеер не воспроизводит, выводится сообщение.
        """
        if self.is_playing:
            self.is_playing = False
            print(f"{self.name} остановил воспроизведение.")
        else:
            print(f"{self.name} не воспроизводит.")



audioplayer.py

from player import *

class AudioPlayer(Player):
    """
    Класс для аудиоплеера, наследует от базового класса Player.
    Реализует дополнительные особенности для воспроизведения аудиофайлов.
    """
    def __init__(self, name, audio_file=None):
        """
        Инициализация аудиоплеера с параметром для аудиофайла.
        
        :param name: название плеера.
        :param audio_file: название аудиофайла, который будет воспроизводиться.
        """
        super().__init__(name)  # Вызов конструктора базового класса Player
        self.__audio_file = audio_file  # Аудиофайл, который будет воспроизводиться

    @property
    def audio_file(self):
        """Геттер для получения суммы денег."""
        return self.__audio_file
    
    @audio_file.setter
    def amount(self, value):
        self.__audio_file = value

    def start(self):
        """
        Переопределение метода для начала воспроизведения аудиофайла.
        """
        super().start()  # Вызов метода start() из базового класса Player
        print(f"Воспроизведение аудиофайла {self.audio_file}.")

    def stop(self):
        """
        Переопределение метода для остановки воспроизведения аудиофайла.
        """
        super().stop()  # Вызов метода stop() из базового класса Player
        print("Аудио воспроизведение остановлено.")



dvdplayer.py

from player import *

# Класс DvdПлеер наследует от Плеера
class DvdPlayer(Player):
    """
    Класс для DVD плеера, наследует от базового класса Player.
    Реализует дополнительные особенности для воспроизведения DVD дисков.
    """
    def __init__(self, name, dvd_disc=None):
        """
        Инициализация DVD плеера с параметром для диска.
        
        :param name: название плеера.
        :param dvd_disc: название DVD диска, который будет воспроизводиться.
        """
        super().__init__(name)  # Вызов конструктора базового класса Player
        self.__dvd_disc = dvd_disc  # Диск, который будет воспроизводиться

    @property
    def dvd_disc(self):
        """Геттер для получения суммы денег."""
        return self.__dvd_disc
    
    @dvd_disc.setter
    def amount(self, value):
        self.__dvd_disc = value
    
    def start(self):
        """
        Переопределение метода для начала воспроизведения DVD.
        """
        super().start()  # Вызов метода start() из базового класса Player
        print(f"Воспроизведение DVD диска {self.dvd_disc}.")

    def stop(self):
        """
        Переопределение метода для остановки воспроизведения DVD.
        """
        super().stop()  # Вызов метода stop() из базового класса Player
        print("DVD воспроизведение остановлено.")


videoplayer.py


from player import *

# Класс ВидеоПлеер наследует от Плеера
class VideoPlayer(Player):
    """
    Класс для видео плеера, наследует от базового класса Player.
    Реализует дополнительные особенности для воспроизведения видео.
    """
    def __init__(self, name, resolution="1080p"):
        """
        Инициализация видео плеера с параметром разрешения.
        
        :param name: название плеера.
        :param resolution: разрешение видео (по умолчанию 1080p).
        """
        super().__init__(name)  # Вызов конструктора базового класса Player
        self.__resolution = resolution


    @property
    def resolution(self):
        """Геттер для получения суммы денег."""
        return self.__resolution
    
    @resolution.setter
    def amount(self, value):
        self.__resolution = value

    def start(self):
        """
        Переопределение метода для начала воспроизведения видео.
        """
        super().start()  # Вызов метода start() из базового класса Player
        print(f"Воспроизведение видео в разрешении {self.resolution}.")

    def stop(self):
        """
        Переопределение метода для остановки воспроизведения видео.
        """
        super().stop()  # Вызов метода stop() из базового класса Player
        print("Видео остановлено.")

