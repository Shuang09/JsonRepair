
import os
# dir = "./target_json"
# list = os.listdir(dir) # dir is your directory path
# number_files = len(list)
# print (number_files)

file = "./target_json.txt"

i = 0

with open(file, 'r') as f:
    lines = f.read().split("\n")
    print(len(lines))
    # for line in lines [: min(50, len(input_lines) - 1)]:
    #     i+1;
# print(i)



