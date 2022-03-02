from cgitb import text
import imp
from time import time
from assets.draw import Draw
from states.state import State
from charactor.player import Player
from game_sys.word import Word
from game_sys.healthbar import Healthbar
from game_sys.timer import Time
from assets.assets import Assets
import pygame, os


class GameScene(State):
    def __init__(self, game) -> None:
        State.__init__(self, game)
        self.assets = Assets()
        self.player = Player(self.CANVAS_W * 0.2, self.CANVAS_H * 0.75)
        self.word_file = os.path.join(self.assets.words_dir, 'engmix.txt')
        self.word = Word(self.canvas, self.word_file)
        self.heathbar = Healthbar(self.canvas,1000,50)
        self.timer = Time()

        self.player.add_player()
        self.sound.fadeout_music(1)
        self.sound.play_music(self.sound.begin_theme_intro, 1)
        self.sound.queue_music(self.sound.begin_theme_loop)
        self.player_idle = False
        self.word.get_new_word()
        self.timer.setTimeMarker()

    def update(self, delta_time, actions):
        self.player_idle = True
        self.heathbar.advanced_health()
        if actions['enter']:
            if self.game.user_text.lower() == 'gg':
                self.heathbar.take_health(self.heathbar.max_health)

            if self.word.checkWord(self.game.user_text):
                print('TRUE')
                self.word.get_new_word()
                self.timer.getTimeDiff()
                self.timer.setTimeMarker()
                self.heathbar.take_health(100)
            else:
                print('FALSE')
                self.heathbar.take_damage(100)
            self.game.user_text = ''

    def render(self, surface):

        surface.fill((0, 0, 0))
        self.player.draw_sprite(surface, self.player_idle)
        self.word.renderInputBox('white', self.game.user_text)
        surface.blit(self.word.answerMeaning, self.word.meaning_rect)
        # surface.blit(self.word.answer, self.word.answer_rect)
        self.heathbar.update()

