import os
import sys
import time
import json
import pygame
from states.title import Title

class Game():
    def __init__(self) -> None:

        os.environ['SDL_VIDEO_CENTERED'] = '1'
        # pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.init()
        pygame.display.set_caption("Evog")

        self.setting_value = {
            "fullscreen": False,
            "max_fps": 60,
            "overall_sound": 0.5,
            "music_sound": 1,
            "effect_sound": 1,
            "high_score" : 0
        }
        self.load_saved()

        self.GAME_W, self.GAME_H = 320, 180
        self.DEFAULT_W, self.DEFAULT_H = 1280, 720
        self.canvas = pygame.Surface((self.GAME_W, self.GAME_H))
        if self.setting_value["fullscreen"] == True:
            # monitor = pygame.display.Info()
            # self.SCREEN_W, self.SCREEN_H = monitor.current_w, monitor.current_h
            self.SCREEN_W, self.SCREEN_H = self.DEFAULT_W, self.DEFAULT_H
            self.screen = pygame.display.set_mode(
                (self.SCREEN_W, self.SCREEN_H), pygame.FULLSCREEN)
        else:
            
            self.SCREEN_W, self.SCREEN_H = self.DEFAULT_W, self.DEFAULT_H
            self.screen = pygame.display.set_mode(
                (self.SCREEN_W, self.SCREEN_H))

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
        self.load_states()

        self.user_text = ''

    def game_loop(self):
        while self.playing:
            self.get_dt()
            self.get_events()
            self.update()
            
            self.render()
            self.clock.tick(self.setting_value["max_fps"])

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.actions["escape"] = True
                if event.key == pygame.K_BACKSPACE:
                    self.user_text = self.user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    self.actions["enter"] = True
                else:
                    self.user_text += event.unicode
                    if len(self.user_text) > 13:
                        self.user_text = self.user_text[:-1]
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
        self.state_stack[-1].render(self.canvas)
        self.screen.blit(pygame.transform.scale(
            self.canvas, (self.SCREEN_W, self.SCREEN_H)), (0, 0))
        pygame.display.flip()

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

    def change_resolution(self):
        if self.setting_value["fullscreen"] == True:
            # monitor = pygame.display.Info()
            # self.SCREEN_W, self.SCREEN_H = monitor.current_w, monitor.current_h
            self.SCREEN_W, self.SCREEN_H = self.DEFAULT_W, self.DEFAULT_H
            self.screen = pygame.display.set_mode(
                (self.SCREEN_W, self.SCREEN_H), pygame.FULLSCREEN)
        else:
            self.SCREEN_W, self.SCREEN_H = self.DEFAULT_W, self.DEFAULT_H
            self.screen = pygame.display.set_mode(
                (self.SCREEN_W, self.SCREEN_H))
        self.render()
    
    def reset_user_text(self):
        self.user_text = ''

    def exit_game(self):
        self.save_data()
        pygame.quit()
        sys.exit()

# Data Section

    def load_saved(self):
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


if __name__ == "__main__":
    g = Game()
    while g.running:
        g.game_loop()
