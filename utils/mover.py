import os
import shutil

def move_file(source, destination):
    source = str(source)
    destination = str(destination)

    try:
        if os.path.exists(destination):
            print("There is already a file here")
        else:
            shutil.move(source, destination)
            print(source + " was moved")
    except FileNotFoundError:
        print(source + " was not found")