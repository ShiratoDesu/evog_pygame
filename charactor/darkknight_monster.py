import pygame
from assets.sound import Sound 
from assets.sprites import Sprites

class Darkknight():
    def __init__(self, pos_x, pos_y, sound):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.atk_sound = sound.player_atk_sound

        self.sprite = Sprites()
        self.sound = Sound(sound.overall_volume, sound.music_volume, sound.effect_volume)
        self.attacking = False
        self.hitted = False
        
        self.current_sprite = 0
        self.image = self.sprite.darkknight_list_idle[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

        self.name = 'Dark Knight'
        self.hp = 625
        self.hp_bar_lenght = 130
        self.atk = 13
        self.heal = 25
        self.atk_cd = 7000

    def update(self, speed, dt, animation=False):
        adj_speed = speed * dt * 60
        if self.attacking == True:
            self.image = self.sprite.darkknight_list_atk[int(self.current_sprite)]
            self.current_sprite += adj_speed

            if int(self.current_sprite) >= len(self.sprite.darkknight_list_atk):
                self.current_sprite = 0
                self.attacking = False

        elif animation == True:
            self.current_sprite += adj_speed

            if int(self.current_sprite) >= len(self.sprite.darkknight_list_idle):
                self.current_sprite = 0

        if self.attacking == False:
            self.image = self.sprite.darkknight_list_idle[int(self.current_sprite)]


    def attack(self):
        self.current_sprite = 0
        self.attacking = True
    
    def get_hitted(self):
        self.hitted = True

# Reset animation after killed
    def killed(self):
        self.current_sprite = 0
        self.attacking = False
        self.image = self.sprite.darkknight_list_idle[int(self.current_sprite)]
        self.sound.change_music(self.sound.exploring_the_unknown_intro, 1, 1)
        self.sound.queue_music(self.sound.exploring_the_unknown_loop)

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
    
    #def add_monster(self):
    #     self.moving_monster_sprites = pygame.sprite.Group()
    #     monster = Mrcube(self.pos_x, self.pos_y)
    #     self.moving_monster_sprites.add(monster)