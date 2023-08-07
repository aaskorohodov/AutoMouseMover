import threading

from infi.systray import SysTrayIcon

from mouse_mover import AutomaticMouseMover


class Trayer(SysTrayIcon):
    """Responsible for building an icon in system-tray

    Attributes:
        idle_time: Idle-time in seconds, after which mouse will be moved
        keep_running: Thread-communicator object"""

    def __init__(self, idle_time: int = 600):
        """Starts this all up

        Args:
            idle_time: Idle-time in seconds, after which mouse will be moved"""

        self.idle_time: int         = idle_time
        self.keep_running: dict     = {'keep_running': True}

        self.start_mover()

        logo = 'media/cursor.ico'
        system_tray_name = 'Mover'
        menu_options = None
        super().__init__(logo, system_tray_name, menu_options, on_quit=self._quit)
        self.start()

    def start_mover(self) -> None:
        """Creates an instance of a mover in separate thread"""

        mover_thread = threading.Thread(
            target=AutomaticMouseMover,
            args=(self.keep_running, self.idle_time),
            daemon=True)
        mover_thread.start()

    def _quit(self, _):
        """Custom action. Being called automatically by systray on exit.

        Args:
            _: Trayer (self's class), provided by systray"""

        self.keep_running['keep_running'] = False
        print('I am out, goodbye :*')
