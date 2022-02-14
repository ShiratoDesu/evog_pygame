import os
import pygame
from assets.assets import Assets

class Draw(Assets):
    def __init__(self) -> None:
        Assets.__init__(self)
        self.load_font()
    
    def load_font(self):
        self.main_font = os.path.join(self.font_dir, "PressStart2P-vaV7.ttf")

    def draw_text(self, surface, size, text, color, x, y, anti_aliasing=True):
        font = pygame.font.Font(self.main_font, size)
        text_surface = font.render(
            text, anti_aliasing, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)

    def fade_screen(self, color, state, canvas_w, canvas_h, screen_w, screen_h, canvas, screen,fade_time=200):
        fade_canvas = pygame.Surface((canvas_w, canvas_h))
        opacity = 0
        fade_canvas.fill(color)
        for i in range(0, fade_time):
            opacity += 1
            fade_canvas.set_alpha(opacity)
            canvas.blit(fade_canvas, (0, 0))
            screen.blit(pygame.transform.scale(canvas, (screen_w, screen_h)), (0, 0))
            pygame.display.flip()
            pygame.time.delay(5)
        for i in range(0, fade_time):
            opacity -= 1
            fade_canvas.set_alpha(opacity)
            state.render(canvas)
            canvas.blit(fade_canvas, (0, 0))
            screen.blit(pygame.transform.scale(canvas, (screen_w, screen_h)), (0, 0))
            pygame.display.flip()
            pygame.time.delay(5)