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
            [6, "Max FPS", "white", .20, .45],
            [6, "Overall volume", "white", .20, .55],
            [6, "Music volume", "white", .20, .65],
            [6, "Effect volume", "white", .20, .75],
        )
        # size, tect, color, % canvas width, % canvas height, num of setable value
        self.setted_value = (
            [7, self.fullscreen, "white", .75, .35, 2],
            [6, self.max_fps, "white", .75, .45, 3],
            [6, self.overall_volume, "white", .75, .55, 2],
            [6, self.music_volume, "white", .75, .65, 5],
            [6, self.effect_volume, "white", .75, .75, 5],
        )

        self.menu_index = 0
        self.CURSOR_OFFSET = -20

        # when select choice to set
        self.is_setting = False
        self.setting_index = 0
        self.last_setting_index = 0
        self.SETTING_OFFSET = -40
        self.setable_value = []

    # update game value
    def update(self, delta_time, actions):
        self.update_setted_value()

        # when select choice to set
        if self.is_setting:
            self.run_setting_by_index(actions)
            self.move_setting_cursor(actions)

        # when normal options menu
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

    # render image to screen
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

    # get value from game dict and assign to variable
    def get_setted_value(self):
        if self.game.setting_value["fullscreen"] == True:
            self.fullscreen = "On"
        else:
            self.fullscreen = "Off"
        self.max_fps = self.game.setting_value["max_fps"]
        self.overall_volume = int(
            self.game.setting_value["overall_sound"] * 10)
        self.music_volume = int(
            (self.game.setting_value["music_sound"] / 1) * 5)
        self.effect_volume = int(
            (self.game.setting_value["effect_sound"] / 1) * 5)

    # assign value of variable to setted_value list
    def update_setted_value(self):
        self.setted_value[0][1] = self.fullscreen
        self.setted_value[1][1] = self.max_fps
        self.setted_value[2][1] = self.overall_volume
        self.setted_value[3][1] = self.music_volume
        self.setted_value[4][1] = self.effect_volume

    # draw each value and option setting
    def draw_options(self):
        # options choice
        for option in self.options:
            self.draw.draw_text(option[0], option[1], option[2],
                                self.CANVAS_W * option[3], self.CANVAS_H * option[4], False)
        # value of setting
        for value in self.setted_value:
            self.draw.draw_text(
                value[0], value[1], value[2], self.CANVAS_W * value[3], self.CANVAS_H * value[4])

    # draw cursor that point to options setting
    def draw_options_cursor(self):
        # setting cursor
        self.draw.draw_text(6, "->", "gray", (self.CANVAS_W *
                            self.options[self.menu_index][3]) + self.CURSOR_OFFSET, self.CANVAS_H * self.options[self.menu_index][4])

    # run setting method base on menu_index
    def run_setting_by_index(self, actions):
        if self.options[self.menu_index][1] == "Fullscreen":
            self.fullscreen_choice(actions)
        elif self.options[self.menu_index][1] == "Max FPS":
            self.max_fps_choice(actions)
        elif self.options[self.menu_index][1] == "Overall volume":
            pass
        elif self.options[self.menu_index][1] == "Music volume":
            pass
        elif self.options[self.menu_index][1] == "Effect volume":
            pass

    # draw setting options when selected
    def draw_setting(self):
        self.options[self.menu_index][2] = "yellow"
        self.setted_value[self.menu_index][2] = "yellow"
        self.draw.draw_text(6, "<", "yellow", (self.CANVAS_W *
                            self.setted_value[self.menu_index][3]) + self.SETTING_OFFSET, self.CANVAS_H * self.setted_value[self.menu_index][4])
        self.draw.draw_text(6, ">", "yellow", (self.CANVAS_W *
                            self.setted_value[self.menu_index][3]) - self.SETTING_OFFSET, self.CANVAS_H * self.setted_value[self.menu_index][4])

    # move setting options cursor when selected
    def move_setting_cursor(self, actions):
        if actions["right"]:
            if self.setting_index != (self.setted_value[self.menu_index][5] - 1):
                self.setting_index = self.setting_index + 1
                self.play_cursor_sound()
            else:
                self.play_error_sound()
        if actions["left"]:
            if self.setting_index != 0:
                self.setting_index = self.setting_index - 1
                self.play_cursor_sound()
            else:
                self.play_error_sound()

    # create list of each setting in options and set last index
    def create_setable(self, list, current_value):
        self.setable_value.clear()
        for value in list:
            self.setable_value.append(value)
            if value == current_value:
                self.setting_index = list.index(value)
        self.last_setting_index = self.setting_index

    def get_setable_value(self):
        fullscreen_value = ["Off", "On"]
        max_fps_value = [30, 60]

        # create fullscreen setting list
        if self.options[self.menu_index][1] == "Fullscreen":
            self.create_setable(fullscreen_value, self.fullscreen)

        # create max fps setting list
        elif self.options[self.menu_index][1] == "Max FPS":
            self.create_setable(max_fps_value, self.max_fps)

    # method to run when fullscreen is selected
    def fullscreen_choice(self, actions):

        # get last value before changed
        last_setting = self.setable_value[self.last_setting_index]

        # set value to draw
        self.fullscreen = self.setable_value[self.setting_index]

        # if player press enter to change value that not last value
        if actions["enter"] & (self.fullscreen != last_setting):
            self.play_confirm_sound()
            if self.fullscreen == "On":
                self.game.setting_value["fullscreen"] = True
            elif self.fullscreen == "Off":
                self.game.setting_value["fullscreen"] = False

            self.game.change_resolution()
            self.is_setting = False

        # if player press escape while setting
        if actions["escape"]:
            self.play_back_sound()
            if self.check_confirm("Discard change?", 6):
                self.fullscreen = last_setting
                self.is_setting = False

    # method to run when max fps is selected
    def max_fps_choice(self, actions):

        # get last value before changed
        last_setting = self.setable_value[self.last_setting_index]

        # set value
        self.max_fps = self.setable_value[self.setting_index]

        # if player press enter to change value that not last value
        if actions["enter"] & (self.max_fps != last_setting):
            self.play_confirm_sound()
            last_value = self.game.setting_value["max_fps"]
            if self.max_fps == 30:
                self.game.setting_value["max_fps"] = 30
            elif self.max_fps == 60:
                self.game.setting_value["max_fps"] = 60

            # ask player to keep change and do below if player not keep
            if self.check_confirm("Keep change?", 6) != True:
                self.game.setting_value["max_fps"] = last_value
                self.max_fps = last_setting
            self.is_setting = False

        # if player press escape while setting
        if actions["escape"]:
            self.play_back_sound()
            if self.check_confirm("Discard change?", 6):
                self.max_fps = last_setting
                self.is_setting = False
