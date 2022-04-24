import pygame
import random
import time
import os
from assets.assets import Assets
from assets.draw import Draw

class Word():

    def __init__(self, canvas, word_file, screen):
        super().__init__()
        
        self.assets = Assets()
        self.draw = Draw(canvas, screen)

        self.font_thaipixel = os.path.join(self.assets.font_dir, "zoo8.ttf")

        self.word_file  = word_file
        self.canvas = canvas
        self.font_small = pygame.font.Font(self.font_thaipixel, 20)

        self.draw.load_font('zoo8.ttf')
        
        self.input_space = pygame.Rect(canvas.get_width()/2, canvas.get_height()/2, 0, 20)
        self.input_space.center
        self.word_correct_count = 0

    def get_new_word(self):
        self.answerWord = open(self.word_file, encoding = 'utf-8').read().splitlines()

        random.seed(time.time())
        self.randNumber = random.randrange(len(self.answerWord))
        self.chosenWord = self.answerWord[self.randNumber]
        self.word = self.chosenWord.split(' ')[0]
        self.meaning = self.chosenWord.split(' ')[1]

    def checkWord(self, user_text):
        if user_text.lower().strip(' ') == self.word:
            self.word_correct_count += 1
            return True
        else:
            return False

    def renderInputBox(self, color, userText):

        self.draw.draw_text_with_outline(35, self.meaning, 'white', self.canvas.get_width()*0.5, self.canvas.get_height()*0.45)

        pygame.draw.rect(self.canvas, 'black', self.input_space)
        pygame.draw.rect(self.canvas, color, self.input_space, 1)

        text_surface = self.font_small.render(userText, False, (255, 255, 255))
        self.canvas.blit(text_surface, (self.input_space.x + 5, self.input_space.y - 5))

        self.input_space.w = max(self.canvas.get_width()/4, text_surface.get_width() + 10)

        self.input_space.center = (((self.canvas.get_width()/2)), self.canvas.get_height()*0.75)

    def reset_word_count(self):
        self.word_correct_count = 0
