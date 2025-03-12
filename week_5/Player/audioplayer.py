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
