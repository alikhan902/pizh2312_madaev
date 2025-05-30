from abc import ABC, abstractmethod

class IPlayable(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Player(IPlayable):
    def __init__(self, name):
        self.name = name
        self.is_playing = False

    def start(self):
        if not self.is_playing:
            self.is_playing = True
            print(f"{self.name} начал воспроизведение.")
        else:
            print(f"{self.name} уже воспроизводит.")

    def stop(self):
        if self.is_playing:
            self.is_playing = False
            print(f"{self.name} остановил воспроизведение.")
        else:
            print(f"{self.name} не воспроизводит.")
