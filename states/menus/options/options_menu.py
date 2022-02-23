import pygame
from states.menus.menu import Menu


class Options(Menu):
    def __init__(self, game) -> None:
        Menu.__init__(self, game)

        # normal options menu
        self.get_setted_value()

        # size, text, color, % canvas width, % canvas height
        self.options = (
            [7, "Fullscreen", "white", .20, .35],
            [6, "Resolution", "white", .20, .45],
            [6, "Max FPS", "white", .20, .55],
            [6, "Overall volume", "white", .20, .65],
            [6, "Music volume", "white", .20, .75],
            [6, "Effect volume", "white", .20, .85]
        )
        # size, tect, color, % canvas width, % canvas height, num of setable value
        self.setted_value = (
            [7, self.fullscreen, "white", .75, .35, 2],
            [6, self.resolution, "white", .75, .45, 3],
            [6, self.max_fps, "white", .75, .55, 2],
            [6, self.overall_volume, "white", .75, .65, 5],
            [6, self.music_volume, "white", .75, .75, 5],
            [6, self.effect_volume, "white", .75, .85, 5]
        )

        self.menu_index = 0
        self.CURSOR_OFFSET = -20

        # when select choice to set
        self.is_setting = False
        self.setting_index = 0
        self.SETTING_OFFSET = -40
        self.setable_value = []

    def update(self, delta_time, actions):
        self.update_setted_value()

        # when select choice to set
        if self.is_setting:
            self.check_menu_index(actions)
            self.move_setting_cursor(actions)

        # normal options menu
        else:
            self.update_cursor(actions)
            if actions["escape"]:
                self.play_back_sound()
                self.draw.fade_screen("black", self.prev_state, 100)
                self.exit_state()
            if actions["enter"]:
                self.play_confirm_sound()
                self.is_setting = True
                self.get_setable_value()

    def render(self, surface):
        surface.fill("black")
        self.draw.draw_text(10, "Options", "green",
                            self.CANVAS_W * .5, self.CANVAS_H * .2)
        self.draw_options()
        if self.is_setting:
            self.draw_setting()
        else:
            self.draw_options_cursor()

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

    def get_setted_value(self):
        if self.game.setting_value["fullscreen"] == True:
            self.fullscreen = "On"
        else:
            self.fullscreen = "Off"
        self.resolution = str(self.screen_w) + "*" + str(self.screen_h)
        self.max_fps = self.game.setting_value["max_fps"]
        self.overall_volume = int(
            self.game.setting_value["overall_sound"] * 10)
        self.music_volume = int(
            (self.game.setting_value["music_sound"] / 1) * 5)
        self.effect_volume = int(
            (self.game.setting_value["effect_sound"] / 1) * 5)

    def update_setted_value(self):
        self.setted_value[0][1] = self.fullscreen
        self.setted_value[1][1] = self.resolution
        self.setted_value[2][1] = self.max_fps
        self.setted_value[3][1] = self.overall_volume
        self.setted_value[4][1] = self.music_volume
        self.setted_value[5][1] = self.effect_volume

    def draw_options(self):
        # options choice
        for option in self.options:
            self.draw.draw_text(option[0], option[1], option[2],
                                self.CANVAS_W * option[3], self.CANVAS_H * option[4], False)
        # value of setting
        for value in self.setted_value:
            self.draw.draw_text(
                value[0], value[1], value[2], self.CANVAS_W * value[3], self.CANVAS_H * value[4])

    def draw_options_cursor(self):
        # setting cursor
        self.draw.draw_text(6, "->", "gray", (self.CANVAS_W *
                            self.options[self.menu_index][3]) + self.CURSOR_OFFSET, self.CANVAS_H * self.options[self.menu_index][4])

    def check_menu_index(self, actions):
        if self.options[self.menu_index][1] == "Fullscreen":
            self.fullscreen_choice(actions)

    def draw_setting(self):
        self.options[self.menu_index][2] = "yellow"
        self.setted_value[self.menu_index][2] = "yellow"
        self.draw.draw_text(6, "<", "yellow", (self.CANVAS_W *
                            self.setted_value[self.menu_index][3]) + self.SETTING_OFFSET, self.CANVAS_H * self.setted_value[self.menu_index][4])
        self.draw.draw_text(6, ">", "yellow", (self.CANVAS_W *
                            self.setted_value[self.menu_index][3]) - self.SETTING_OFFSET, self.CANVAS_H * self.setted_value[self.menu_index][4])

    def move_setting_cursor(self, actions):
        if actions["right"]:
            if self.setting_index != (self.setted_value[self.menu_index][5] - 1):
                self.setting_index = self.setting_index + 1
                self.play_cursor_sound()
            else:
                self.play_error_sound()
        elif actions["left"]:
            if self.setting_index != 0:
                self.setting_index = self.setting_index - 1
                self.play_cursor_sound()
            else:
                self.play_error_sound()

    def get_setable_value(self):
        self.setable_value.clear()
        fullscreen_value = ["On", "Off"]
        if self.options[self.menu_index][1] == "Fullscreen":
            self.setable_value.append(self.fullscreen)
            for value in fullscreen_value:
                if value not in self.setable_value:
                    self.setable_value.append(value)

    def fullscreen_choice(self, actions):
        last_setting = self.setable_value[0]
        self.fullscreen = self.setable_value[self.setting_index]
        if actions["enter"] & (self.fullscreen != last_setting):
            self.play_confirm_sound()
            last_value = self.game.setting_value["fullscreen"]
            if self.fullscreen == "On":
                pygame.display.toggle_fullscreen()
                self.game.setting_value["fullscreen"] = True
            elif self.fullscreen == "Off":
                pygame.display.toggle_fullscreen()
                self.game.setting_value["fullscreen"] = False
            if self.check_confirm("Save change?", 6) != True:
                pygame.display.toggle_fullscreen()
                self.fullscreen = last_setting
                self.setted_value[0][1] = last_value
            self.setting_index = 0
            self.is_setting = False
        if actions["escape"]:
            self.play_back_sound()
            if self.check_confirm("Discard change?", 6):
                self.fullscreen = last_setting
                self.setted_value[0][1] = last_setting
                self.setting_index = 0
                self.is_setting = False
