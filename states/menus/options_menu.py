import pygame
from states.menus.menu import Menu


class Options(Menu):
    def __init__(self, game) -> None:
        Menu.__init__(self, game)

        # normal options menu
        self.get_setted_value()

        # size, text, color, % canvas width, % canvas height
        self.options = (
            [8, "Fullscreen", "white", .20, .35],
            [7, "Max FPS", "white", .20, .45],
            [7, "Overall volume", "white", .20, .55],
            [7, "Music volume", "white", .20, .65],
            [7, "Effect volume", "white", .20, .75],
        )
        # size, tect, color, % canvas width, % canvas height, num of setable value
        self.setted_value = (
            [8, self.fullscreen, "white", .75, .35, 2],
            [7, self.max_fps, "white", .75, .45, 2],
            [7, self.overall_volume, "white", .75, .55, 11],
            [7, self.music_volume, "white", .75, .65, 11],
            [7, self.effect_volume, "white", .75, .75, 11],
        )

        self.menu_index = 0
        self.CURSOR_OFFSET = -20

        # when select choice to set
        self.is_setting = False
        self.setting_index = 0
        self.SETTING_OFFSET = -40
        self.setable_value = []

    # update game value
    def update(self, delta_time, actions):
        super().update(delta_time, actions)
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
                self.draw.fade_screen("black", 100)
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
            self.game.setting_value["overall_sound"] * 20)
        self.music_volume = int(
            self.game.setting_value["music_sound"] * 10)
        self.effect_volume = int(
            self.game.setting_value["effect_sound"] * 10)

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
                                self.CANVAS_W * option[3], self.CANVAS_H * option[4], 'left')
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
            self.overall_volume_choice(actions)
        elif self.options[self.menu_index][1] == "Music volume":
            self.music_volume_choice(actions)
        elif self.options[self.menu_index][1] == "Effect volume":
            self.effect_volume_choice(actions)

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

    def get_setable_value(self):
        fullscreen_value = ["Off", "On"]
        max_fps_value = [30, 60]
        volume = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        # create fullscreen setting list
        if self.options[self.menu_index][1] == "Fullscreen":
            self.create_setable(fullscreen_value, self.fullscreen)

        # create max fps setting list
        elif self.options[self.menu_index][1] == "Max FPS":
            self.create_setable(max_fps_value, self.max_fps)

        # create overall volume setting list
        elif self.options[self.menu_index][1] == "Overall volume":
            self.create_setable(volume, self.overall_volume)

        # create music volume setting list
        elif self.options[self.menu_index][1] == "Music volume":
            self.create_setable(volume, self.music_volume)

        # create effect volume setting list
        elif self.options[self.menu_index][1] == "Effect volume":
            self.create_setable(volume, self.effect_volume)

    # method to run when fullscreen is selected
    def fullscreen_choice(self, actions):

        # set value by index
        self.fullscreen = self.setable_value[self.setting_index]

        # change game setting value
        if self.fullscreen == "On":
            self.game.setting_value["fullscreen"] = True
        elif self.fullscreen == "Off":
            self.game.setting_value["fullscreen"] = False

        self.game.change_resolution()

        # exit setting
        if actions["enter"] or actions["escape"]:
            self.play_confirm_sound()
            self.is_setting = False

    # method to run when max fps is selected
    def max_fps_choice(self, actions):

        # set value by index
        self.max_fps = self.setable_value[self.setting_index]

        # change game setting value
        for value in self.setable_value:
            if self.max_fps == value:
                self.game.setting_value["max_fps"] = value

        # exit setting
        if actions["enter"] or actions["escape"]:
            self.play_confirm_sound()
            self.is_setting = False

    # method to run when overall volume is selected
    def overall_volume_choice(self, actions):

        # set value by index
        self.overall_volume = self.setable_value[self.setting_index]

        # change game setting value
        for value in self.setable_value:
            if self.overall_volume == value:
                self.game.setting_value["overall_sound"] = value / 20
        self.sound.overall_volume = self.game.setting_value["overall_sound"]
        new_volume = self.sound.overall_volume * self.sound.music_volume
        pygame.mixer.music.set_volume(new_volume)

        # exit setting
        if actions["enter"] or actions["escape"]:
            self.play_confirm_sound()
            self.is_setting = False

    # method to run when music volume is selected
    def music_volume_choice(self, actions):

        # set value by index
        self.music_volume = self.setable_value[self.setting_index]

        # change game setting value
        for value in self.setable_value:
            if self.music_volume == value:
                self.game.setting_value["music_sound"] = value / 10
        self.sound.music_volume = self.game.setting_value["music_sound"]
        new_volume = self.sound.overall_volume * self.sound.music_volume
        pygame.mixer.music.set_volume(new_volume)

        # exit setting
        if actions["enter"] or actions["escape"]:
            self.play_confirm_sound()
            self.is_setting = False

    # method to run when music volume is selected
    def effect_volume_choice(self, actions):

        # set value by index
        self.effect_volume = self.setable_value[self.setting_index]

        # change game setting value
        for value in self.setable_value:
            if self.effect_volume == value:
                self.game.setting_value["effect_sound"] = value / 10

        self.sound.effect_volume = self.game.setting_value["effect_sound"]

        # exit setting
        if actions["enter"] or actions["escape"]:
            self.play_confirm_sound()
            self.is_setting = False
