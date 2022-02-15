from states.state import State
from states.menus.main_menu import MainMenu


class Title(State):
    def __init__(self, game) -> None:
        State.__init__(self, game)
        self.draw.fade_screen("black", self)

    def update(self, delta_time, actions):
        if actions["enter"]:
            self.sound.play_sound(self.sound.confirm_echo_sound)
            new_state = MainMenu(self.game)
            self.draw.fade_screen("white", new_state)
            new_state.enter_state()
        if actions["escape"]:
            self.sound.play_sound(self.sound.back_echo_sound)
            self.game.game_delay(1)
            self.game.exit_game()

    def render(self, surface):
        surface.fill("white")
        self.draw.draw_text(12, "EVOG the Adventure",
                            "black", self.CANVAS_W * .5, self.CANVAS_H * .45)
        self.draw.draw_text(7, "Enter to start",
                            "black", self.CANVAS_W * .5, self.CANVAS_H * .55)
