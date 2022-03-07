import pygame
import time


class Time():
    def __init__(self):
        self.start_time = time.time()
        self.elasped_time = 0
        self.last = pygame.time.get_ticks()

    def get_elapsed_time(self):
        self.elasped_time = time.time() - self.start_time
    
    def reset_start_time(self):
        self.start_time = time.time()

    def get_time_diff(self, cooldown):
        now = pygame.time.get_ticks()
        if now - self.last >= cooldown:
            self.last = now
            return True
        print(now - self.last)

    def reset_last_ticks(self):
        self.last = pygame.time.get_ticks()

    def pause_timer(self):
        self.start_pause = time.time()
        self.start_tick_pause = pygame.time.get_ticks()
    
    def unpause_timer(self):
        pause_time = time.time() - self.start_pause
        self.start_time += pause_time
        self.last += (pygame.time.get_ticks() - self.start_tick_pause)

