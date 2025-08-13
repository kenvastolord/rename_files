import os

directory = "./"
files = os.listdir(directory)

print("Files in the Directory: ")

for file in files:
    old_file = os.path.join(directory, file)
    new_file = os.path.join(directory, "new_" + file)
    os.rename(old_file, new_file)
    print(f"rename {file} -> new_{file}")
