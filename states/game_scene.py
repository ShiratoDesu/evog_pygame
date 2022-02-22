from assets.draw import Draw
from states.state import State
from charactor.player import Player
import pygame

class GameScene(State):
    def __init__(self, game) -> None:
        State.__init__(self, game)
        self.player = Player(self.canvas_w*0.2, self.canvas_h*0.75)
        self.player.add_player()
        self.sound.fadeout_music(1)
        self.sound.play_music(self.sound.begin_theme_intro, self.overall_volume, self.music_volume, 1)
        self.sound.queue_music(self.sound.begin_theme_loop)
        
    def update(self, delta_time, actions):
        pass

    def render(self, surface):
        surface.fill((0, 0, 0))
        self.player.draw_sprite(surface)