import json
import os
import codecs


def json_check(json_str, file):
    try:
        json.loads(json_str)
    except json.JSONDecodeError:
        print("invalid")
    else:
        print("valid")

def read_files(files):
    for file in files:
        if not os.path.isdir(file):
            with open(path+ "/" + file, encoding="utf8", errors='ignore') as f:
            # f = open(path + "/" + file,'r')
            #     iter_f = iter(f)
                str = f.read()
                # for line in iter_f:
                #     str = str + line
                json_check(str,file)


if __name__ == '__main__':
    path = "/Users/shuhangyan/Desktop/ECE750-043/Project/json-valid"
    files = os.listdir(path)
    read_files(files)
