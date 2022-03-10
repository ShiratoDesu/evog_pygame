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
import random


class GameScene(State):
    def __init__(self, game, main_menu) -> None:
        State.__init__(self, game)
        self.assets = Assets()
        
        # player and monster object
        self.player = Player(self.CANVAS_W * 0.2, self.CANVAS_H * 0.75)
        self.monster_list = [ DemoMonster(self.CANVAS_W * 0.8, self.CANVAS_H * 0.8 ) ]      

        # random monster from monster list
        random.seed(time.time())
        self.monster = random.choice(self.monster_list)

        # set player and monster hp bar
        self.player_hp = Healthbar(self.canvas, self.player.hp, self.player.hp_bar_lenght, 20, 45)
        self.monster_hp = Healthbar(self.canvas, self.monster.hp, self.monster.hp_bar_lenght, 300 - self.monster.hp_bar_lenght, 45)

        # add player and monster to screen and set idle animation
        self.player.add_player()
        self.monster.add_monster()
        self.player_idle = False
        self.monster_idle = False

        # get first word and answer
        self.word_file = os.path.join(self.assets.words_dir, 'engmix.txt')
        self.word = Word(self.canvas, self.word_file)
        self.word.get_new_word()

        # set timer
        self.timer = Time()
        self.timer.reset_start_time()

        # play new music
        self.sound.change_music(self.sound.begin_theme_intro, 1, 1)
        self.sound.queue_music(self.sound.begin_theme_loop)

        self.main_menu = main_menu
        self.monster_visible = True

    def update(self, delta_time, actions):
        super().update(delta_time, actions)

        # set idle animation to true
        self.player_idle = True
        self.monster_idle = True

        # get elapsed time
        self.timer.get_elapsed_time()

        # when player escape button down pause game and show exit to title choice
        if actions['escape']:
            self.timer.pause_timer()

            # exit to main menu
            if self.main_menu.check_confirm('Exit to Menu?', 7):
                while len(self.game.state_stack) > 2:
                    self.exit_state()
                    self.sound.change_music(self.sound.title_theme, 1)
                    self.draw.fade_screen('black', self.main_menu, 100)
            else:

                # for fix bug (unknown str) add here
                self.game.user_text = self.game.user_text[:-1]
                self.timer.unpause_timer()

        # when player enter button down
        if actions['enter'] & (self.monster_visible == True):

            # cheat
            if self.game.user_text.lower().strip() == 'gg':
                self.player_hp.take_health(self.player_hp.max_health)

            ## check player word
            # get new word and heal player monster take dmg
            if self.word.checkWord(self.game.user_text):
                self.word.get_new_word()
                self.player_hp.take_health(self.player.heal)
                self.monster_hp.take_damage(self.player.atk)
                self.sound.play_sound(self.sound.player_atk_sound)

            # monster heal
            else:
                self.monster_hp.take_health(self.monster.heal)
                self.sound.play_sound(self.sound.heal_sound)

            # check if monster dead
            if self.monster_hp.target_health <= 0:
                self.timer.reset_last_ticks()
                self.monster_visible = False

            # reset input user_text
            self.game.user_text = ''

        # do something every 5 second and monster visible
        if self.monster_visible == True:
            if self.timer.get_time_diff(5000):

                # monster attack
                self.player_hp.take_damage(self.monster.atk)
                self.sound.play_sound(self.sound.demo_atk_sound)
        
        # player dead go to end screen show score
        if self.player_hp.target_health <= 0:
            new_state = EndScreen(self.game, self.timer.elasped_time, self.word.word_correct_count, self.player_hp.target_health, self.main_menu)
            new_state.enter_state()
            self.sound.change_music(self.sound.begin_theme_end, 1, 1)

        # monster dead, spawn new monster
        if self.monster_hp.target_health <= 0 and (self.monster_visible == False):

            # cooldown 1.5 second before spawn new monster
            if self.timer.get_time_diff(1500):
            
                # random choice from monster list
                random.seed(time.time())
                self.monster = random.choice(self.monster_list)
                self.monster_hp = Healthbar(self.canvas, self.monster.hp, self.monster.hp_bar_lenght, 300 - self.monster.hp_bar_lenght, 45)
                self.monster.add_monster()
                self.monster_visible = True
                self.game.reset_user_text()
                self.timer.reset_last_ticks()
            
    def render(self, surface):

        # fill background
        surface.fill((0, 0, 0))

        # draw player sprite
        self.player.draw_sprite(surface, self.player_idle)

        if self.monster_visible == True:

            # draw monster sprite
            self.monster.draw_sprite(surface, self.monster_idle)

            # render and show input box
            self.word.renderInputBox('white', self.game.user_text)

            # show meaning to screen
            surface.blit(self.word.answerMeaning, self.word.meaning_rect)

        self.render_name_and_helath()

        # render time count
        self.draw.draw_text(6, int(self.timer.elasped_time), 'white', self.CANVAS_W * 0.5, self.CANVAS_H * 0.1)

    def render_name_and_helath(self):

        # draw player name and health bar
        self.draw.draw_text(8, self.player.name, 'white', 45, 37)
        self.player_hp.update()

        # draw monster name and heath bar
        if self.monster_visible == True:
            self.monster_hp.update()
            self.draw.draw_text(8, self.monster.name, 'white', 300, 37, False, True)

