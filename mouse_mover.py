import pyautogui
import time

from pyautogui import Point


class AutomaticMouseMover:
    """Responsible for moving you mouse after some idle time

    Attributes:
        previous_pos: Stores previous detected mouse position
        x_move_direction: Stores the direction, in which mouse should be moved in X-axis
        y_move_direction: Stores the direction, in which mouse should be moved in Y-axis
        idle_time: Idle-time in seconds, after which mouse will be moved
        keep_running: Thread-communicator object, that will shut down this thread, when needed
        no_movement_for: How much time passed, since last mouse-move"""

    def __init__(self, keep_running: dict, idle_time: int = 600):
        """Launches this all up

        Args:
            keep_running: Thread-communicator object
            idle_time: Time, after which mouse will be moved, in case of idle (seconds)"""

        self.previous_pos: Point    = pyautogui.position()
        self.x_move_direction: int  = 1
        self.y_move_direction: int  = 1
        self.idle_time: int         = idle_time
        self.keep_running: dict     = keep_running
        self.no_movement_for: int   = 0

        self.move_mouse_periodically()

    def move_mouse_periodically(self) -> None:
        """Endless cycle, that moves mouse a bit occasionally"""

        # Checking, if trayer is still running (otherwise User has closed the app and this thread should end)
        while self.keep_running['keep_running']:

            '''Checking thread-communicator each second. If not doing this, and simply sleep for self.idle_time => 
            this thread will be active, till idle time os over, even after User will close this app in sys-tray.'''
            if self.no_movement_for < self.idle_time:
                time.sleep(1)
                self.no_movement_for += 1

            else:
                self.no_movement_for = 0
                current_pos = pyautogui.position()
                if self.previous_pos == current_pos:
                    self.change_move_direction()
                    pyautogui.moveRel(self.x_move_direction, self.y_move_direction, duration=0.1)
                    pyautogui.leftClick()
                self.previous_pos = pyautogui.position()

    def change_move_direction(self) -> None:
        """Changes mouse-move direction onto opposite, so that mouse will not move all over the screen"""

        if self.x_move_direction == 2:
            self.x_move_direction = -2
        else:
            self.x_move_direction = 2

        if self.y_move_direction == 2:
            self.y_move_direction = -2
        else:
            self.y_move_direction = 2
