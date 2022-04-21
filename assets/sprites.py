import os
import pygame
from assets.assets import Assets

class Sprites(Assets):
    def __init__(self) -> None:
        Assets.__init__(self)
        self.knight_idle_dir = os.path.join(self.sprites_dir, 'knight_idle')
        self.mrcube_idle_dir = os.path.join(self.sprites_dir, 'mrcube_idle')
        self.randomdice_idle_dir = os.path.join(self.sprites_dir, 'randomdice_idle')
        self.shadowman_idle_dir = os.path.join(self.sprites_dir, 'shadowman_idle')
        self.littleghost_idle_dir = os.path.join(self.sprites_dir, 'littleghost_idle')
        self.smilebanana_idle_dir = os.pathsep.join(self.sprites_dir, 'smilebanana_idle')

        self.knight_atk_dir = os.path.join(self.sprites_dir, 'knight_atk')
        self.mrcube_atk_atk = os.path.join(self.sprites_dir, 'mrcube_atk')
        self.randomdice_atk_dir = os.path.join(self.sprites_dir, 'randomdice_atk')
        self.shadowman_atk_dir = os.path.join(self.sprites_dir, 'shadowman_atk')
        self.littleghost_atk_dir = os.path.join(self.sprites_dir, 'littleghost_atk')
        self.smilebanana_atk_dir = os.pathsep.join(self.sprites_dir, 'smilebanana_atk')

        self.demo_monster_idle_dir = os.path.join(self.sprites_dir, 'demo_idle')
        self.load_sprites()

    # method to load sprites
    def load_sprites(self):
        self.kinght_sprite_idle = os.listdir(self.knight_idle_dir)
        self.demo_monster_sprite_idle = os.listdir(self.demo_monster_idle_dir)
        
        # define list
        self.knight = []
        self.demo_monster = []
        
        # loop for load image to list
        for knight_idle in self.kinght_sprite_idle[:]:
            if knight_idle.endswith('.png'):
                dir = os.path.join(self.knight_idle_dir, knight_idle)
                self.knight.append(pygame.image.load(dir))

        for demo_monster_idle in self.demo_monster_sprite_idle[:]:
            if demo_monster_idle.endswith('.png'):
                dir = os.path.join(self.demo_monster_idle_dir, demo_monster_idle)
                image = pygame.image.load(dir)
                image_filp = pygame.transform.flip(image,True,False)
                self.demo_monster.append(image_filp)

        for mrcube_idle in self.mrcube_idle_dir[:]:
            if knight_idle.endswith('.png'):
                dir = os.path.join(self.knight_idle_dir, knight_idle)
                self.knight.append(pygame.image.load(dir))

        