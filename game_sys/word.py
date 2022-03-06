from tkinter import CENTER, Canvas
import pygame
import random
import time
import os
from assets.assets import Assets

class Word():

    def __init__(self, canvas, word_file):
        super().__init__()
        
        # self.healthbar = Healthbar(canvas.get_width(), canvas.get_height(), canvas)
        self.assets = Assets()

        self.font_thaipixel = os.path.join(self.assets.font_dir, "zoo8.ttf")

        self.word_file  = word_file
        self.canvas = canvas
        self.font_small = pygame.font.Font(self.font_thaipixel, 20)
        self.font_large = pygame.font.Font(self.font_thaipixel, 30)
        
        self.input_space = pygame.Rect(canvas.get_width()/2, canvas.get_height()/2, 0, 20)
        # self.input_space.center = (canvas.get_width()/2, canvas.get_height()*0.3)
        self.input_space.center
        self.word_correct_count = 0

    def get_new_word(self):
        self.answerWord = open(self.word_file, encoding = 'utf-8').read().splitlines()

        random.seed(time.time())
        self.randNumber = random.randrange(len(self.answerWord))
        self.chosenWord = self.answerWord[self.randNumber]
        self.word = self.chosenWord.split(' ')[0]
        self.meaning = self.chosenWord.split(' ')[1]

        self.answer = self.font_small.render(self.word, False, (255, 255, 255))
        self.answerMeaning = self.font_large.render(self.meaning, False, (255, 255, 255))

        self.answer_rect = self.answer.get_rect(center = (self.canvas.get_width()*0.5, self.canvas.get_height()*0.7))
        self.meaning_rect = self.answerMeaning.get_rect(center = (self.canvas.get_width()*0.5, self.canvas.get_height()*0.5))

    def checkWord(self, user_text):
        if user_text.lower().strip(' ') == self.word:
            self.word_correct_count += 1
            return True
        else:
            return False

    def renderInputBox(self, color, userText):

        pygame.draw.rect(self.canvas, color, self.input_space, 1)

        text_surface = self.font_small.render(userText, False, (255, 255, 255))
        self.canvas.blit(text_surface, (self.input_space.x + 5, self.input_space.y - 5))

        self.input_space.w = max(self.canvas.get_width()/4, text_surface.get_width() + 10)

        self.input_space.center = (((self.canvas.get_width()/2)), self.canvas.get_height()*0.8)

    def reset_word_count(self):
        self.word_correct_count = 0
