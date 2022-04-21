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
        self.smilebanana_idle_dir = os.path.join(self.sprites_dir, 'smilebanana_idle')

        self.knight_atk_dir = os.path.join(self.sprites_dir, 'knight_atk')
        self.mrcube_atk_dir = os.path.join(self.sprites_dir, 'mrcube_atk')
        self.randomdice_atk_dir = os.path.join(self.sprites_dir, 'randomdice_atk')
        self.shadowman_atk_dir = os.path.join(self.sprites_dir, 'shadowman_atk')
        self.littleghost_atk_dir = os.path.join(self.sprites_dir, 'littleghost_atk')
        self.smilebanana_atk_dir = os.path.join(self.sprites_dir, 'smilebanana_atk')

        self.demo_monster_idle_dir = os.path.join(self.sprites_dir, 'demo_idle')
        self.load_sprites()

    # method to load sprites
    def load_sprites(self):
        self.kinght_sprite_idle = os.listdir(self.knight_idle_dir)
        self.demo_monster_sprite_idle = os.listdir(self.demo_monster_idle_dir)
        self.mrcube_sprite_idle = os.listdir(self.mrcube_idle_dir)
        self.randomdice_sprite_idle = os.listdir(self.randomdice_idle_dir)
        self.shadowman_sprite_idle = os.listdir(self.shadowman_idle_dir)
        self.littleghost_sprite_idle = os.listdir(self.littleghost_idle_dir)
        self.smilebanana_sprite_idle = os.listdir(self.smilebanana_idle_dir)

        self.mrcube_sprite_atk = os.listdir(self.mrcube_atk_dir)
        self.randomdice_sprite_atk = os.listdir(self.randomdice_atk_dir)
        self.shadowman_sprite_atk = os.listdir(self.shadowman_atk_dir)
        self.littleghost_sprite_atk = os.listdir(self.littleghost_atk_dir)
        self.smilebanana_sprite_atk = os.listdir(self.smilebanana_atk_dir)
        self.knight_sprite_atk = os.listdir(self.knight_atk_dir)
        
        # define list
        self.knight_list_idle = []
        self.demo_monster = []

        self.mrcube_list_idle = []
        self.randomdice_list_idle = []
        self.littleghost_list_idle = []
        self.smilebanana_list_idle = []
        self.shadowman_list_idle = []

        self.knight_list_atk = []
        self.mrcube_list_atk = []
        self.randomdice_list_atk = []
        self.littleghost_list_atk = []
        self.smilebanana_list_atk = []
        self.shadowman_list_atk = []
        
        # loop for load image to list
        # idle list
        for knight_idle in self.kinght_sprite_idle[:]:
            if knight_idle.endswith('.png'):
                dir = os.path.join(self.knight_idle_dir, knight_idle)
                self.knight_list_idle.append(pygame.image.load(dir))

        for demo_monster_idle in self.demo_monster_sprite_idle[:]:
            if demo_monster_idle.endswith('.png'):
                dir = os.path.join(self.demo_monster_idle_dir, demo_monster_idle)
                image = pygame.image.load(dir)
                image_filp = pygame.transform.flip(image,True,False)
                self.demo_monster.append(image_filp)

        for randomdice_idle in self.randomdice_sprite_idle[:]:
            if randomdice_idle.endswith('.png'):
                dir = os.path.join(self.randomdice_idle_dir, randomdice_idle)
                self.randomdice_list_idle.append(pygame.image.load(dir))

        for shadowman_idle in self.shadowman_sprite_idle[:]:
            if shadowman_idle.endswith('.png'):
                dir = os.path.join(self.shadowman_idle_dir, shadowman_idle)
                self.shadowman_list_idle.append(pygame.image.load(dir))

        for littleghost_idle in self.littleghost_sprite_idle[:]:
            if littleghost_idle.endswith('.png'):
                dir = os.path.join(self.littleghost_idle_dir, littleghost_idle)
                self.littleghost_list_idle.append(pygame.image.load(dir))

        for smilebanana_idle in self.smilebanana_sprite_idle[:]:
            if smilebanana_idle.endswith('.png'):
                dir = os.path.join(self.smilebanana_idle_dir, smilebanana_idle)
                self.smilebanana_list_idle.append(pygame.image.load(dir))

        for mrcube_idle in self.mrcube_sprite_idle[:]:
            if mrcube_idle.endswith('.png'):
                dir = os.path.join(self.mrcube_idle_dir, mrcube_idle)
                self.mrcube_list_idle.append(pygame.image.load(dir))

        # atk list
        for knight_atk in self.knight_sprite_atk[:]:
            if knight_idle.endswith('.png'):
                dir = os.path.join(self.knight_atk_dir, knight_atk)
                self.knight_list_atk.append(pygame.image.load(dir))

        for mrcube_atk in self.mrcube_sprite_atk[:]:
            if mrcube_atk.endswith('.png'):
                dir = os.path.join(self.mrcube_atk_dir, mrcube_atk)
                self.mrcube_list_atk.append(pygame.image.load(dir))

        for randomdice_atk in self.randomdice_sprite_atk[:]:
            if randomdice_atk.endswith('.png'):
                dir = os.path.join(self.randomdice_atk_dir, randomdice_atk)
                self.randomdice_list_atk.append(pygame.image.load(dir))

        for shadowman_atk in self.shadowman_sprite_atk[:]:
            if shadowman_atk.endswith('.png'):
                dir = os.path.join(self.shadowman_atk_dir, shadowman_atk)
                self.shadowman_list_atk.append(pygame.image.load(dir))

        for littleghost_atk in self.littleghost_sprite_atk[:]:
            if littleghost_atk.endswith('.png'):
                dir = os.path.join(self.littleghost_atk_dir, littleghost_atk)
                self.littleghost_list_atk.append(pygame.image.load(dir))

        for smilebanana_atk in self.smilebanana_sprite_atk[:]:
            if smilebanana_atk.endswith('.png'):
                dir = os.path.join(self.smilebanana_atk_dir, smilebanana_atk)
                self.smilebanana_list_atk.append(pygame.image.load(dir))