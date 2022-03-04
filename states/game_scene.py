from states.state import State
from charactor.player import Player
from charactor.demo_monster import DemoMonster
from game_sys.word import Word
from game_sys.healthbar import Healthbar
from game_sys.timer import Time
from assets.assets import Assets
import os


class GameScene(State):
    def __init__(self, game, main_menu) -> None:
        State.__init__(self, game)
        self.assets = Assets()
        self.player = Player(self.CANVAS_W * 0.2, self.CANVAS_H * 0.75)
        self.demo_monster = DemoMonster(self.CANVAS_W * 0.8, self.CANVAS_H * 0.8)
        self.word_file = os.path.join(self.assets.words_dir, 'engmix.txt')
        self.word = Word(self.canvas, self.word_file)
        self.player_hp = Healthbar(self.canvas, self.player.hp, self.player.hp_bar_lenght, 40, 45)
        self.demo_monster_hp = Healthbar(self.canvas, self.demo_monster.hp, self.demo_monster.hp_bar_lenght, 300 - self.demo_monster.hp_bar_lenght,45)
        self.timer = Time()
        self.main_menu = main_menu

        self.player.add_player()
        self.demo_monster.add_monster()
        self.sound.fadeout_music(1)
        self.sound.play_music(self.sound.begin_theme_intro, 1)
        self.sound.queue_music(self.sound.begin_theme_loop)
        self.player_idle = False
        self.demo_idle = False
        self.word.get_new_word()
        self.timer.setTimeMarker()

    def update(self, delta_time, actions):
        self.player_idle = True
        self.demo_idle = True
        self.player_hp.advanced_health()
        self.demo_monster_hp.advanced_health()
        if actions['escape']:
            
            #exit to main menu
            if self.main_menu.check_confirm('Exit to Menu?', 7):
                while len(self.game.state_stack) > 2:
                    self.exit_state()
                    self.sound.fadeout_music(1)
                    self.draw.fade_screen('black', self.main_menu, 100)
                    self.sound.play_music(self.sound.title_theme)
            else:
                self.game.user_text = self.game.user_text[:-1]
        if actions['enter']:
            if self.game.user_text.lower().strip(' ') == 'gg':
                self.player_hp.take_health(self.player_hp.max_health)

            if self.word.checkWord(self.game.user_text):
                self.word.get_new_word()
                self.timer.getTimeDiff()
                self.timer.setTimeMarker()
                self.player_hp.take_health(self.player.heal)
                self.demo_monster_hp.take_damage(self.player.atk)
            else:
                self.player_hp.take_damage(self.demo_monster.atk)
            self.game.user_text = ''
            

    def render(self, surface):

        surface.fill((0, 0, 0))
        self.player.draw_sprite(surface, self.player_idle)
        self.demo_monster.draw_sprite(surface, self.demo_idle)
        self.word.renderInputBox('white', self.game.user_text)
        surface.blit(self.word.answerMeaning, self.word.meaning_rect)
        # surface.blit(self.word.answer, self.word.answer_rect)
        self.demo_monster_hp.update()
        self.player_hp.update()
