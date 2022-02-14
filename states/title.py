from states.state import State
from states.main_menu import MainMenu


class Title(State):
    def __init__(self, game) -> None:
        State.__init__(self, game)
        self.draw.fade_screen("black", self, self.canvas_w, self.canvas_h,
                              self.screen_w, self.screen_h, self.canvas, self.screen)

    def update(self, delta_time, actions):
        if actions["enter"]:
            self.sound.play_sound(
                self.sound.confirm_echo_sound, self.overall_volume, self.effect_volume)
            new_state = MainMenu(self.game)
            self.draw.fade_screen("white", new_state, self.canvas_w, self.canvas_h,
                                  self.screen_w, self.screen_h, self.canvas, self.screen)
            new_state.enter_state()
        if actions["escape"]:
            self.sound.play_sound(self.sound.back_echo_sound,
                                  self.overall_volume, self.effect_volume)
            self.game.game_delay(1)
            self.game.exit_game()

    def render(self, surface):
        surface.fill(self.game.colors["white"])
        self.draw.draw_text(surface, 12, "EVOG the Adventure",
                            "black", self.canvas_w * .5, self.canvas_h * .45, self.anti_aliasing_text)
        self.draw.draw_text(surface, 7, "Enter to start",
                            "black", self.canvas_w * .5, self.canvas_h * .55, self.anti_aliasing_text)
