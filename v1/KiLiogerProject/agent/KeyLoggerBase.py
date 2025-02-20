from abc import ABC , abstractmethod


class IKeyLogger:
    @abstractmethod
    def start_logging(self)->None:
        pass

    @abstractmethod
    def stop_logging(self)->None:
        pass

    @abstractmethod
    def get_logged_keys(self)->list[str]:
        pass


class IFileWriter:
    @abstractmethod
    def send_data(self,data:str,machine_name:str)->None:
        pass



