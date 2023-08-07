import pyautogui
import time


class AutomaticMouseMover:
    """Responsible for moving you mouse after some idle time

    Attributes:
        previous_pos: Stores previous detected mouse position
        x_move_direction: Stores the direction, in which mouse should be moved in X-axis
        y_move_direction: Stores the direction, in which mouse should be moved in Y-axis
        idle_time: Idle-time in seconds, after which mouse will be moved"""

    def __init__(self, idle_time: int = 600):
        """Launches this all up

        Args:
            idle_time: Time, after which mouse will be moved, in case of idle (seconds)"""

        self.previous_pos = pyautogui.position()
        self.x_move_direction = 1
        self.y_move_direction = 1
        self.idle_time = idle_time

        self.move_mouse_periodically()

    def move_mouse_periodically(self) -> None:
        """Endless cycle, that moves mouse a bit occasionally"""

        while True:
            self.previous_pos = pyautogui.position()
            time.sleep(self.idle_time)

            current_pos = pyautogui.position()
            if self.previous_pos == current_pos:
                self.change_move_direction()
                pyautogui.moveRel(self.x_move_direction, self.y_move_direction, duration=0.1)
                self.previous_pos = pyautogui.position()

    def change_move_direction(self) -> None:
        """Changes mouse-move direction onto opposite, so that mouse will not move all over the screen"""

        if self.x_move_direction == 1:
            self.x_move_direction = -1
        else:
            self.x_move_direction = 1

        if self.y_move_direction == 1:
            self.y_move_direction = -1
        else:
            self.y_move_direction = 1
