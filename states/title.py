from states.state import State
from states.menus.main_menu import MainMenu
from game_sys.timer import Time


class Title(State):
    def __init__(self, game) -> None:
        State.__init__(self, game)
        self.timer = Time()
        self.draw.fade_screen("black")
        self.timer.reset_last_ticks()

    def update(self, delta_time, actions):
        super().update(delta_time, actions)
        if self.timer.get_time_diff(1000):
            new_state = MainMenu(self.game)
            self.draw.fade_screen("white")
            new_state.enter_state()
        # if actions["enter"]:
        #     self.sound.play_sound(self.sound.confirm_echo_sound)
        #     new_state = MainMenu(self.game)
        #     self.draw.fade_screen("white", new_state)
        #     new_state.enter_state()
        # if actions["escape"]:
        #     self.sound.play_sound(self.sound.back_echo_sound)
        #     self.game.game_delay(1)
        #     self.game.exit_game()

    def render(self, surface):
        surface.fill("white")
        self.draw.draw_text(12, "KKU AdvanceCom Project",
                            "black", self.CANVAS_W * .5, self.CANVAS_H * .45)
        self.draw.draw_text(8, "ACP2021-19",
                            "black", self.CANVAS_W * .5, self.CANVAS_H * .55)
