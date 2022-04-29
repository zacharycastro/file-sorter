import json

with open("config/folder.json") as json_folder_data:
    folder_data = json.load(json_folder_data)
    
with open("config/type.json") as json_type_data:
    type_data = json.load(json_type_data)
