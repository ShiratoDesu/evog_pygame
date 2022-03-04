import pygame
import sys
from assets.sprites import Sprites

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.sprite = Sprites()
        
        self.current_sprite = 0
        self.image = self.sprite.knight[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.idle_animation = False

        self.profile = open('charactor/player.txt',encoding = 'utf-8').read().splitlines()

        self.name = self.profile[0]
        self.hp = int(self.profile[1])
        self.hp_bar_lenght = int(self.profile[2])
        self.atk = int(self.profile[3])
        self.heal = int(self.profile[4])

    def update(self, speed, animation=False):
        if animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprite.knight):
                self.current_sprite = 0

        self.image = self.sprite.knight[int(self.current_sprite)]

# Creating the sprites and groups
    def draw_sprite(self, screen, animation):
        self.moving_sprites.draw(screen)
        self.moving_sprites.update(0.25, animation)

    
    def add_player(self):
        self.moving_sprites = pygame.sprite.Group()
        player = Player(self.pos_x, self.pos_y)
        self.moving_sprites.add(player)