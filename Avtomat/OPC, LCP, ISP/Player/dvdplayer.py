from player import Player

class DvdPlayer(Player):
    def __init__(self, name, dvd_disc=None):
        super().__init__(name)
        self._dvd_disc = dvd_disc

    @property
    def dvd_disc(self):
        return self._dvd_disc

    @dvd_disc.setter
    def dvd_disc(self, value):
        self._dvd_disc = value

    def start(self):
        super().start()
        if self.is_playing:
            print(f"Воспроизведение DVD диска {self.dvd_disc}.")

    def stop(self):
        super().stop()
        if not self.is_playing:
            print("DVD воспроизведение остановлено.")
