from states.state import State
import pygame

class GameScene(State):
    def __init__(self, game) -> None:
        State.__init__(self, game)
        self.game.fadeout_music(1)
        self.game.play_music(self.game.begin_theme_intro, 1)
        self.game.queue_music(self.game.begin_theme_loop)
        self.sprite = pygame.image.load(self.game.mc_sprite)
        self.sprite_rect = self.sprite.get_rect(center = (self.game.GAME_W / 2, self.game.GAME_H / 2))
    def update(self, delta_time, actions):
        pass

    def render(self, surface):
        surface.fill((0, 0, 0))
        surface.blit(self.sprite, self.sprite_rect)