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
        self.amongus_idle_dir = os.path.join(self.sprites_dir, 'amongus_idle')
        self.madsoldier_idle_dir = os.path.join(self.sprites_dir, 'madsoldier_idle')
        self.forestenergy_idle_dir = os.path.join(self.sprites_dir, 'forestenergy_idle')
        self.archer_idle_dir = os.path.join(self.sprites_dir, 'archer_idle')
        self.darkknight_idle_dir = os.path.join(self.sprites_dir, 'darkknight_idle')

        self.knight_atk_dir = os.path.join(self.sprites_dir, 'knight_atk')
        self.mrcube_atk_dir = os.path.join(self.sprites_dir, 'mrcube_atk')
        self.randomdice_atk_dir = os.path.join(self.sprites_dir, 'randomdice_atk')
        self.shadowman_atk_dir = os.path.join(self.sprites_dir, 'shadowman_atk')
        self.littleghost_atk_dir = os.path.join(self.sprites_dir, 'littleghost_atk')
        self.smilebanana_atk_dir = os.path.join(self.sprites_dir, 'smilebanana_atk')
        self.amongus_atk_dir = os.path.join(self.sprites_dir, 'amongus_atk')
        self.madsoldier_atk_dir = os.path.join(self.sprites_dir, 'madsoldier_atk')
        self.forestenergy_atk_dir = os.path.join(self.sprites_dir, 'forestenergy_atk')
        self.archer_atk_dir = os.path.join(self.sprites_dir, 'archer_atk')
        self.darkknight_atk_dir = os.path.join(self.sprites_dir, 'darkknight_atk')

        self.load_sprites()

    # method to load sprites
    def load_sprites(self):
        self.kinght_sprite_idle = os.listdir(self.knight_idle_dir)
        self.mrcube_sprite_idle = os.listdir(self.mrcube_idle_dir)
        self.randomdice_sprite_idle = os.listdir(self.randomdice_idle_dir)
        self.shadowman_sprite_idle = os.listdir(self.shadowman_idle_dir)
        self.littleghost_sprite_idle = os.listdir(self.littleghost_idle_dir)
        self.smilebanana_sprite_idle = os.listdir(self.smilebanana_idle_dir)
        self.amongus_sprite_idle = os.listdir(self.amongus_idle_dir)
        self.madsoldier_sprite_idle = os.listdir(self.madsoldier_idle_dir)
        self.forestenergy_sprite_idle = os.listdir(self.forestenergy_idle_dir)
        self.archer_sprite_idle = os.listdir(self.archer_idle_dir)
        self.darkknight_sprite_idle = os.listdir(self.darkknight_idle_dir)

        self.mrcube_sprite_atk = os.listdir(self.mrcube_atk_dir)
        self.randomdice_sprite_atk = os.listdir(self.randomdice_atk_dir)
        self.shadowman_sprite_atk = os.listdir(self.shadowman_atk_dir)
        self.littleghost_sprite_atk = os.listdir(self.littleghost_atk_dir)
        self.smilebanana_sprite_atk = os.listdir(self.smilebanana_atk_dir)
        self.knight_sprite_atk = os.listdir(self.knight_atk_dir)
        self.amongus_sprite_atk = os.listdir(self.amongus_atk_dir)
        self.madsoldier_sprite_atk = os.listdir(self.madsoldier_atk_dir)
        self.forestenergy_sprite_atk = os.listdir(self.forestenergy_atk_dir)
        self.archer_sprite_atk = os.listdir(self.archer_atk_dir)
        self.darkknight_sprite_atk = os.listdir(self.darkknight_atk_dir)
        
        # define list
        self.knight_list_idle = []

        self.mrcube_list_idle = []
        self.randomdice_list_idle = []
        self.littleghost_list_idle = []
        self.smilebanana_list_idle = []
        self.shadowman_list_idle = []
        self.amongus_list_idle = []
        self.madsoldier_list_idle = []
        self.forestenergy_list_idle = []
        self.archer_list_idle = []
        self.darkknight_list_idle = []

        self.knight_list_atk = []
        self.mrcube_list_atk = []
        self.randomdice_list_atk = []
        self.littleghost_list_atk = []
        self.smilebanana_list_atk = []
        self.shadowman_list_atk = []
        self.amongus_list_atk = []
        self.madsoldier_list_atk = []
        self.forestenergy_list_atk = []
        self.archer_list_atk = []
        self.darkknight_list_atk = []
        
        # loop for load image to list
        # idle list
        for knight_idle in self.kinght_sprite_idle[:]:
            if knight_idle.endswith('.png'):
                dir = os.path.join(self.knight_idle_dir, knight_idle)
                self.knight_list_idle.append(pygame.image.load(dir))

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
        
        for amongus_idle in self.amongus_sprite_idle[:]:
            if amongus_idle.endswith('.png'):
                dir = os.path.join(self.amongus_idle_dir, amongus_idle)
                self.amongus_list_idle.append(pygame.image.load(dir))

        for madsoldier_idle in self.madsoldier_sprite_idle[:]:
                if madsoldier_idle.endswith('.png'):
                    dir = os.path.join(self.madsoldier_idle_dir, madsoldier_idle)
                    self.madsoldier_list_idle.append(pygame.image.load(dir))

        for forestenergy_idle in self.forestenergy_sprite_idle[:]:
                if forestenergy_idle.endswith('.png'):
                    dir = os.path.join(self.forestenergy_idle_dir, forestenergy_idle)
                    self.forestenergy_list_idle.append(pygame.image.load(dir))

        for archer_idle in self.archer_sprite_idle[:]:
                if archer_idle.endswith('.png'):
                    dir = os.path.join(self.archer_idle_dir, archer_idle)
                    self.archer_list_idle.append(pygame.image.load(dir))

        for darkknight_idle in self.darkknight_sprite_idle[:]:
            if darkknight_idle.endswith('.png'):
                dir = os.path.join(self.darkknight_idle_dir, darkknight_idle)
                image = pygame.image.load(dir)
                image_filp = pygame.transform.flip(image,True,False)
                self.darkknight_list_idle.append(image_filp)

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

        for amongus_atk in self.amongus_sprite_atk[:]:
            if amongus_atk.endswith('.png'):
                dir = os.path.join(self.amongus_atk_dir, amongus_atk)
                self.amongus_list_atk.append(pygame.image.load(dir))

        for madsoldier_atk in self.madsoldier_sprite_atk[:]:
                if madsoldier_atk.endswith('.png'):
                    dir = os.path.join(self.madsoldier_atk_dir, madsoldier_atk)
                    self.madsoldier_list_atk.append(pygame.image.load(dir))

        for forestenergy_atk in self.forestenergy_sprite_atk[:]:
                if forestenergy_atk.endswith('.png'):
                    dir = os.path.join(self.forestenergy_atk_dir, forestenergy_atk)
                    self.forestenergy_list_atk.append(pygame.image.load(dir))

        for archer_atk in self.archer_sprite_atk[:]:
                if archer_atk.endswith('.png'):
                    dir = os.path.join(self.archer_atk_dir, archer_atk)
                    self.archer_list_atk.append(pygame.image.load(dir))

        for darkknight_atk in self.darkknight_sprite_atk[:]:
            if darkknight_atk.endswith('.png'):
                dir = os.path.join(self.darkknight_atk_dir, darkknight_atk)
                image = pygame.image.load(dir)
                image_filp = pygame.transform.flip(image,True,False)
                self.darkknight_list_atk.append(image_filp)