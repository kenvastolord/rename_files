import os

directory = "./test/"
files = os.listdir(directory)


prefix = input(
    "Enter the prefix you want to add to the file names (leave empty for no prefix): "
)

suffix = input(
    "Enter the suffix you want to add to the file names (leave empty for no suffix): "
)

for file in files:
    old_file_path = os.path.join(directory, file)

    if os.path.exists(old_file_path) and os.path.isfile(old_file_path):
        filename, ext = os.path.splitext(file)

        new_file_name = f"{prefix + '_' if prefix else ''}{filename}{'_' + suffix if suffix else ''}{ext}"
        new_file_path = os.path.join(directory, new_file_name)

        if old_file_path != new_file_path:
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {old_file_path} -> {new_file_path}")
