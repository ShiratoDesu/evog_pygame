import os
import sys
import time
import json
import pygame
from states.title import Title


class Game():
    def __init__(self) -> None:
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.init()
        self.setting_value = {
            "SCREEN_W": 1280,
            "SCREEN_H": 720,
            "anti_aliasing_text": False,
            "MAX_FPS": 60,
            "overall_sound": 1,
            "music_sound": 1,
            "effect_sound": 1
        }
        self.GAME_W, self.GAME_H = 320, 180
        self.game_canvas = pygame.Surface((self.GAME_W, self.GAME_H))
        self.screen = pygame.display.set_mode(
            (self.setting_value["SCREEN_W"], self.setting_value["SCREEN_H"]))
        self.running, self.playing = True, True
        self.actions = {
            "left": False,
            "right": False,
            "up": False,
            "down": False,
            "enter": False,
            "escape": False
        }
        self.colors = {
            "black": (0, 0, 0),
            "white": (255, 255, 255),
            "red": (255, 0, 0),
            "yellow": (255, 255, 0)
        }
        self.dt, self.prev_time = 0, 0
        self.state_stack = []
        self.clock = pygame.time.Clock()
        self.load_assets()
        self.load_states()

    def game_loop(self):
        while self.playing:
            self.get_dt()
            self.get_events()
            self.update()
            self.render()
            pygame.display.flip()
            self.clock.tick(self.setting_value["MAX_FPS"])

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.actions["escape"] = True
                if event.key == pygame.K_RETURN:
                    self.actions["enter"] = True
                if event.key == pygame.K_UP:
                    self.actions["up"] = True
                if event.key == pygame.K_DOWN:
                    self.actions["down"] = True
                if event.key == pygame.K_LEFT:
                    self.actions["left"] = True
                if event.key == pygame.K_RIGHT:
                    self.actions["right"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.actions["escape"] = False
                if event.key == pygame.K_RETURN:
                    self.actions["enter"] = False
                if event.key == pygame.K_UP:
                    self.actions["up"] = False
                if event.key == pygame.K_DOWN:
                    self.actions["down"] = False
                if event.key == pygame.K_LEFT:
                    self.actions["left"] = False
                if event.key == pygame.K_RIGHT:
                    self.actions["right"] = False

    def update(self):
        self.state_stack[-1].update(self.dt, self.actions)
        self.reset_keys()

    def render(self):
        self.state_stack[-1].render(self.game_canvas)
        self.screen.blit(pygame.transform.scale(
            self.game_canvas, (self.setting_value["SCREEN_W"], self.setting_value["SCREEN_H"])), (0, 0))

# Game Section

    def get_dt(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False

    def game_delay(self, delay_sec):
        pygame.time.delay(delay_sec * 1000)

    def exit_game(self):
        self.save_data()
        pygame.quit()
        sys.exit()

# Data Section

    def load_assets(self):
        # assets folder
        self.assets_dir = os.path.join("assets")
        self.charractor_dir = os.path.join(self.assets_dir, "charactor")
        self.sprites_dir = os.path.join(self.assets_dir, "sprites")
        self.font_dir = os.path.join(self.assets_dir, "font")
        self.sounds_dir = os.path.join(self.assets_dir, "sounds")

        # assets/font folder
        self.main_font = os.path.join(self.font_dir, "PressStart2P-vaV7.ttf")

        # assets/charactor
        self.mc_sprite = os.path.join(self.charractor_dir, "main_design.png")

        # assets/sounds
        self.bg_musics_dir = os.path.join(self.sounds_dir, "bg_musics")
        self.effects_dir = os.path.join(self.sounds_dir, "effects")

        # assets/sounds/bg_musics
        self.title_theme = os.path.join(self.bg_musics_dir, "TitleTheme.wav")
        self.title_theme_end = os.path.join(self.bg_musics_dir, "TitleThemeEnd.wav")
        self.begin_theme_intro = os.path.join(self.bg_musics_dir, "JourneyBeginsIntro.wav")
        self.begin_theme_loop = os.path.join(self.bg_musics_dir, "JourneyBeginsLoop.wav")
        self.begin_theme_end = os.path.join(self.bg_musics_dir, "JourneyBeginsEnd.wav")

        # assets/sounds/effects
        self.cursor_sound = os.path.join(self.effects_dir, "cursor.ogg")
        self.confirm_sound = os.path.join(self.effects_dir, "confirm.ogg")
        self.confirm_echo_sound = os.path.join(self.effects_dir, "confirm_echo.ogg")
        self.back_sound = os.path.join(self.effects_dir, "back.ogg")
        self.back_echo_sound = os.path.join(self.effects_dir, "back_echo.ogg")
        self.error_sound = os.path.join(self.effects_dir, "error.ogg")

        # saved folder
        self.saved_dir = os.path.join("saved")
        try:
            self.saved_setting = os.path.join(self.saved_dir, "setting.txt")
            with open(self.saved_setting) as setting_file:
                self.setting_value = json.load(setting_file)
        except:
            pass

    def load_states(self):
        self.title_screen = Title(self)
        self.state_stack.append(self.title_screen)

    def save_data(self):
        with open(self.saved_setting, "w") as setting_file:
            json.dump(self.setting_value, setting_file)

# Screen Section

    def draw_text(self, surface, size, text, color, x, y):
        font = pygame.font.Font(self.main_font, size)
        text_surface = font.render(
            text, self.setting_value["anti_aliasing_text"], color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)

    def fade_screen(self, color, fade_time, state):
        fade_canvas = pygame.Surface((self.GAME_W, self.GAME_H))
        opacity = 0
        fade_canvas.fill(color)
        for i in range(0, fade_time):
            opacity += 1
            fade_canvas.set_alpha(opacity)
            self.game_canvas.blit(fade_canvas, (0,0))
            self.screen.blit(pygame.transform.scale(
                self.game_canvas, (self.setting_value["SCREEN_W"], self.setting_value["SCREEN_H"])), (0, 0))        
            pygame.display.flip()
            pygame.time.delay(5)
        for i in range(0,fade_time):
            opacity -= 1
            fade_canvas.set_alpha(opacity)
            state.render(self.game_canvas)
            self.game_canvas.blit(fade_canvas, (0,0))
            self.screen.blit(pygame.transform.scale(
                self.game_canvas, (self.setting_value["SCREEN_W"], self.setting_value["SCREEN_H"])), (0, 0))        
            pygame.display.flip()
            pygame.time.delay(5)      

# Music and Sound Section

    def play_music(self, music_path, time = -1):
        music_volume = (
            self.setting_value["overall_sound"] * self.setting_value["music_sound"])
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(time)
        pygame.mixer.music.set_volume(music_volume)

    def queue_music(self, music_path, time = -1):
        pygame.mixer.music.queue(music_path, "next", time)

    def fadeout_music(self, fadeout_sec):
        pygame.mixer.music.fadeout(int(fadeout_sec * 1000))

    def play_sound(self, sound_path):
        effect_volume = self.setting_value["overall_sound"] * \
            self.setting_value["effect_sound"]
        sound_effect = pygame.mixer.Sound(sound_path)
        sound_effect.play()
        sound_effect.set_volume(effect_volume)


if __name__ == "__main__":
    g = Game()
    while g.running:
        g.game_loop()
