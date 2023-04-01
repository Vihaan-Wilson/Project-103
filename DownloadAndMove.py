import sys
import time
import random
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VS
#"C:\Users\Vihaan Patil\Dropbox\My PC (Vihaan-Laptop)\Downloads"
#C:\Python work\Class 103
from_dir = "C:/Users/Vihaan Patil/Dropbox/My PC (Vihaan-Laptop)/Downloads"
to_dir = "C:/Python work/Class 103"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.src_path} is created!")
        print(event.src_path)
        name,extension=os.path.splitext(event.src_path)
        for key, value in dir_tree.items(): 
            time.sleep(1) 
            if extension in value: 
                file_name = os.path.basename(event.src_path) 
                print("Downloaded " + file_name) 
                path1 = from_dir + '/' + file_name 
                path2 = to_dir + '/' + key 
                path3 = to_dir + '/' + key + '/' + file_name 
                if os.path.exists(path2): 
                    print("Directory Exists...") 
                    print("Moving " + file_name + "....") 
                    shutil.move(path1, path3) 
                    time.sleep(1) 
                else: print("Making Directory...") 
                os.makedirs(path2) 
                print("Moving " + file_name + "....") 
                shutil.move(path1, path3) 
                time.sleep(1)
    
    def on_deleted(self, event):
         print(f"It's look like {event.src_path} is deleted!")

# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

try:
    while True:
        time.sleep(3)
        print("running...")
except KeyboardInterrupt:
        print("stopped")
        observer.stop()
    