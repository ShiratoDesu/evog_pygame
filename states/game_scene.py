from charactor.amogus_monster import Amogus
from charactor.archer_monster import Archer
from charactor.darkknight_monster import Darkknight
from charactor.forestenergy_monster import Forestenergy
from charactor.littleghost_monster import Littleghost
from charactor.madsoldier_monster import Madsoldier
from charactor.mrcube_monster import Mrcube
from charactor.randomdice_monster import Randomdice
from charactor.shadowman_monster import Shadowman
from charactor.smilebanana_monster import Smilebanana
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
        self.monster_list = [Mrcube(self.CANVAS_W * 0.8, self.CANVAS_H * 0.8, self.sound),
                             Littleghost(self.CANVAS_W * 0.8,
                                         self.CANVAS_H * 0.8, self.sound),
                             Smilebanana(self.CANVAS_W * 0.8,
                                         self.CANVAS_H * 0.8, self.sound),
                             Madsoldier(self.CANVAS_W * 0.8,
                                        self.CANVAS_H * 0.8, self.sound),
                             Archer(self.CANVAS_W * 0.8, self.CANVAS_H * 0.8, self.sound)]
        self.boss_list = [Forestenergy(self.CANVAS_W * 0.8, self.CANVAS_H * 0.8, self.sound),
                          Shadowman(self.CANVAS_W * 0.8,
                                    self.CANVAS_H * 0.8, self.sound),
                          Randomdice(self.CANVAS_W * 0.8,
                                     self.CANVAS_H * 0.8, self.sound),
                          Darkknight(self.CANVAS_W * 0.8,
                                     self.CANVAS_H * 0.8, self.sound),
                          Amogus(self.CANVAS_W * 0.8, self.CANVAS_H * 0.8, self.sound)]
        self.boss_theme_list = [self.sound.icy_cave_loop,
                                self.sound.mysterious,
                                self.sound.prepare_for_battle_loop,
                                self.sound.exploring_the_unknown_loop,
                                self.sound.amogus_drip]
        self.background_list = ['black', 'red', 'green', 'blue', 'gray']

        self.current_monster = 1
        self.boss_index = 0
        self.background_index = 0

## DemoMonster(self.CANVAS_W * 0.8, self.CANVAS_H * 0.8 )

        # random monster from monster list and boss
        self.spawn_boss_and_monster()

        # set player and monster hp bar
        self.player_hp = Healthbar(
            self.canvas, self.player.hp, self.player.hp_bar_lenght, 20, 45)
        self.monster_hp = Healthbar(
            self.canvas, self.monster.hp, self.monster.hp_bar_lenght, 300 - self.monster.hp_bar_lenght, 45, True)

        # set idle animation
        self.player_idle = False
        self.monster_idle = False

        # get first word and answer
        self.word_file = [os.path.join(self.assets.words_dir, 'engmix_lv1.txt'),
                          os.path.join(self.assets.words_dir,
                                       'engmix_lv2.txt'),
                          os.path.join(self.assets.words_dir,
                                       'engmix_lv3.txt'),
                          os.path.join(self.assets.words_dir,
                                       'engmix_lv4.txt'),
                          os.path.join(self.assets.words_dir, 'engmix_lv5.txt')]
        self.current_word_file = 0
        self.word_correct = 0
        self.word = Word(self.canvas, self.word_file[self.current_word_file])
        self.word.get_new_word()

        # set timer
        self.timer = Time()

        self.timer.reset_start_time()

        # play new music
        self.sound.change_music(self.sound.begin_theme_intro, 1, 1)
        self.sound.queue_music(self.sound.begin_theme_loop)

        self.main_menu = main_menu
        self.monster_visible = True
        self.boss_killed = False

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

            # check player word
            # get new word and heal player monster take dmg
            if self.word.checkWord(self.game.user_text) and self.monster_hp.target_health > 0:
                self.player.attack()
                self.monster.get_hitted()
                self.player_hp.take_health(self.player.heal)
                self.monster_hp.take_damage(self.player.atk)
                self.sound.play_sound(self.sound.player_atk_sound)

                # check if monster is dead or not after damage dealth
                if self.monster_hp.target_health > 0:
                    self.word.get_new_word()
                elif self.monster_hp.target_health <= 0:
                    self.monster.killed()
                    if ((self.current_monster - 1) % 10) == 0:
                        self.boss_killed = True

            # monster heal if monster health > 0
            elif self.monster_hp.target_health > 0:
                self.monster_hp.take_health(self.monster.heal)
                self.sound.play_sound(self.sound.heal_sound)

            # reset input user_text
            self.game.user_text = ''

        # check if monster dead and player attack animation is end
        if self.monster_hp.target_health <= 0 and self.monster_visible and self.player.attacking == False:
            self.timer.reset_last_ticks()
            self.monster_visible = False

        # do something every 5 second and monster visible
        if self.monster_visible == True:
            if self.timer.get_time_diff(self.monster.atk_cd):

                # monster attack
                self.monster.attack()
                self.player.get_hitted()
                self.player_hp.take_damage(self.monster.atk)
                self.sound.play_sound(self.monster.atk_sound)

        # player dead go to end screen show score
        if self.player_hp.target_health <= 0:
            new_state = EndScreen(self.game, self.timer.elasped_time,
                                  self.word_correct, self.player_hp.target_health, self.main_menu)
            new_state.enter_state()
            self.sound.change_music(self.sound.begin_theme_end, 1, 1)

        # monster dead, spawn new monster
        if self.monster_hp.target_health <= 0 and (self.monster_visible == False):

            # cooldown 1.5 second before spawn new monster
            if self.timer.get_time_diff(1500):

                if self.boss_killed:
                    # keep all word correct count
                    self.word_correct += self.word.word_correct_count
                    self.word.reset_word_count()

                    # change background and word index
                    self.background_index += 1
                    self.current_word_file += 1

                    # check if word file and bakcground index out of range
                    if self.current_word_file >= len(self.word_file):
                        self.current_word_file = len(self.word_file) - 1
                    if self.background_index >= len(self.background_list):
                        self.background_index = len(self.background_list) - 1

                    # get new word instance and new world
                    self.word = Word(
                        self.canvas, self.word_file[self.current_word_file])
                    self.boss_killed = False

                # get new word
                self.word.get_new_word()

                # random choice from monster list
                self.spawn_boss_and_monster()
                self.monster_hp = Healthbar(
                    self.canvas, self.monster.hp, self.monster.hp_bar_lenght, 300 - self.monster.hp_bar_lenght, 45, True)
                # self.monster.add_monster()
                self.monster_visible = True
                self.game.reset_user_text()
                self.timer.reset_last_ticks()

    def render(self, surface):

        # fill background
        surface.fill(self.background_list[self.background_index])

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
        self.draw.draw_text(6, int(self.timer.elasped_time),
                            'white', self.CANVAS_W * 0.5, self.CANVAS_H * 0.1)

    def render_name_and_helath(self):

        # draw player name and health bar
        self.draw.draw_text(8, self.player.name, 'white', 52, 37)
        self.player_hp.update()
        self.draw.draw_text(6, str(self.player_hp.target_health) +
                            '/' + str(self.player_hp.max_health), 'white', 47, 50)

        # draw monster name and heath bar
        if self.monster_visible == True:
            self.monster_hp.update()
            self.draw.draw_text(8, self.monster.name,
                                'white', 300, 37, False, True)
            self.draw.draw_text(6, str(self.monster_hp.target_health) + '/' +
                                str(self.monster_hp.max_health), 'white', 295, 50, False, True)

    def spawn_boss_and_monster(self):
        random.seed(time.time())
        if (self.current_monster % 10) == 0 and self.boss_index < len(self.boss_list):

            # check boss index to play intro
            if self.boss_index == 2:
                self.sound.change_music(
                    self.sound.prepare_for_battle_intro, 1, 1)
                self.sound.queue_music(self.boss_theme_list[self.boss_index])
            elif self.boss_index == 3:
                self.sound.change_music(
                    self.sound.exploring_the_unknown_intro, 1, 1)
                self.sound.queue_music(self.boss_theme_list[self.boss_index])
            else:
                self.sound.change_music(
                    self.boss_theme_list[self.boss_index], 1)

            self.monster = self.boss_list[self.boss_index]
            self.boss_index += 1
        elif self.boss_index >= len(self.boss_list):
            self.boss_index = 0
            new_state = EndScreen(self.game, self.timer.elasped_time,
                                  self.word_correct, self.player_hp.target_health, self.main_menu)
            new_state.enter_state()
            self.sound.change_music(self.sound.begin_theme_end, 1, 1)
        else:
            self.monster = random.choice(self.monster_list)
        self.current_monster += 1
