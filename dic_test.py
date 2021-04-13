import os

path = "./test-merge"
filenames = os.listdir(path)

new_file = open('text_merge.txt', 'w')

for filename in filenames:
    filepath = path + '/' + filename
    for line in open(filepath):
        new_file.writelines(line)
    new_file.write('\n')

new_file.close()