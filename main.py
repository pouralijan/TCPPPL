#!/usr/bin/env python3
import os
import sys
import time
import build
import configparser

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileModifiedEvent

config = configparser.ConfigParser()
config.read_file(open(".cpp.notebook.ini"))
APP_EXECUTABLE =  config.get("default", "APP_EXECUTABLE")

os.system("clear")
print("CPP Notebook started")
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            if event.src_path.endswith(".cpp"):
                os.system("clear")
                print("Building ...")
                res = build.build()
                if not res[0]:
                    print("Building [\033[91m{}\x1b[0m]".format(res[1]))
                else:
                    print("Building [\033[92m{}\x1b[0m]".format(res[1]))
                    print("Running ...")
                    os.system("./CPP_NOTEBOOK_BUILD/{}".format(APP_EXECUTABLE))

eh = MyHandler()
observer = Observer()
observer.schedule(eh, path="./src", recursive=False)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
