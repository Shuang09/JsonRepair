# To valid json files
import os
import json

def read_files(files):
    for file in files:
        if not os.path.isdir(file):
            f = open(path + "/" + file,'r')
            iter_f = iter(f)
            str = ""
            for line in iter_f:
                str = str + line

            json_check(str, file)


def json_check(json_str, file):
    try:
        json.loads(json_str)
    except json.JSONDecodeError:
        invalid_json.append(file)
    else:
        valid_json.append(file)


if __name__ == '__main__':
    path = "/Users/shuhangyan/Desktop/ECE750-043/Project/json-invalid-single"
    files = os.listdir(path)
    invalid_json = []
    valid_json = []

    read_files(files)
    print(len(invalid_json))
    print(len(valid_json))
    #print(str(invalid_json)[1:-1])

