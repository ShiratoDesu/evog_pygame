from states.state import State


class MainMenu(State):
    def __init__(self, game) -> None:
        State.__init__(self, game)
        # [size, text, position_x_in_screen, offset_y_in_screen]
        self.menus = [[14, "Start", "white", .5, .5],
                      [10, "Options", "white", .5, .65],
                      [10, "Credits", "white", .5, .7],
                      [8, "Exit", "white", .5, .8]]
        self.menu_index = 0
        self.cursor_offset = 50
        self.game.draw_text(self.game.game_canvas, 12, "X", "white", (self.game.GAME_W *
                            self.menus[self.menu_index][3]) - self.cursor_offset, self.game.GAME_H * self.menus[self.menu_index][4])

    def update(self, delta_time, actions):
        self.update_cursor(actions)
        if actions["escape"]:
            self.game.running = False
            self.game.playing = False
        if actions["enter"]:
            self.transition_state()
        self.game.reset_keys()

    def render(self, surface):
        surface.fill((0, 0, 0))
        self.game.draw_text(surface, 17, "EVOG the Adventure",
                            self.game.colors["white"], self.game.GAME_W * .5, self.game.GAME_H * .3)
        self.draw_menu_and_cursor(surface)

    def draw_menu_and_cursor(self, surface):
        # menu here
        for menu in self.menus:
            self.game.draw_text(surface, menu[0], menu[1], self.game.colors[menu[2]],
                                self.game.GAME_W * menu[3], self.game.GAME_H * menu[4])
        # cursor here
        self.game.draw_text(self.game.game_canvas, 12, "X", "white", (self.game.GAME_W *
            self.menus[self.menu_index][3]) - self.cursor_offset, self.game.GAME_H * self.menus[self.menu_index][4])

    # change menu index if press up and down button
    def update_cursor(self, actions):
        if actions["down"]:
            self.menu_index = (self.menu_index + 1) % len(self.menus)
        elif actions["up"]:
            self.menu_index = (self.menu_index - 1) % len(self.menus)

    def transition_state(self):
        if self.menus[self.menu_index][1] == "Start":
            pass
        elif self.menus[self.menu_index][1] == "Options":
            pass
        elif self.menus[self.menu_index][1] == "Credits":
            pass
        elif self.menus[self.menu_index][1] == "Exit":
            self.game.running = False
            self.game.playing = False
