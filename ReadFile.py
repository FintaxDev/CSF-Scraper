import json

def Json(json_path:str)->dict:
    with open(json_path, "r") as openfile:
        json_data = json.load(openfile)
    return json_data
