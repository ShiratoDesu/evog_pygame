import os
import pygame
from assets.assets import Assets


class Sound(Assets):
    def __init__(self, overall_volume, music_volume, effect_volume) -> None:
        Assets.__init__(self)
        self.load_dir()
        self.load_bg_musics()
        self.load_sounds_effects()
        self.overall_volume = overall_volume
        self.music_volume = music_volume
        self.effect_volume = effect_volume

    def load_dir(self):
        self.bg_musics_dir = os.path.join(self.sounds_dir, "bg_musics")
        self.effects_dir = os.path.join(self.sounds_dir, "effects")

    def load_bg_musics(self):
        self.title_theme = os.path.join(self.bg_musics_dir, "TitleTheme.wav")
        self.title_theme_end = os.path.join(
            self.bg_musics_dir, "TitleThemeEnd.wav")
        self.begin_theme_intro = os.path.join(
            self.bg_musics_dir, "JourneyBeginsIntro.wav")
        self.begin_theme_loop = os.path.join(
            self.bg_musics_dir, "JourneyBeginsLoop.wav")
        self.begin_theme_end = os.path.join(
            self.bg_musics_dir, "JourneyBeginsEnd.wav")

    def load_sounds_effects(self):
        self.cursor_sound = os.path.join(self.effects_dir, "cursor.ogg")
        self.confirm_sound = os.path.join(self.effects_dir, "confirm.ogg")
        self.confirm_echo_sound = os.path.join(
            self.effects_dir, "confirm_echo.ogg")
        self.back_sound = os.path.join(self.effects_dir, "back.ogg")
        self.back_echo_sound = os.path.join(self.effects_dir, "back_echo.ogg")
        self.error_sound = os.path.join(self.effects_dir, "error.ogg")

    def play_music(self, music_path, time=-1):
        volume = self.overall_volume * self.music_volume
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(time)
        pygame.mixer.music.set_volume(volume)

    def queue_music(self, music_path, time=-1):
        pygame.mixer.music.queue(music_path, "next", time)

    def fadeout_music(self, fadeout_sec):
        pygame.mixer.music.fadeout(int(fadeout_sec * 1000))

    def play_sound(self, sound_path):
        volume = self.overall_volume * self.effect_volume
        sound_effect = pygame.mixer.Sound(sound_path)
        sound_effect.play()
        sound_effect.set_volume(volume)
