from pickle import FALSE
import pygame
import sys
from assets.sprites import Sprites

class Smilebanana(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.sprite = Sprites()
        self.attacking = False
        
        self.current_sprite = 0
        self.image = self.sprite.smilebanana_list_idle[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

        self.name = 'Smile Banana'
        self.hp = 100
        self.hp_bar_lenght = 100
        self.atk = 5
        self.heal = 10

    def update(self, speed, animation=False):
        if self.attacking == True:
            self.image = self.sprite.smilebanana_list_atk[int(self.current_sprite)]
            self.current_sprite += speed

            if int(self.current_sprite) >= len(self.sprite.smilebanana_list_atk):
                self.current_sprite = 0
                self.attacking = False

        elif animation == True:
            self.current_sprite += speed

            if int(self.current_sprite) >= len(self.sprite.smilebanana_list_idle):
                self.current_sprite = 0

        if self.attacking == False:
            self.image = self.sprite.smilebanana_list_idle[int(self.current_sprite)]


    def attack(self):
        self.current_sprite = 0
        self.attacking = True

# Reset animation after killed
    def killed(self):
        self.current_sprite = 0
        self.attacking = False
        self.image = self.sprite.smilebanana_list_idle[int(self.current_sprite)]
        
# Creating the sprites and groups
    def draw_sprite(self, screen, animation):
        screen.blit(self.image, (225,100))
        self.update(0.25, animation)
    
    #def add_monster(self):
    #     self.moving_monster_sprites = pygame.sprite.Group()
    #     monster = Mrcube(self.pos_x, self.pos_y)
    #     self.moving_monster_sprites.add(monster)