from states.credits import Credits
from states.game_scene import GameScene
from states.menus.menu import Menu
from states.menus.options_menu import Options


class MainMenu(Menu):
    def __init__(self, game) -> None:
        Menu.__init__(self, game)
        # play title bg
        self.sound.play_music(self.sound.title_theme)
        # [size, text, position_x_in_screen, offset_y_in_screen]
        self.menus = (
            [11, "Start", "gray", .5, .5],
            [8, "Options", "white", .5, .65],
            [8, "Credits", "white", .5, .7],
            [7, "Exit", "white", .5, .8]
        )
        self.menu_index = 0
        self.CURSOR_OFFSET = 40

    def update(self, delta_time, actions):
        super().update(delta_time, actions)
        self.update_cursor(actions)
        if actions["enter"]:
            self.transition_state()
        if actions["escape"]:
            self.play_back_sound()
            self.exit_game()

    def render(self, surface):
        surface.fill("black")
        self.draw.draw_text(12, "EVOG the Adventure", "yellow",
                            self.CANVAS_W * .5, self.CANVAS_H * .3)
        self.draw_menu_and_cursor(surface)

    def draw_menu_and_cursor(self, surface):
        # menu here
        for menu in self.menus:
            self.draw.draw_text(menu[0], menu[1], menu[2], self.CANVAS_W *
                                menu[3], self.CANVAS_H * menu[4])
        # cursor here
        self.draw.draw_text(9, ">", "gray", (self.CANVAS_W * self.menus[self.menu_index][3]) -
                            self.CURSOR_OFFSET, self.CANVAS_H * self.menus[self.menu_index][4])
        self.draw.draw_text(9, "<", "gray", (self.CANVAS_W * self.menus[self.menu_index][3]) +
                            self.CURSOR_OFFSET, self.CANVAS_H * self.menus[self.menu_index][4])

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
            self.enter_options_menu()
        elif self.menus[self.menu_index][1] == "Credits":
            self.enter_credits()
        elif self.menus[self.menu_index][1] == "Exit":
            self.play_confirm_sound()
            self.exit_game()

    def start_game(self):
        self.sound.fadeout_music(0.5)
        self.sound.play_music(self.sound.title_theme_end, 1)
        self.game.game_delay(2)
        new_state = GameScene(self.game, self)
        self.game.reset_user_text()
        self.draw.fade_screen("white", new_state)
        new_state.enter_state()
        new_state.timer.reset_start_time()
        new_state.timer.reset_last_ticks()

    def enter_options_menu(self):
        self.play_confirm_sound()
        new_state = Options(self.game)
        self.draw.fade_screen("black", new_state, 100)
        new_state.enter_state()
    
    def enter_credits(self):
        self.play_confirm_sound()
        new_state = Credits(self.game)
        self.draw.fade_screen('black', new_state, 100)
        new_state.enter_state()

    def exit_game(self):
        if super().check_confirm("Exit?") == True:
            self.sound.fadeout_music(0.5)
            self.sound.play_sound(self.sound.back_echo_sound)
            self.game.game_delay(1)
            self.game.exit_game()
