import pygame
from states.state import State


class Menu(State):
    def __init__(self, game) -> None:
        State.__init__(self, game)
        self._box_actions = {
            "escape": False,
            "enter": False,
            "right": False,
            "left": False
        }
        self._box_text = [
            [6, "Yes", "gray", -20, 10],
            [6, "No", "gray", 20, 10]
        ]
        self._cursor_index = 0

    def update(self, delta_time, actions):
        super().update(delta_time, actions)

    def render(self, surface):
        pass

    def update_cursor(self, actions):
        pass

    def transition_state(self):
        pass

    def play_cursor_sound(self):
        self.sound.play_sound(self.sound.cursor_sound)

    def play_confirm_sound(self):
        self.sound.play_sound(self.sound.confirm_sound)

    def play_back_sound(self):
        self.sound.play_sound(self.sound.back_sound)

    def play_error_sound(self):
        self.sound.play_sound(self.sound.error_sound)

    def check_confirm(self, header_text, size=10):
        need_confirm = True
        confirm = False
        self._box_text[0][0] += 2
        self._box_text[0][2] = "black"
        self._cursor_index = 0
        while need_confirm:
            self._get_event()
            if self._box_actions["enter"] == True:
                if self._cursor_index == 0:
                    self.play_confirm_sound()
                    confirm = True
                    need_confirm = False
                if self._cursor_index == 1:
                    self.play_back_sound()
                    need_confirm = False
            if self._box_actions["escape"] == True:
                self.play_back_sound()
                need_confirm = False
            self._move_cursor(self._box_actions)
            self._draw_confirm_box(header_text, size)
            self._update_screen()
            self._reset_key()
        return confirm

    def _draw_confirm_box(self, header_text, size):
        middle_x, middle_y = self.CANVAS_W / 2, self.CANVAS_H / 2
        # draw box
        box = pygame.Surface((100, 60))
        box.fill("white")
        box_rect = box.get_rect(center=(middle_x, middle_y))
        self.canvas.blit(box, box_rect)
        # draw text
        self.draw.draw_text(size, header_text, "black",
                            middle_x, middle_y - 10)
        for choice in self._box_text:
            self.draw.draw_text(
                choice[0], choice[1], choice[2], middle_x + choice[3], middle_y + choice[4])

    def _get_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.exit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._box_actions["escape"] = True
                if event.key == pygame.K_RETURN:
                    self._box_actions["enter"] = True
                if event.key == pygame.K_RIGHT:
                    self._box_actions["right"] = True
                if event.key == pygame.K_LEFT:
                    self._box_actions["left"] = True

    def _move_cursor(self, actions):
        if actions["right"]:
            self._cursor_index = (self._cursor_index + 1) % len(self._box_text)
            self.play_cursor_sound()
        elif actions["left"]:
            self._cursor_index = (self._cursor_index - 1) % len(self._box_text)
            self.play_cursor_sound()
        for choice in self._box_text:
            choice[0] = 6
            choice[2] = "gray"
        self._box_text[self._cursor_index][0] += 2
        self._box_text[self._cursor_index][2] = "black"

    def _reset_key(self):
        for action in self._box_actions:
            self._box_actions[action] = False

    def _update_screen(self):
        self.screen.blit(pygame.transform.scale(
            self.canvas, (self.screen_w, self.screen_h)), (0, 0))
        pygame.display.flip()
