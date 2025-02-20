import datetime

from key_listener import Listener


class FileWriter:

    def __init__(self, name_file):
        # שם הקובץ אליו מתווספים התווים
        self.file= name_file


    def time(self):
        now = datetime.datetime.now()
        self.now = str(now.strftime("%m-%d-%Y %H:%M "))
        return self.now


    def up_to_file(self, data)-> None :
        with open(self.file, 'a') as file:
            file.write(f'[{self.time()}]:{str(data)} \n')



