from states.menus.menu import Menu


class Options(Menu):
    def __init__(self, game) -> None:
        Menu.__init__(self, game)

        self.get_setted_value()

        self.options = (
            [7, "Resolution", "white", .20, .35],
            [6, "Anti-Aliasing Text", "white", .20, .45],
            [6, "Max FPS", "white", .20, .55],
            [6, "Overall volume", "white", .20, .65],
            [6, "Music volume", "white", .20, .75],
            [6, "Effect volume", "white", .20, .85]
        )
        self.setted_value = (
            [7, self.resolution, "white", .75, .35],
            [6, self.antialias, "white", .75, .45],
            [6, self.max_fps, "white", .75, .55],
            [6, self.overall_volume, "white", .75, .65],
            [6, self.music_volume, "white", .75, .75],
            [6, self.effect_volume, "white", .75, .85]
        )

        self.menu_index = 0
        self.CURSOR_OFFSET = -20

    def update(self, delta_time, actions):
        self.update_cursor(actions)
        if actions["escape"]:
            self.play_back_sound()
            self.draw.fade_screen("black", self.prev_state, 100)
            self.exit_state()
        if actions["enter"]:
            self.transition_state()

    def render(self, surface):
        surface.fill("black")
        self.draw.draw_text(10, "Options", "green",
                            self.CANVAS_W * .5, self.CANVAS_H * .2)
        self.draw_options()

    # change menu index if press up and down button
    def update_cursor(self, actions):
        last_index = self.menu_index
        if actions["down"]:
            self.menu_index = (self.menu_index + 1) % len(self.options)
            self.play_cursor_sound()
        elif actions["up"]:
            self.menu_index = (self.menu_index - 1) % len(self.options)
            self.play_cursor_sound()
        self.options[last_index][0] -= 1
        self.setted_value[last_index][0] -= 1
        self.options[last_index][2] = "white"
        self.setted_value[last_index][2] = "white"
        self.options[self.menu_index][0] += 1
        self.setted_value[self.menu_index][0] += 1
        self.options[self.menu_index][2] = "gray"
        self.setted_value[self.menu_index][2] = "gray"

    def transition_state(self):
        if self.options[self.menu_index][1] == "Resoulution":
            pass
        elif self.options[self.menu_index][1] == "Anti-Aliasing Text":
            pass
        elif self.options[self.menu_index][1] == "Max FPS":
            pass
        elif self.options[self.menu_index][1] == "Overall volume":
            pass
        elif self.options[self.menu_index][1] == "Music volume":
            pass
        elif self.options[self.menu_index][1] == "Effect volume":
            pass

    def get_setted_value(self):
        self.resolution = str(self.screen_w) + "*" + str(self.screen_h)
        if self.game.setting_value["anti_aliasing_text"] == True:
            self.antialias = "On"
        else:
            self.antialias = "Off"
        self.max_fps = self.game.setting_value["max_fps"]
        self.overall_volume = int(
            (self.game.setting_value["overall_sound"] / 0.5) * 100)
        self.music_volume = int(
            (self.game.setting_value["music_sound"] / 1) * 100)
        self.effect_volume = int(
            (self.game.setting_value["effect_sound"] / 1) * 100)

    def draw_options(self):
        # options choice
        for option in self.options:
            self.draw.draw_text(option[0], option[1], option[2],
                                self.CANVAS_W * option[3], self.CANVAS_H * option[4], False)
        # value of setting
        for value in self.setted_value:
            self.draw.draw_text(
                value[0], value[1], value[2], self.CANVAS_W * value[3], self.CANVAS_H * value[4])
        # setting cursor
        self.draw.draw_text(6, "->", "gray", (self.CANVAS_W *
                            self.options[self.menu_index][3]) + self.CURSOR_OFFSET, self.CANVAS_H * self.options[self.menu_index][4])
