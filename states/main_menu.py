from states.game_scene import GameScene
from states.menu import Menu


class MainMenu(Menu):
    def __init__(self, game) -> None:
        Menu.__init__(self, game)
        # play title bg
        self.game.play_music(self.game.title_theme)
        # [size, text, position_x_in_screen, offset_y_in_screen]
        self.menus = [
            [11, "Start", "gray", .5, .5],
            [8, "Options", "white", .5, .65],
            [8, "Credits", "white", .5, .7],
            [7, "Exit", "white", .5, .8]
        ]
        self.menu_index = 0
        self.cursor_offset = 50

    def update(self, delta_time, actions):
        self.update_cursor(actions)
        if actions["enter"]:
            self.transition_state()
        if actions["escape"]:
            self.play_back_sound()
            self.exit_game()

    def render(self, surface):
        surface.fill("black")
        self.game.draw_text(surface, 12, "EVOG the Adventure",
                            "yellow", self.game.GAME_W * .5, self.game.GAME_H * .3)
        self.draw_menu_and_cursor(surface)

    def draw_menu_and_cursor(self, surface):
        # menu here
        for menu in self.menus:
            self.game.draw_text(surface, menu[0], menu[1], menu[2],
                                self.game.GAME_W * menu[3], self.game.GAME_H * menu[4])
        # cursor here
        self.game.draw_text(self.game.game_canvas, 9, "X", "gray", (self.game.GAME_W *
                            self.menus[self.menu_index][3]) - self.cursor_offset, self.game.GAME_H * self.menus[self.menu_index][4])

    # change menu index if press up and down button
    def update_cursor(self, actions):
        last_index = self.menu_index
        if actions["down"]:
            self.menu_index = (self.menu_index + 1) % len(self.menus)
            self.play_cursor_sound()
        elif actions["up"]:
            self.menu_index = (self.menu_index - 1) % len(self.menus)
            self.play_cursor_sound()
        self.menus[last_index][0] -= 1
        self.menus[last_index][2] = "white"
        self.menus[self.menu_index][0] += 1
        self.menus[self.menu_index][2] = "gray"

    def transition_state(self):
        if self.menus[self.menu_index][1] == "Start":
            self.start_game()
        elif self.menus[self.menu_index][1] == "Options":
            self.play_error_sound()
        elif self.menus[self.menu_index][1] == "Credits":
            self.play_error_sound()
        elif self.menus[self.menu_index][1] == "Exit":
            self.play_confirm_sound()
            self.exit_game()

    def start_game(self):
        self.game.fadeout_music(0.5)
        self.game.play_music(self.game.title_theme_end, 1)
        self.game.game_delay(2)
        new_state = GameScene(self.game)
        self.game.fade_screen("white", 200, new_state)
        new_state.enter_state()

    def exit_game(self):
        if super().check_confirm("Exit?") == True:
            self.game.fadeout_music(0.5)
            self.game.play_sound(self.game.back_echo_sound)
            self.game.game_delay(1)
            self.game.exit_game()