import os

target_data_path = "./json-valid"
target_texts = []

target_files = os.listdir(target_data_path)
for target_file in target_files:
    if not os.path.isdir(target_file):
        with open(target_data_path +"/" + target_file,'r') as target_f:
            target_data = target_f.read()
            target_texts.append(target_data)

print(target_texts)