from assets.sprites import Sprites

class Madsoldier():
    def __init__(self, pos_x, pos_y, sound):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.atk_sound = sound.mad_soldier_atk_sound

        self.sprite = Sprites()
        self.sound = sound
        self.attacking = False
        self.hitted = False
        
        self.current_sprite = 0
        self.image = self.sprite.madsoldier_list_idle[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

        self.name = 'Mad soldier'
        self.hp = 75
        self.hp_bar_lenght = 70
        self.atk = 4
        self.heal = 15
        self.atk_cd = 3000

    def update(self, speed, dt, animation=False):
        adj_speed = speed * dt * 60
        if self.attacking == True:
            self.image = self.sprite.madsoldier_list_atk[int(self.current_sprite)]
            self.current_sprite += adj_speed

            if int(self.current_sprite) >= len(self.sprite.madsoldier_list_atk):
                self.current_sprite = 0
                self.attacking = False

        elif animation == True:
            self.current_sprite += adj_speed

            if int(self.current_sprite) >= len(self.sprite.madsoldier_list_idle):
                self.current_sprite = 0

        if self.attacking == False:
            self.image = self.sprite.madsoldier_list_idle[int(self.current_sprite)]


    def attack(self):
        self.current_sprite = 0
        self.attacking = True
    
    def get_hitted(self):
        self.hitted = True

# Reset animation after killed
    def killed(self):
        self.current_sprite = 0
        self.attacking = False
        self.image = self.sprite.madsoldier_list_idle[int(self.current_sprite)]

# Creating the sprites and groups
    def draw_sprite(self, screen, animation, dt):
        if self.attacking:
            self.rect = (225 - 5, 100)
        elif self.hitted:
            self.rect = (225 + 5, 100)
            self.hitted = False
        else:
            self.rect = (225, 100)
        screen.blit(self.image, self.rect)
        self.update(0.25, dt, animation)