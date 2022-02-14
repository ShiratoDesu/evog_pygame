from xml.etree.ElementTree import tostring
from states.menu import Menu


class Options(Menu):
    def __init__(self, game) -> None:
        Menu.__init__(self, game)

        self.get_setted_value()

        self.options = (
            [6, "Resolution", "white", .20, .35],
            [6, "Anti-Aliasing Text", "white", .20, .45],
            [6, "Max FPS", "white", .20, .55],
            [6, "Overall volume", "white", .20, .65],
            [6, "Music volume", "white", .20, .75],
            [6, "Effect volume", "white", .20, .85]
        )
        self.setted_value = (
            [6, self.resolution, "white", .75, .35],
            [6, self.antialias, "white", .75, .45],
            [6, self.max_fps, "white", .75, .55],
            [6, self.overall_volume, "white", .75, .65],
            [6, self.music_volume, "white", .75, .75],
            [6, self.effect_volume, "white", .75, .85]
        )

    def update(self, delta_time, actions):
        if actions["escape"]:
            self.play_back_sound()
            self.draw.fade_screen("black", self.prev_state, 50)
            self.exit_state()

    def render(self, surface):
        surface.fill("black")
        self.draw.draw_text(10, "Options", "green",
                            self.canvas_w * .5, self.canvas_h * .2)
        self.draw_options()

    def get_setted_value(self):
        self.resolution = str(self.screen_w) + " x " + str(self.screen_h)
        if self.game.setting_value["anti_aliasing_text"] == True:
            self.antialias = "On"
        else:
            self.antialias = "Off"
        self.max_fps = self.game.setting_value["MAX_FPS"]
        self.overall_volume = int(
            (self.game.setting_value["overall_sound"] / 0.5) * 100)
        self.music_volume = int(
            (self.game.setting_value["music_sound"] / 1) * 100)
        self.effect_volume = int(
            (self.game.setting_value["effect_sound"] / 1) * 100)

    def draw_options(self):
        for option in self.options:
            self.draw.draw_text(option[0], option[1], option[2],
                                self.canvas_w * option[3], self.canvas_h * option[4], False)
        for value in self.setted_value:
            self.draw.draw_text(
                value[0], value[1], value[2], self.canvas_w * value[3], self.canvas_h * value[4])
