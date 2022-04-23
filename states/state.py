import os
from assets.sound import Sound
from assets.draw import Draw
from assets.sprites import Sprites


class State():
    def __init__(self, game) -> None:
        self.game = game
        self.prev_state = None
        self.CANVAS_W, self.CANVAS_H = game.canvas.get_size()
        self.screen_w, self.screen_h = game.screen.get_size()
        self.canvas = game.canvas
        self.screen = game.screen

        self.sound = Sound(self.game.setting_value["overall_sound"],
                           self.game.setting_value["music_sound"],
                           self.game.setting_value["effect_sound"])
        self.draw = Draw(self.canvas, self.screen)
        self.sprites = Sprites()
        
        self.background_dir = os.path.join(self.draw.assets_dir, 'background')

    def update(self, delta_time, actions):
        self.sound.update_volume(
            self.game.setting_value["overall_sound"], self.game.setting_value["music_sound"], self.game.setting_value["effect_sound"])

    def render(self, surface):
        pass

    def enter_state(self):
        if len(self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack[-1]
        self.game.state_stack.append(self)

    def exit_state(self):
        self.game.state_stack.pop()
