import requests


class SendData:
    def __init__(self):
        self.url = "http://127.0.0.1:5000/savedata"

    def send_to_server(self, data):
        try:
            response = requests.post(self.url, json=data, timeout=5)
            if response.status_code == 200:
                print("Sent successfully!")
            else:
                print(f"Error: {response.status_code}, {response.text}")
        except Exception as e:
            print(f"Error: {e}")
