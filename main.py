from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
import shutil

if not os.path.isdir('exefile'):
    try:
        os.mkdir("exefile")
    except OSError as error:
        print(error)
else:
    pass


class MoveFile(FileSystemEventHandler):
    def on_created(self, event):
        for filename in os.listdir():
            f_name, f_ext = os.path.splitext(filename)
            if f_ext == ".exe":
                time.sleep(5)
                shutil.move(os.path.join(os.getcwd(), filename), os.path.join(os.getcwd(), "exefile", filename))

            else:
                pass


observer = Observer()
observer.schedule(MoveFile(), os.getcwd(), recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join
