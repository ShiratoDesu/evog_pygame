from states.state import State
from states.main_menu import MainMenu

class Title(State):
    def __init__(self, game) -> None:
        State.__init__(self, game)
        self.game.fade_screen("black", 300, self)

    def update(self, delta_time, actions):
        if actions["enter"]:
            self.game.play_sound(self.game.confirm_echo_sound)
            new_state = MainMenu(self.game)
            self.game.fade_screen("white", 200, new_state)
            new_state.enter_state()
        if actions["escape"]:
            self.game.play_sound(self.game.back_echo_sound)
            self.game.game_delay(1)
            self.game.exit_game()

    def render(self, surface):
        surface.fill(self.game.colors["white"])
        self.game.draw_text(surface, 12, "EVOG the Adventure",
                            "black", self.game.GAME_W * .5, self.game.GAME_H * .45)
        self.game.draw_text(surface, 7, "Enter to start",
                            "black", self.game.GAME_W * .5, self.game.GAME_H * .55)