import json

from Yam.JsonPollute import json_check
file = "./simple.json"

dic = set()
with open(file, 'r') as f:
    data = f.read()
    for char in data:
        if char not in dic:
            dic.add(char)

print(dic)
c = '\t'
print(c in dic)

