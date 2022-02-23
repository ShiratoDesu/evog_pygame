from assets.draw import Draw
from states.state import State
from charactor.player import Player
import pygame


class GameScene(State):
    def __init__(self, game) -> None:
        State.__init__(self, game)
        self.player = Player(self.CANVAS_W*0.2, self.CANVAS_H*0.75)
        self.player.add_player()
        self.sound.fadeout_music(1)
        self.sound.play_music(self.sound.begin_theme_intro, 1)
        self.sound.queue_music(self.sound.begin_theme_loop)

    def update(self, delta_time, actions):
        self.start_idle(actions)
        print(self.player.idle_animation)

    def render(self, surface):
        surface.fill((0, 0, 0))
        self.player.draw_sprite(surface)

    def start_idle(self, actions):
        if actions["enter"] == True:
            self.player.idle()
