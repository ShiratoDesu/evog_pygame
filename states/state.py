from assets.sound import Sound
from assets.draw import Draw
from assets.sprites import Sprites

class State():
    def __init__(self, game) -> None:
        self.game = game
        self.prev_state = None
        self.canvas_w, self.canvas_h = game.GAME_W, game.GAME_H
        self.screen_w, self.screen_h = game.setting_value["SCREEN_W"], game.setting_value["SCREEN_H"]
        self.canvas = game.game_canvas
        self.screen = game.screen
        self.overall_volume = game.setting_value["overall_sound"]
        self.music_volume = game.setting_value["music_sound"]
        self.effect_volume = game.setting_value["effect_sound"]
        self.anti_aliasing_text = game.setting_value["anti_aliasing_text"]

        self.sound = Sound()
        self.draw = Draw()
        self.sprites = Sprites()

    def update(self, delta_time, actions):
        pass

    def render(self, surface):
        pass

    def enter_state(self):
        if len(self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack[-1]
        self.game.state_stack.append(self)

    def exit_state(self):
        self.game.state_stack.pop()