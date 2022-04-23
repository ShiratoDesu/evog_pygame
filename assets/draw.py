import os
import pygame
from assets.assets import Assets


class Draw(Assets):
    def __init__(self, canvas, screen) -> None:
        Assets.__init__(self)
        self.load_font()
        self.canvas = canvas
        self.screen = screen
        self.canvas_w, self.canvas_h = canvas.get_size()
        self.screen_w, self.screen_h = screen.get_size()
        self.anti_aliasing = False

    def load_font(self, font = "PressStart2P-vaV7.ttf"):
        self.main_font = os.path.join(self.font_dir, font)

    def draw_text(self, size, text, color, x, y, align = 'center'):
        font = pygame.font.Font(self.main_font, size)
        text_surface = font.render(str(text), self.anti_aliasing, color).convert()
        text_rect = text_surface.get_rect()

        if align == 'center':
            text_rect.center = (x, y)
        elif align == 'right':
            text_rect.midright = (x,y)
        elif align == 'left':
            text_rect.midleft = (x, y)
        self.canvas.blit(text_surface, text_rect)
    
    def draw_text_with_outline(self, size, text, color, x, y, align = 'center', outline_color = 'black'):
        self.draw_text(size, text, outline_color, x + 1, y + 1, align)
        self.draw_text(size, text, outline_color, x + 1, y - 1, align)
        self.draw_text(size, text, outline_color, x - 1, y + 1, align)
        self.draw_text(size, text, outline_color, x - 1, y - 1, align)
        self.draw_text(size, text, color, x, y, align)

    def fade_screen(self, color, fade_time=200):
        fade_canvas = pygame.Surface((self.canvas_w, self.canvas_h)).convert_alpha()
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
