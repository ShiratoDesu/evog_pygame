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
        self.draw.draw_text(10, 'Credits', 'white', self.CANVAS_W * 0.5, self.CANVAS_H * 0.1)
