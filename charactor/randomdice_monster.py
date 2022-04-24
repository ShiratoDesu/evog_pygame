import random
import time
from assets.sprites import Sprites

class Randomdice():
    def __init__(self, pos_x, pos_y, sound):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.atk_sound = sound.random_dice_atk_sound

        self.sprite = Sprites()
        self.sound = sound
        self.attacking = False
        self.hitted = False
        
        self.current_sprite = 0
        self.image = self.sprite.randomdice_list_idle[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

        self.name = 'Random Dice'
        self.hp = 500
        self.hp_bar_lenght = 120
        self.atk = 10
        self.heal = 10
        self.atk_cd = 5000

    def update(self, speed, dt, animation=False):
        adj_speed = speed * dt * 60
        if self.attacking == True:
            self.image = self.sprite.randomdice_list_atk[int(self.current_sprite)]
            self.current_sprite += adj_speed

            if int(self.current_sprite) >= len(self.sprite.randomdice_list_atk):
                self.current_sprite = 0
                self.attacking = False

        elif animation == True:
            self.current_sprite += adj_speed

            if int(self.current_sprite) >= len(self.sprite.randomdice_list_idle):
                self.current_sprite = 0

        if self.attacking == False:
            self.image = self.sprite.randomdice_list_idle[int(self.current_sprite)]


    def attack(self):
        self.current_sprite = 0
        random.seed(time.time())
        self.atk = random.randrange(2, 13)
        self.atk_cd = random.randrange(2000, 7000)
        self.attacking = True
    
    def get_hitted(self):
        self.hitted = True
        random.seed(time.time())
        self.heal = random.randrange(10, 50)

# Reset animation after killed
    def killed(self):
        self.current_sprite = 0
        self.attacking = False
        self.image = self.sprite.randomdice_list_idle[int(self.current_sprite)]
        self.sound.change_music(self.sound.prepare_for_battle_intro, 1, 1)
        self.sound.queue_music(self.sound.prepare_for_battle_loop)

# Creating the sprites and groups
    def draw_sprite(self, screen, animation, dt):
        if self.attacking:
            self.rect = (225 - 5, 100)
        elif self.hitted:
            self.rect = (225 + 5, 100)
            self.hitted = False
        else:
            self.rect = (225, 100)
        screen.blit(self.image, self.rect)
        self.update(0.25, dt, animation)