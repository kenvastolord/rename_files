import os

directory = "./"
files = os.listdir(directory)

print("Directory's Files: ")

for file in files:
    print(file)
