import os

def hapax(s):
    word = s.split()
    for i in word:
        if i in end:
            end[i] += 1
        else:
            end[i] = 1
    for i in end:
        if end[i] == 1:
            print(i)


os.chdir("/Users/Wilbert")
file = open("Book.txt", "r")

s = file.read().lower()
punc = '''!()-[]{};:'"\,<>./™?˜@#$â%^&*_”~€'''
for element in s:
    if element in punc:
        s = s.replace(element, "")
end = dict()
end = hapax(s)

file.close()