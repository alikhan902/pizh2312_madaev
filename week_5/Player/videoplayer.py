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

