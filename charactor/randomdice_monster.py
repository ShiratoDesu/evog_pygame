import pygame
from assets.sound import Sound 
from assets.sprites import Sprites

class Randomdice(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, sound):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.atk_sound = sound.random_dice_atk_sound

        self.sprite = Sprites()
        self.sound = Sound(sound.overall_volume, sound.music_volume, sound.effect_volume)
        self.attacking = False
        self.hitted = False
        
        self.current_sprite = 0
        self.image = self.sprite.randomdice_list_idle[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

        self.name = 'Random Dice'
        self.hp = 100
        self.hp_bar_lenght = 100
        self.atk = 5
        self.heal = 10

    def update(self, speed, animation=False):
        if self.attacking == True:
            self.image = self.sprite.randomdice_list_atk[int(self.current_sprite)]
            self.current_sprite += speed

            if int(self.current_sprite) >= len(self.sprite.randomdice_list_atk):
                self.current_sprite = 0
                self.attacking = False

        elif animation == True:
            self.current_sprite += speed

            if int(self.current_sprite) >= len(self.sprite.randomdice_list_idle):
                self.current_sprite = 0

        if self.attacking == False:
            self.image = self.sprite.randomdice_list_idle[int(self.current_sprite)]


    def attack(self):
        self.current_sprite = 0
        self.attacking = True
    
    def get_hitted(self):
        self.hitted = True

# Reset animation after killed
    def killed(self):
        self.current_sprite = 0
        self.attacking = False
        self.image = self.sprite.randomdice_list_idle[int(self.current_sprite)]
        self.sound.change_music(self.sound.icy_cave_end, 1, 1)
        self.sound.queue_music(self.sound.begin_theme_loop)

# Creating the sprites and groups
    def draw_sprite(self, screen, animation):
        if self.attacking:
            self.rect = (225 - 5, 100)
        elif self.hitted:
            self.rect = (225 + 5, 100)
            self.hitted = False
        else:
            self.rect = (225, 100)
        screen.blit(self.image, self.rect)
        self.update(0.25, animation)
    
    #def add_monster(self):
    #     self.moving_monster_sprites = pygame.sprite.Group()
    #     monster = Mrcube(self.pos_x, self.pos_y)
    #     self.moving_monster_sprites.add(monster)