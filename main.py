import pyautogui
import time


class AutomaticMouseMover:
    def __init__(self):
        self.previous_pos = pyautogui.position()
        self.x_move_direction = 1
        self.y_move_direction = 1

        self.move_mouse_periodically()

    def move_mouse_periodically(self):
        while True:
            self.previous_pos = pyautogui.position()
            time.sleep(2)

            current_pos = pyautogui.position()
            if self.previous_pos == current_pos:
                self.change_move_direction()
                pyautogui.moveRel(self.x_move_direction, self.y_move_direction, duration=0.1)
                self.previous_pos = pyautogui.position()

    def change_move_direction(self):
        if self.x_move_direction == 1:
            self.x_move_direction = -1
        else:
            self.x_move_direction = 1

        if self.y_move_direction == 1:
            self.y_move_direction = -1
        else:
            self.y_move_direction = 1


auto_mover = AutomaticMouseMover()
