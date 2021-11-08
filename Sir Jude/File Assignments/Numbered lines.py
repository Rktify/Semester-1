import os

def main(filename):
    out = open("out.txt", "w")
    with open(filename, "r") as file:
        lines = file.readlines()
        x = 0
        for i in lines:
            x += 1
            output = (f"{x}. {i}")
            out.writelines(output)
    out.close()

os.chdir("/Users/Wilbert/Tugas/Sir Jude/File Assignments") #Add your directory here
name = input("What is the file name (in .txt): ") #Enter the text file name (not case-sensitive)

main(name)

