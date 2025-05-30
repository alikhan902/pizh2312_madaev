from player import Player

class VideoPlayer(Player):
    def __init__(self, name, resolution="1080p"):
        super().__init__(name)
        self._resolution = resolution

    @property
    def resolution(self):
        return self._resolution

    @resolution.setter
    def resolution(self, value):
        self._resolution = value

    def start(self):
        super().start()
        if self.is_playing:
            print(f"Воспроизведение видео в разрешении {self.resolution}.")

    def stop(self):
        super().stop()
        if not self.is_playing:
            print("Видео остановлено.")
