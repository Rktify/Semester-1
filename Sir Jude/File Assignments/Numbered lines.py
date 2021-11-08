import os

def main(filename, outname):
    out = open(outname, "w")
    with open(filename, "r") as file:
        lines = file.readlines()
        x = 0
        for i in lines:
            x += 1
            output = (f"{x}. {i}")
            out.writelines(output)
    out.close()

os.chdir("/Users/Wilbert/Tugas/Sir Jude/File Assignments") #Add your directory here
name = input("What is the file name? (in .txt): ") #Enter the text file name (not case-sensitive)
outname = input("Whats ur desired output file name? (in .txt): ") #Enter anything you want cause the program will make a file with this name

main(name, outname)

