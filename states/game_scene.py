from hashlib import new
from states.state import State
from charactor.player import Player
from charactor.demo_monster import DemoMonster
from game_sys.word import Word
from game_sys.healthbar import Healthbar
from game_sys.timer import Time
from assets.assets import Assets
from states.end_screen import EndScreen
import os
import time


class GameScene(State):
    def __init__(self, game, main_menu) -> None:
        State.__init__(self, game)
        self.assets = Assets()
        self.player = Player(self.CANVAS_W * 0.2, self.CANVAS_H * 0.75)
        self.demo_monster = DemoMonster(
            self.CANVAS_W * 0.8, self.CANVAS_H * 0.8)
        self.word_file = os.path.join(self.assets.words_dir, 'engmix.txt')
        self.word = Word(self.canvas, self.word_file)
        self.player_hp = Healthbar(
            self.canvas, self.player.hp, self.player.hp_bar_lenght, 20, 45)
        self.demo_monster_hp = Healthbar(
            self.canvas, self.demo_monster.hp, self.demo_monster.hp_bar_lenght, 300 - self.demo_monster.hp_bar_lenght, 45)
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
        self.timer.reset_start_time()

    def update(self, delta_time, actions):
        self.player_idle = True
        self.demo_idle = True
        self.player_hp.advanced_health()
        self.demo_monster_hp.advanced_health()
        self.timer.get_elapsed_time()
        if actions['escape']:
            start_pause = time.time()

            # exit to main menu
            if self.main_menu.check_confirm('Exit to Menu?', 7):
                while len(self.game.state_stack) > 2:
                    self.exit_state()
                    self.sound.fadeout_music(1)
                    self.draw.fade_screen('black', self.main_menu, 100)
                    self.sound.play_music(self.sound.title_theme)
            else:
                self.game.user_text = self.game.user_text[:-1]
                pause_time = time.time() - start_pause
                self.timer.start_time += pause_time
        if actions['enter']:
            if self.game.user_text.lower().strip() == 'gg':
                self.player_hp.take_health(self.player_hp.max_health)

            if self.word.checkWord(self.game.user_text):
                self.word.get_new_word()
                self.player_hp.take_health(self.player.heal)
                self.demo_monster_hp.take_damage(self.player.atk)

            else:
                self.player_hp.take_damage(self.demo_monster.atk)
            self.game.user_text = ''
        self.pause_time = 0

        if self.timer.get_time_diff(5000):
                self.player_hp.take_damage(self.demo_monster.atk)
        
        if self.player_hp.current_health <= 0 or self.demo_monster_hp.current_health <= 0:
            new_state = EndScreen(self.game, self.timer.elasped_time, self.word.word_correct_count, self.player_hp.current_health, self.main_menu)
            new_state.enter_state()
            
    def render(self, surface):

        surface.fill((0, 0, 0))
        self.player.draw_sprite(surface, self.player_idle)
        self.demo_monster.draw_sprite(surface, self.demo_idle)
        self.word.renderInputBox('white', self.game.user_text)
        surface.blit(self.word.answerMeaning, self.word.meaning_rect)
        # surface.blit(self.word.answer, self.word.answer_rect)
        self.demo_monster_hp.update()
        self.player_hp.update()
        self.showName()

        # render time count
        self.draw.draw_text(6, int(self.timer.elasped_time), 'white', self.CANVAS_W * 0.5, self.CANVAS_H * 0.1)

    def showName(self):
        self.draw.draw_text(8, self.player.name, 'white', 45, 37)
        self.draw.draw_text(8, self.demo_monster.name, 'white', 300, 37, False, True)

