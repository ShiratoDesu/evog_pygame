import pygame, sys

class Healthbar(pygame.sprite.Sprite):
    def __init__(self, canvas, health, healthbar_length):
        super().__init__()
        self.canvas = canvas
        self.canvas_w, self.canvas_h = canvas.get_size()
        self.image = pygame.Surface((40, 40))
        self.image.fill((0,240,240))
        self.rect = self.image.get_rect(center = (self.canvas_w/2, self.canvas_h/2))
        self.current_health = health
        self.target_health = health
        self.max_health = health
        self.health_bar_length = healthbar_length
        self.health_bar_hieght = 10
        self.health_ratio = self.max_health / self.health_bar_length
        self.health_change_speed = 2

    def update(self):
        self.advanced_health()

    def take_damage(self, amount):
        if self.target_health > 0:
            self.target_health -= amount
        if self.target_health <= 0:
            self.target_health = 0

    def take_health(self, amount):
        if self.target_health < self.max_health:
            self.target_health += amount
        if self.target_health >= self.max_health:
            self.target_health = self.max_health

    # def basic_health(self):
    #     pygame.draw.rect(self.canvas, (255,0,0), (10, 10, self.target_health/self.health_ratio, 25))
    #     pygame.draw.rect(self.canvas, (255,255,255), (10, 10, self.health_bar_length, 25), 2)

    def advanced_health(self):
            transition_width = 0
            transition_color = "red"
            health_bar_rect = pygame.Rect(10,45,self.current_health / self.health_ratio, self.health_bar_hieght)
            transition_bar_rect = pygame.Rect(health_bar_rect.right,45,transition_width, self.health_bar_hieght)
            if self.current_health < self.target_health:
                self.current_health += self.health_change_speed
                transition_width = int((self.target_health - self.current_health) / self.health_ratio)
                transition_color = (0,255,0)
                health_bar_rect = pygame.Rect(10,45,self.current_health / self.health_ratio, self.health_bar_hieght)

            if self.current_health > self.target_health:
                self.current_health -= self.health_change_speed 
                transition_width = int((self.current_health - self.target_health) / self.health_ratio)
                transition_color = "yellow"
                health_bar_rect = pygame.Rect(10,45,self.target_health / self.health_ratio, self.health_bar_hieght)

            transition_bar_rect = pygame.Rect(health_bar_rect.right,45,transition_width, self.health_bar_hieght)
            
            pygame.draw.rect(self.canvas,(255,0,0),health_bar_rect) 
            pygame.draw.rect(self.canvas,transition_color,transition_bar_rect)	
            pygame.draw.rect(self.canvas,(255,255,255),(10,45,self.health_bar_length, self.health_bar_hieght),1)	