import os

valid_path = "./json-valid"
vald_filenames = os.listdir(valid_path)
valid_file = open('json-valid.txt', 'w')

for filename in vald_filenames:
    filepath = valid_path + '/' + filename
    for line in open(filepath):
        valid_file.writelines(line)
valid_file.close()

invalid_path = "./json-invalid"
invald_filenames = os.listdir(invalid_path)
invalid_file = open("json-invalid.txt", 'w')
for filename in invald_filenames:
    filepath = invalid_path + '/' + filename
    for line in open(filepath):
        invalid_file.writelines(line)
invalid_file.close()
