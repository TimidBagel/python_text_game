import json

def write_file(file_path, data):
    file = open(file_path, "w")
    json.dump(data, file)
    file.close()

def read_file(file_path):
    file = open(file_path, "r")
    data = json.load(file)
    file.close()
    return data