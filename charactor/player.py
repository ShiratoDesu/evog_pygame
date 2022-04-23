import pygame
import sys
from assets.sprites import Sprites

class Player():
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.sprite = Sprites()
        
        self.current_sprite = 0
        self.image = self.sprite.knight_list_idle[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.attacking = False
        self.hitted = False

        self.name = 'Sir.Evog'
        self.hp = 50
        self.hp_bar_lenght = 70
        self.atk = 25
        self.heal = 5

    def update(self, speed, dt, animation=False):
        adj_speed = speed * dt * 60
        if self.attacking == True:
            self.image = self.sprite.knight_list_atk[int(self.current_sprite)]
            self.current_sprite += adj_speed

            if int(self.current_sprite) >= len(self.sprite.knight_list_atk):
                self.current_sprite = 0
                self.attacking = False

        elif animation == True:
            self.current_sprite += adj_speed

            if int(self.current_sprite) >= len(self.sprite.knight_list_idle):
                self.current_sprite = 0

        if self.attacking == False:
            self.image = self.sprite.knight_list_idle[int(self.current_sprite)]

    def attack(self):
        self.current_sprite = 0
        self.attacking = True

    def get_hitted(self):
        self.hitted = True

# Creating the sprites and groups
    def draw_sprite(self, screen, animation, dt):
        if self.attacking:
            self.rect.center = (self.pos_x + 5, self.pos_y)
        elif self.hitted:
            self.rect.center = (self.pos_x - 5, self.pos_y)
            self.hitted = False
        else:
            self.rect.center = (self.pos_x, self.pos_y)
        screen.blit(self.image, self.rect)
        self.update(0.25, dt, animation)

    
    # def add_player(self):
    #     self.moving_sprites = pygame.sprite.Group()
    #     player = Player(self.pos_x, self.pos_y)
    #     self.moving_sprites.add(player)