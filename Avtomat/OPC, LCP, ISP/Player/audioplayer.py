from player import Player

class AudioPlayer(Player):
    def __init__(self, name, audio_file=None):
        super().__init__(name)
        self._audio_file = audio_file

    @property
    def audio_file(self):
        return self._audio_file

    @audio_file.setter
    def audio_file(self, value):
        self._audio_file = value

    def start(self):
        super().start()
        if self.is_playing:
            print(f"Воспроизведение аудиофайла {self.audio_file}.")

    def stop(self):
        super().stop()
        if not self.is_playing:
            print("Аудио воспроизведение остановлено.")
