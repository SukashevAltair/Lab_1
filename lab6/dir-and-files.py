import os 

#1

files = []
folders = []
path = os.getcwd()
files_and_folders = os.scandir(path)
for entry in files_and_folders:
    if entry.is_dir():
        folders.append(entry)
    elif entry.is_file():
        files.append(entry)
all = files + folders
print(files)
print(folders)
print(all)

#2

p = input()
print("Exists:", os.path.exists(p))
print("Readable:", os.access(p, os.R_OK))
print("Writable:", os.access(p, os.W_OK))
print("Executable:", os.access(p, os.X_OK))

#3

p = input()
if os.path.exists(p):
    print("file exists")
    print("directory:", os.path.dirname(p))
    print("file name:", os.path.basename(p))
else:
    print("file does not exist")

#4

with open("text.exe","r") as f:
    neshe = 0
    for _ in f:
        neshe +=1
print(neshe)

#5

students = ['Altair','Ansar','Timur']
with open("text.exe","a") as f:
    f.write("\n".join(students) + "\n")

#6

import string
for i in string.ascii_uppercase:
    with open(f"{i}.txt", "w") as f:
        f.write(f"This is {i} file")

#7

with open("text.exe","r") as d:
    with open("text1.exe","w") as f:
        f.write(d.read())

#8

p = input()
if os.path.exists(p) and os.path.isfile(p):
    print("file exists")
    print("Readable:", os.access(p, os.R_OK))
    print("Writable:", os.access(p, os.W_OK))
    if os.access(p, os.W_OK):
        os.remove(p)
        print(f"File {p} has been deleted.") 
    else:
        print(f"No permission to delete {p}.")
else:
    print(f"File {p} not found.")