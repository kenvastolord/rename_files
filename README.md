# Rename Files Utility

A simple Python script to batch rename files in a folder by adding a **custom prefix**, **suffix**, and optionally **filtering by file extension**. Hidden files (starting with a dot, e.g., `.DS_Store`) are ignored by default.

---

## 🚀 Features

- ✅ Add a **prefix** to file names
- ✅ Add a **suffix** to file names
- ✅ Filter files by extension (e.g., `.jpg`, `.txt`)
- ✅ Automatically ignores **hidden files**
- ✅ Preserves original file extensions
- ✅ Prevents renaming if the filename doesn’t change

---

## 📂 Project Structure

Rename_Files/
├── test/ # Folder containing files to rename
├── rename_files.py # Main script
└── README.md # Documentation

---

## ⚙️ How It Works

1. The script scans the `./test/` folder.
2. It filters out:
   - Hidden files (`.gitignore`, `.DS_Store`, etc.)
   - Files not matching the specified extension (if provided).
3. It renames each valid file by applying the given **prefix** and/or **suffix**.

---

## 🧑‍💻 Usage

### 🛠 Requirements

- Python 3.x
- No external libraries required

---

### ▶️ Run the script

```bash
python rename_files.py
```
