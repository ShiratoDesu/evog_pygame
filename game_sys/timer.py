import pygame
import time


class Time():
    def __init__(self):
        super().__init__()
        self.time_marker = 0
        self.current_time = 0
        self.start_time = time.time()
        self.elasped_time = 0

    def setTimeMarker(self):
        self.time_marker = pygame.time.get_ticks()

    def getTimeDiff(self):

        self.current_time = pygame.time.get_ticks()
        self.time_diff = self.current_time - self.time_marker

        print(self.time_diff)

    def get_elapsed_time(self):
        self.elasped_time = time.time() - self.start_time
    
    def reset_start_time(self):
        self.start_time = time.time()
