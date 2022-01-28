import os
import time
import pygame
from states.title import Title


class Game():
    def __init__(self) -> None:
        pygame.init()
        self.GAME_W, self.GAME_H = 400, 300
        self.SCREEN_W, self.SCREEN_H = 800, 600
        self.game_canvas = pygame.Surface((self.GAME_W, self.GAME_H))
        self.screen = pygame.display.set_mode((self.SCREEN_W, self.SCREEN_H))
        self.running, self.playing = True, True
        self.actions = {"left": False, "right": False, "up": False, "down": False,
                        "enter": False, "escape": False}
        self.colors = {"black": (0, 0, 0), "white": (255, 255, 255)}
        self.dt, self.prev_time = 0, 0
        self.anti_aliasing_text = False
        self.state_stack = []
        self.MAX_FPS = 60
        self.clock = pygame.time.Clock()
        self.load_assets()
        self.load_states()

    def game_loop(self):
        while self.playing:
            self.get_dt()
            self.get_events()
            self.update()
            self.render()
            self.clock.tick(self.MAX_FPS)

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
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

    def render(self):
        self.state_stack[-1].render(self.game_canvas)
        self.screen.blit(pygame.transform.scale(
            self.game_canvas, (self.SCREEN_W, self.SCREEN_H)), (0, 0))
        pygame.display.flip()

    def get_dt(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

    def draw_text(self, surface, size, text, color, x, y):
        font = pygame.font.Font(self.main_font, size)
        text_surface = font.render(text, self.anti_aliasing_text, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)

    def load_assets(self):
        self.assets_dir = os.path.join("assets")
        self.sprites_dir = os.path.join(self.assets_dir, "sprites")
        self.font_dir = os.path.join(self.assets_dir, "font")
        self.main_font = os.path.join(self.font_dir, "PressStart2P-vaV7.ttf")

    def load_states(self):
        self.title_screen = Title(self)
        self.state_stack.append(self.title_screen)

    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False


if __name__ == "__main__":
    g = Game()
    while g.running:
        g.game_loop()
