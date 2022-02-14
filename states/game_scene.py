from states.state import State
import pygame

class GameScene(State):
    def __init__(self, game) -> None:
        State.__init__(self, game)
        self.sound.fadeout_music(1)
        self.sound.play_music(self.sound.begin_theme_intro, 1)
        self.sound.queue_music(self.sound.begin_theme_loop)
        self.sprite = pygame.image.load(self.sprites.mc_sprite)
        self.sprite_rect = self.sprite.get_rect(center = (self.canvas_w * 0.25, self.canvas_h * 0.75))
    
    def update(self, delta_time, actions):
        pass

    def render(self, surface):
        surface.fill((0, 0, 0))
        surface.blit(self.sprite, self.sprite_rect)