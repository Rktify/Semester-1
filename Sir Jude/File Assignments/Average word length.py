import os

def wordcount(s):
    word = s.split()
    x = 0
    y = 0
    for i in word:
        y += len(i) #The character count
        x += 1 #The word count
    print(f"The word count is {x}")
    print(f"The character count is {y}")
    ave = y//x
    print(f"The average characters per word is {ave}")


os.chdir("/Users/Wilbert")
name = input("What is the file name? (in .txt): ") #Enter the text file name (not case-sensitive)
file = open(name, "r")

s = file.read().lower()
punc = '''!()-[]{};:'"\,<>./™?˜ã©@#$ªâ%^&*_”~€''' #This is for me removing all of the odd characters and punctutations
for element in s:
    if element in punc:
        s = s.replace(element, "")
all = dict()
all = wordcount(s)