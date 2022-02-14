import pygame
from states.state import State
from assets.sound import Sound
from assets.draw import Draw


class Menu(State):
    def __init__(self, game) -> None:
        State.__init__(self, game)
        self.surface = self.game.game_canvas
        self.box_actions = {
            "escape": False,
            "enter": False,
            "right": False,
            "left": False
        }
        self.box_text = [
            [6, "Yes", "black", -20, 10],
            [6, "No", "black", 20, 10]
        ]
        self.cursor_index = 0

    def update(self, delta_time, actions):
        pass

    def render(self, surface):
        pass

    def play_cursor_sound(self):
        self.sound.play_sound(self.sound.cursor_sound)

    def play_confirm_sound(self):
        self.sound.play_sound(self.sound.confirm_sound)

    def play_back_sound(self):
        self.sound.play_sound(self.sound.back_sound)

    def play_error_sound(self):
        self.sound.play_sound(self.sound.error_sound)

    def check_confirm(self, header_text):
        need_confirm = True
        confirm = False
        self.box_text[0][0] += 2
        self.box_text[0][2] = "red"
        self.cursor_index = 0
        while need_confirm:
            self.get_event()
            if self.box_actions["enter"] == True:
                if self.cursor_index == 0:
                    self.play_confirm_sound()
                    confirm = True
                    need_confirm = False
                if self.cursor_index == 1:
                    self.play_back_sound()
                    need_confirm = False
            if self.box_actions["escape"] == True:
                self.play_back_sound()
                need_confirm = False
            self.move_cursor(self.box_actions)
            self.draw_confirm_box(self.canvas, header_text)
            self.update_screen()
            self.reset_key()
        return confirm

    def draw_confirm_box(self, surface, header_text):
        middle_x, middle_y = self.canvas_w / 2, self.canvas_h / 2
        # draw box
        box = pygame.Surface((100, 60))
        box.fill("gray")
        box_rect = box.get_rect(
            center=(self.canvas_w / 2, self.canvas_h / 2))
        surface.blit(box, box_rect)
        # draw text
        self.draw.draw_text(surface, 10, header_text, "yellow",
                            middle_x, middle_y - 10, self.anti_aliasing_text)
        for choice in self.box_text:
            self.draw.draw_text(surface, choice[0], choice[1], choice[2],
                                middle_x + choice[3], middle_y + choice[4], self.anti_aliasing_text)

    def get_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.exit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.box_actions["escape"] = True
                if event.key == pygame.K_RETURN:
                    self.box_actions["enter"] = True
                if event.key == pygame.K_RIGHT:
                    self.box_actions["right"] = True
                if event.key == pygame.K_LEFT:
                    self.box_actions["left"] = True

    def move_cursor(self, actions):
        if actions["right"]:
            self.cursor_index = (self.cursor_index + 1) % len(self.box_text)
            self.play_cursor_sound()
        elif actions["left"]:
            self.cursor_index = (self.cursor_index - 1) % len(self.box_text)
            self.play_cursor_sound()
        for choice in self.box_text:
            choice[0] = 6
            choice[2] = "black"
        self.box_text[self.cursor_index][0] += 2
        self.box_text[self.cursor_index][2] = "red"

    def reset_key(self):
        for action in self.box_actions:
            self.box_actions[action] = False

    def update_screen(self):
        self.screen.blit(pygame.transform.scale(
            self.canvas, (self.screen_w, self.screen_h)), (0, 0))
        pygame.display.flip()
