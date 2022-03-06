from states.state import State

class EndScreen(State):
    def __init__(self, game, time, count, remaining_health, main_menu):
        super().__init__(game)
        self.score = 0
        self.count = count
        self.time = int(time)
        self.main_menu = main_menu
        self.calculate_score(time, count, remaining_health)
        
    def calculate_score(self, time, count, remaining_health):
        if remaining_health <= 0 and count == 0:
            self.score = 0
        if remaining_health > 0 or count > 0:
            self.score = int((count * 100) + (remaining_health * 10) - (time * 5))

    def update(self, delta_time, actions):
        if actions['enter']:
            while len(self.game.state_stack) > 2:
                self.exit_state()
                self.sound.fadeout_music(1)
            self.draw.fade_screen('black', self.main_menu, 200)

    def render(self, surface):
        surface.fill('black')
        self.draw.draw_text(12, 'GAME END' , 'white', self.CANVAS_W/2, self.CANVAS_H*0.2)
        self.draw.draw_text(10, 'Score : ' + str(self.score) , 'white', self.CANVAS_W/2, self.CANVAS_H*0.5)
        self.draw.draw_text(8, 'Correct words : ' + str(self.count) , 'white', self.CANVAS_W/2, self.CANVAS_H*0.6)
        self.draw.draw_text(8, 'Time used : ' + str(self.time) + ' s', 'white', self.CANVAS_W/2, self.CANVAS_H*0.7)
        self.draw.draw_text(7, 'Press Enter to main menu' , 'white', self.CANVAS_W/2, self.CANVAS_H*0.9)