import os
import pygame
from assets.assets import Assets


class Draw(Assets):
    def __init__(self, canvas, screen, anti_aliasing) -> None:
        Assets.__init__(self)
        self.load_font()
        self.canvas = canvas
        self.screen = screen
        self.canvas_w, self.canvas_h = canvas.get_size()
        self.screen_w, self.screen_h = screen.get_size()
        self.anti_aliasing = anti_aliasing

    def load_font(self):
        self.main_font = os.path.join(self.font_dir, "PressStart2P-vaV7.ttf")

    def draw_text(self, size, text, color, x, y, center=True):
        font = pygame.font.Font(self.main_font, size)
        text_surface = font.render(str(text), self.anti_aliasing, color)
        text_rect = text_surface.get_rect()
        if center == True:
            text_rect.center = (x, y)
        else:
            text_rect.midleft = (x, y)
        self.canvas.blit(text_surface, text_rect)

    def fade_screen(self, color, state, fade_time=200):
        fade_canvas = pygame.Surface((self.canvas_w, self.canvas_h))
        opacity = 0
        fade_canvas.fill(color)
        for i in range(0, fade_time):
            opacity += 1
            fade_canvas.set_alpha(opacity)
            self.canvas.blit(fade_canvas, (0, 0))
            self.screen.blit(pygame.transform.scale(
                self.canvas, (self.screen_w, self.screen_h)), (0, 0))
            pygame.display.flip()
            pygame.time.delay(5)
        for i in range(0, fade_time):
            opacity -= 1
            fade_canvas.set_alpha(opacity)
            state.render(self.canvas)
            self.canvas.blit(fade_canvas, (0, 0))
            self.screen.blit(pygame.transform.scale(
                self.canvas, (self.screen_w, self.screen_h)), (0, 0))
            pygame.display.flip()
            pygame.time.delay(5)
