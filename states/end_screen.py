from states.state import State

class EndScreen(State):
    def __init__(self, game, time, count, remaining_health):
        super().__init__(game)
        self.score = 0
        self.count = count
        self.time = int(time)
        self.calculate_score(time, count, remaining_health)
        
    def calculate_score(self, time, count, remaining_health):
        if remaining_health <= 0 and count == 0:
            self.score = 0
        if remaining_health > 0 or count > 0:
            self.score = int((count * 100) + (remaining_health * 10) - (time * 5))
        
        # check high score and save
        if self.score > self.game.setting_value["high_score"]:
            self.game.setting_value["high_score"] = self.score

    def update(self, delta_time, actions):
        super().update(delta_time, actions)
        if actions['enter']:
            while len(self.game.state_stack) > 2:
                self.exit_state()
            self.draw.fade_screen('black')
            self.sound.fadeout_music(1)
            self.sound.play_music(self.sound.title_theme)

    def render(self, surface):
        surface.fill('black')
        self.draw.draw_text_with_outline(12, 'GAME END' , 'pink', self.CANVAS_W/2, self.CANVAS_H*0.2, outline_color= 'red')
        self.draw.draw_text(10, 'Score : ' + str(self.score) , 'green', self.CANVAS_W/2, self.CANVAS_H*0.35)
        self.draw.draw_text(9, 'High score : ' + str(self.game.setting_value["high_score"]), 'yellow', self.CANVAS_W/2, self.CANVAS_H*0.5)
        self.draw.draw_text(8, 'Correct words : ' + str(self.count) , 'white', self.CANVAS_W/2, self.CANVAS_H*0.6)
        self.draw.draw_text(8, 'Time used : ' + str(self.time) + ' s', 'white', self.CANVAS_W/2, self.CANVAS_H*0.7)
        self.draw.draw_text(7, 'Press Enter to main menu' , 'gray', self.CANVAS_W/2, self.CANVAS_H*0.9)