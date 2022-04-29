from utils.mover import move_file
from config.json_reader import folder_data_target, type_data
import glob
import time
import argparse

parser = argparse.ArgumentParser(description="Move files from downloads to there correct locations")
parser.add_argument("run_type", type=str, help="run the sorter multiple times")
args = parser.parse_args()

def main(argument):
    print(argument)
    loop = True
    
    if argument == "run":
        print("running (to exit press ctrl + c)")
    elif argument == "run-once":
        print("running once")
    else:
        print("invalid type")
        loop = False
    
    while (loop):
        try:
            main_source = str(folder_data_target["Path Folder"])
            
            for string in type_data:
                main_destination = folder_data_target[string + " Folder"]
                file_type = type_data[string]
                found_files = glob.glob(main_source + file_type)

                for file in found_files:
                    file = file.split("/")
                    file = file[len(file) - 1]

                    move_file(main_source + file, main_destination + file)
        
            time.sleep(5)
        
            if argument == "run":
                print("update (to exit press ctrl + c)")
                continue
            else:
                break
        except KeyboardInterrupt:
            print("\nkeyboard interrupt detected exiting program")
            loop = False

if __name__ == "__main__":
    main(args.run_type)