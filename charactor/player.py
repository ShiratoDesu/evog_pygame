import pygame
import sys
from assets.sprites import Sprites

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.idle()
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.sprite = Sprites()
        
        self.current_sprite = 0
        self.image = self.sprite.knight[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def idle(self):
        self.idle_animation = True

    def update(self, speed):
        if self.idle_animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprite.knight):
                self.current_sprite = 0

        self.image = self.sprite.knight[int(self.current_sprite)]

# Creating the sprites and groups
    def draw_sprite(self, screen):
        self.moving_sprites.draw(screen)
        self.moving_sprites.update(0.25)

    
    def add_player(self):
        self.moving_sprites = pygame.sprite.Group()
        player = Player(self.pos_x, self.pos_y)
        self.moving_sprites.add(player)

# #while True:
#     for event in pygame.event.get():
#         player.idle()
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         #if event.type == pygame.KEYDOWN:
#             #player.idle()

    # Drawing
    # screen.fill((0, 0, 0))
    # moving_sprites.draw(screen)
    # moving_sprites.update(0.25)
    # pygame.display.flip()
    # clock.tick(60)
