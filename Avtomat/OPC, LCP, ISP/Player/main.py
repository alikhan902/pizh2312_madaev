from dvdplayer import *
from videoplayer import *
from audioplayer import *
from player import IPlayable

audio_player = AudioPlayer("Мой аудиоплеер", "song.mp3")
audio_player.start()  # Воспроизводится аудио от Браво
audio_player.stop()   # Останавливается аудио

video_player = VideoPlayer("ВидеоПлеер")
video_player.start()  # Воспроизводится видео в разрешении 1080p
video_player.stop()   # Останавливается видео

dvd_player = DvdPlayer("DvdПлеер", dvd_disc="Фильм: Побег")
dvd_player.start()  # Воспроизводится DVD диск "Фильм: Побег"
dvd_player.stop()   # Останавливается воспроизведение DVD


def play_media(player: IPlayable):
    player.start()
    player.stop()

play_media(AudioPlayer("Аудио", "song.mp3"))
play_media(VideoPlayer("Видео"))
play_media(DvdPlayer("DVD", "Фильм"))
