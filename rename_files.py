import os

directory = "./"
files = os.listdir(directory)

print("Files in the Directory: ")

for file in files:
    old_file = os.path.join(directory, file)
    if os.path.exists(old_file) and os.path.isfile(old_file):
        new_file = os.path.join(directory, "new_" + file)
        counter = 1
        while os.path.exists(new_file):
            base, ext = os.path.splitext(new_file)
            new_file = f"{base}_{counter}{ext}"
            counter += 1
    else:
        print(f"{file} is either missign or not a valid file")

    os.rename(old_file, new_file)
    print(f"rename {file} -> new_{file}")
