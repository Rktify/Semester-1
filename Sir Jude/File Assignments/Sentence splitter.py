import re
import os

def split(filename):
    file = open(filename, "r")
    r = file.read()
    sentence = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', r)
    for i in sentence:
        print(i)
    file.close()

os.chdir("/Users/Wilbert/Tugas/Sir Jude/File Assignments")
split("text.txt")