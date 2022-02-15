from states.state import State
import pygame

class GameScene(State):
    def __init__(self, game) -> None:
        State.__init__(self, game)
        self.sound.fadeout_music(1)
        self.sound.play_music(self.sound.begin_theme_intro, 1)
        self.sound.queue_music(self.sound.begin_theme_loop)
        self.sprite = pygame.image.load(self.sprites.mc_sprite)
        self.sprite_rect = self.sprite.get_rect(center = (self.CANVAS_W * 0.25, self.CANVAS_H * 0.75))
    
    def update(self, delta_time, actions):
        pass

    def render(self, surface):
        surface.fill("black")
        surface.blit(self.sprite, self.sprite_rect)