import pygame

class Healthbar(pygame.sprite.Sprite):
    def __init__(self, canvas, health, healthbar_length, position_x, position_y, reverse=False):
        super().__init__()
        self.canvas = canvas
        self.canvas_w, self.canvas_h = canvas.get_size()
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 240, 240))
        self.rect = self.image.get_rect(
            center=(self.canvas_w/2, self.canvas_h/2))
        self.current_health = health
        self.target_health = health
        self.max_health = health
        self.health_bar_length = healthbar_length
        self.health_bar_height = 10
        self.health_ratio = self.max_health / self.health_bar_length
        self.health_change_speed = 1
        self.pos_x, self.pos_y = position_x, position_y
        self.reverse = reverse

    def update(self, dt):
        adj_health_change_speed = self.health_change_speed * dt * 60
        self.advanced_health(adj_health_change_speed)

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

    def advanced_health(self, change_speed):
        transition_width = 0
        transition_color = "red"

        # stable healthbar
        if self.reverse:
            health_bar_rect = pygame.Rect(self.pos_x + self.health_bar_length - (self.current_health / self.health_ratio),
                                          self.pos_y, (self.current_health / self.health_ratio), self.health_bar_height)
            transition_bar_rect = pygame.Rect(
                health_bar_rect.left - transition_width, self.pos_y, transition_width, self.health_bar_height)
        else:
            health_bar_rect = pygame.Rect(
                self.pos_x, self.pos_y, (self.current_health / self.health_ratio), self.health_bar_height)
            transition_bar_rect = pygame.Rect(
                health_bar_rect.right, self.pos_y, transition_width, self.health_bar_height)

        # healing
        if self.current_health < self.target_health:
            self.current_health += change_speed
            transition_width = int(
                (self.target_health - self.current_health) / self.health_ratio)
            transition_color = (0, 255, 0)
            if self.reverse:
                health_bar_rect = pygame.Rect(self.pos_x + self.health_bar_length - (self.current_health / self.health_ratio),
                                              self.pos_y, (self.current_health / self.health_ratio), self.health_bar_height)
            else:
                health_bar_rect = pygame.Rect(
                    self.pos_x, self.pos_y, (self.current_health / self.health_ratio), self.health_bar_height)

        # damaged
        if self.current_health > self.target_health:
            self.current_health -= change_speed
            transition_width = int(
                (self.current_health - self.target_health) / self.health_ratio)
            transition_color = "yellow"
            if self.reverse:
                health_bar_rect = pygame.Rect(self.pos_x + self.health_bar_length - (self.target_health / self.health_ratio),
                                              self.pos_y, (self.target_health / self.health_ratio), self.health_bar_height)
            else:
                health_bar_rect = pygame.Rect(
                    self.pos_x, self.pos_y, (self.target_health / self.health_ratio), self.health_bar_height)

        if self.reverse:
            transition_bar_rect = pygame.Rect(
                health_bar_rect.left - transition_width, self.pos_y, transition_width, self.health_bar_height)
        else:
            transition_bar_rect = pygame.Rect(
                health_bar_rect.right, self.pos_y, transition_width, self.health_bar_height)

        pygame.draw.rect(self.canvas, (0, 0, 0), (self.pos_x, self.pos_y,
                         self.health_bar_length, self.health_bar_height))
        pygame.draw.rect(self.canvas, (255, 0, 0), health_bar_rect)
        pygame.draw.rect(self.canvas, transition_color, transition_bar_rect)
        pygame.draw.rect(self.canvas, (255, 255, 255), (self.pos_x,
                         self.pos_y, self.health_bar_length, self.health_bar_height), 1)
