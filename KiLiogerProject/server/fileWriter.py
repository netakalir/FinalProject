import os
from datetime import datetime


class FileWriter():
    def send_data(self,data:str,create_directory_if_not_exists:str)->None:
        # print(data, machine_name)
        with open(create_directory_if_not_exists,"a") as f:
            f.write(f"{data}{"\n"}")


    def create_directory_if_not_exists(self,path):
        """
        Creates a directory if it doesn't already exist.

        Args:
            path: The path to the directory.
        """
        try:
            if not os.path.exists(path):
                print(f"Directory '{path}+{datetime.now().strftime('%Y-%m-%d')}' created.")
            # else:
            #     print(f"Directory '{path}' already exists.")
        except:
            pass
        return os.makedirs(path)

# דוגמה לשימוש
# a = FileWriter()
# directory_path = f"C:\\Users\\netan\Desktop\KiLiogerProject\server\\all_data\\{r}\\"}+{datetime.now().strftime('%Y-%m-%d')}"
# a.create_directory_if_not_exists(directory_path)