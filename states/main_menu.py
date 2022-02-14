from states.game_scene import GameScene
from states.menu import Menu


class MainMenu(Menu):
    def __init__(self, game) -> None:
        Menu.__init__(self, game)
        # play title bg
        self.sound.play_music(self.sound.title_theme,
                              self.overall_volume, self.music_volume)
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
        self.draw.draw_text(surface, 12, "EVOG the Adventure",
                            "yellow", self.canvas_w * .5, self.canvas_h * .3, self.anti_aliasing_text)
        self.draw_menu_and_cursor(surface)

    def draw_menu_and_cursor(self, surface):
        # menu here
        for menu in self.menus:
            self.draw.draw_text(surface, menu[0], menu[1], menu[2],
                                self.canvas_w * menu[3], self.canvas_h * menu[4], self.anti_aliasing_text)
        # cursor here
        self.draw.draw_text(self.game.game_canvas, 9, "X", "gray", (self.canvas_w *
                            self.menus[self.menu_index][3]) - self.cursor_offset, self.canvas_h * self.menus[self.menu_index][4], self.anti_aliasing_text)

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
        self.sound.fadeout_music(0.5)
        self.sound.play_music(self.sound.title_theme_end,
                              self.overall_volume, self.music_volume, 1)
        self.game.game_delay(2)
        new_state = GameScene(self.game)
        self.draw.fade_screen("white", new_state, self.canvas_w, self.canvas_h,
                              self.screen_w, self.screen_h, self.canvas, self.screen)
        new_state.enter_state()

    def exit_game(self):
        if super().check_confirm("Exit?") == True:
            self.sound.fadeout_music(0.5)
            self.sound.play_sound(self.sound.back_echo_sound,
                                  self.overall_volume, self.effect_volume)
            self.game.game_delay(1)
            self.game.exit_game()
