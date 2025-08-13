import os

directory = "./"
files = os.listdir(directory)

print("Files in the Directory: ")

for file in files:
    old_file = os.path.join(directory, file)
    if os.path.exists(old_file) and os.path.isfile(old_file):
        print(f"the {file} exists and is a valid file")
    else:
        print(f"{file} is either missign or not a valid file")

    new_file = os.path.join(directory, "new_" + file)
    os.rename(old_file, new_file)
    print(f"rename {file} -> new_{file}")
