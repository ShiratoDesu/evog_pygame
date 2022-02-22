import os
import pygame
from assets.assets import Assets

class Sprites(Assets):
    def __init__(self) -> None:
        Assets.__init__(self)
        self.knight_idle_dir = os.path.join(self.sprites_dir, 'knight_idle')
        self.load_sprites()

    # method to load sprites
    def load_sprites(self):
        self.mc_sprite = os.path.join(self.sprites_dir, 'knight_design.png')
        self.kinght_sprite_idle = os.listdir(self.knight_idle_dir)
        
        # define list
        self.knight = []
        emptyList = []
        
        # loop for load image to list
        for knight_idle in self.kinght_sprite_idle[:]:
            if knight_idle.endswith('.png'):
                dir = os.path.join(self.knight_idle_dir, knight_idle)
                self.knight.append(pygame.image.load(dir))


