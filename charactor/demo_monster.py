import pygame
from assets.sprites import Sprites

class DemoMonster(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.sprite = Sprites()
        
        self.current_sprite = 0
        self.image = self.sprite.demo_monster[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.idle_animation = False

        self.name = '????'
        self.hp = 100
        self.hp_bar_lenght = 70
        self.atk = 25
        self.heal = 100

    def update(self, speed, animation=False):
        if animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprite.demo_monster):
                self.current_sprite = 0

        self.image = self.sprite.demo_monster[int(self.current_sprite)]


# Creating the sprites and groups
    def draw_sprite(self, screen, animation):
        self.moving_monster_sprites.draw(screen)
        self.moving_monster_sprites.update(0.25, animation)
    
    def add_monster(self):
        self.moving_monster_sprites = pygame.sprite.Group()
        monster = DemoMonster(self.pos_x, self.pos_y)
        self.moving_monster_sprites.add(monster)