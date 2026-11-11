import json

class ReadJson:

    def read_jsonfile(self):
        with open(r"C:\Users\user\Downloads\Demo_project\Utilities\data.json","r") as file:
            data=json.load(file)
        return data

