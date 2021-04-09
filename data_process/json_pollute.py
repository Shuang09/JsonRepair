import os

from JsonPollute import JsonPollute

def read_files(files):
    for file in files:
        if not os.path.isdir(file):
            f = open(path + "/" + file,'r')
            iter_f = iter(f)
            str = ""
            for line in iter_f:
                str = str + line
            file_pollute(file, str)


def file_pollute(file,data):

    jsp = JsonPollute(data, pollute_rate= 3)
    jsp.pollute([0,1,1,1])
    ans = jsp.pollute()
    print(file, ans[1])

if __name__ == '__main__':
    path = "../json-valid"
    files = os.listdir(path)
    read_files(files)
