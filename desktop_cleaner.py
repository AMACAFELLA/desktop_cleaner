import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(desktop_path):
            if filename == '.DS_Store' or filename == 'desktop_cleaner':
                continue
            src_path = os.path.join(desktop_path, filename)
            file_ext = os.path.splitext(filename)[1][1:] # get the file extension
            ext_folder = os.path.join(target_folder, file_ext) # create a path to the folder with the name of the file extension

            # check if the folder exists, if not, create it
            if not os.path.exists(ext_folder):
                os.makedirs(ext_folder)

            dst_path = os.path.join(ext_folder, filename)
            if os.path.exists(dst_path):
                new_dst_file_name = "{}_{}".format(int(time.time()), filename)
                dst_path = os.path.join(ext_folder, new_dst_file_name)

            shutil.move(src_path, dst_path)

desktop_path = os.path.expanduser("~/Desktop")
target_folder = os.path.expanduser("~/Documents")
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, desktop_path, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
