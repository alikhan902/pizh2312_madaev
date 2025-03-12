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
