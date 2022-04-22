import pygame
from states.state import State


class Credits(State):
    def __init__(self, game) -> None:
        State.__init__(self, game)

        self.sound.change_music(self.sound.the_final_of_the_fantasy, 1)

    def update(self, delta_time, actions):
        super().update(delta_time, actions)
        
        # check if player press enter or escape, exit credits screne
        if actions['enter'] or actions['escape']:
            self.sound.play_sound(self.sound.back_echo_sound)
            self.sound.change_music(self.sound.title_theme, 1)
            self.draw.fade_screen("black", self.prev_state, 100)
            self.exit_state()
    
    def render(self, surface):
        surface.fill('black')
        self.draw.load_font()
        self.draw.draw_text(10, 'Credits', 'yellow', self.CANVAS_W * 0.5, self.CANVAS_H * 0.1)
        
        # developer list 
        self.draw.draw_text(8, 'Developer :', 'yellow', self.CANVAS_W * 0.05, self.CANVAS_H * 0.2, center = False)
        self.draw.draw_text(8, 'Sirawit Pawano', 'white', self.CANVAS_W * 0.1, self.CANVAS_H * 0.275, center = False)
        self.draw.draw_text(8, 'Yannawat Somon', 'white', self.CANVAS_W * 0.1, self.CANVAS_H * 0.325, center = False)

        # musics credit
        self.draw.draw_text(8, 'Musics by :', 'yellow', self.CANVAS_W * 0.05, self.CANVAS_H * 0.5, center = False)
        self.draw.draw_text(8, 'xDeviruchi', 'white', self.CANVAS_W * 0.1, self.CANVAS_H * 0.575, center = False)
        self.draw.draw_text(8, 'MrTrololow', 'white', self.CANVAS_W * 0.1, self.CANVAS_H * 0.625, center = False)

        # sound fx credit
        self.draw.draw_text(8, 'Sound FX by :', 'yellow', self.CANVAS_W * 0.475, self.CANVAS_H * 0.2, center = False)
        self.draw.draw_text(8, 'ObsydianX', 'white', self.CANVAS_W * 0.525, self.CANVAS_H * 0.275, center = False)
        self.draw.draw_text(8, 'lulyc', 'white', self.CANVAS_W * 0.525, self.CANVAS_H * 0.325, center = False)
        self.draw.draw_text(8, 'Mixkit', 'white', self.CANVAS_W * 0.525, self.CANVAS_H * 0.375, center = False)
        self.draw.draw_text(6, 'LittleRobotSoundFactory', 'white', self.CANVAS_W * 0.525, self.CANVAS_H * 0.425, center = False)

        # adviser list
        self.draw.draw_text(8, 'Adviser :', 'yellow', self.CANVAS_W * 0.05, self.CANVAS_H * 0.8, center = False)
        self.draw.draw_text(7, 'Asst. Prof. Dr.Pattarawit Polpinit', 'white', self.CANVAS_W * 0.07, self.CANVAS_H * 0.87, center = False)
        self.draw.draw_text(7, 'Assoc. Prof. Dr.Kanda Runapongsa Saikaew', 'white', self.CANVAS_W * 0.07, self.CANVAS_H * 0.92, center = False)
