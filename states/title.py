from states.state import State
from states.main_menu import MainMenu

class Title(State):
    def __init__(self, game) -> None:
        State.__init__(self, game)

    def update(self, delta_time, actions):
        if actions["enter"]:
            new_state = MainMenu(self.game)
            new_state.enter_state()
        if actions["escape"]:
            self.game.running = False
            self.game.playing = False
        self.game.reset_keys()

    def render(self, surface):
        surface.fill(self.game.colors["white"])
        self.game.draw_text(surface, 12, "EVOG the Adventure",
                            self.game.colors["black"], self.game.GAME_W * .5, self.game.GAME_H * .45)
        self.game.draw_text(surface, 7, "Enter to start",
                            self.game.colors["black"], self.game.GAME_W * .5, self.game.GAME_H * .55)