import os 
import sys 
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DEMO_DIR = BASE_DIR / "file_handling_demo"
DEMO_DIR.mkdir(exist_ok=True)

text_file = DEMO_DIR / "notes.txt"
text_file.touch(exist_ok=True)

with open(text_file, "w", encoding="utf-8") as f:
    f.write("Line 1: Hello, Python File Handling!\n")


with open(text_file, "w", encoding="utf-8") as f:
    f.write("Line 2: The 'w' mode overwrites previous content.\n")


print(text_file)

with open(text_file, "a", encoding="utf-8") as f:
    f.write("Line 3: Appended this new line safely.\n")
    f.writelines(["Line 4: First list item\n", "Line 5: Second list item\n"])

print(text_file)

with open(text_file, "r", encoding="utf-8") as f:
    print("--- Method A: read() [Entire file as a single string] ---")
    entire_content = f.read()
    print(f"Total characters: {len(entire_content)}")
   # print(entire_content)

with open(text_file, "r", encoding="utf-8") as f:
    print("\n--- Method C: readlines() [Returns a list of all lines] ---")
    lines_list = f.readlines()
    print(f"Total lines in list: {len(lines_list)}")

print("\n--- Method D: Iterating directly over the file object (Memory Efficient) ---")
with open(text_file, "r", encoding="utf-8") as f:
    for line_num, line in enumerate(f, start=1):
        if line_num <= 2:  # Print first 2 lines as sample
            print(f"  Line {line_num}: {line.strip()}")

with open(text_file, "r", encoding="utf-8") as f:
    print(f"Initial pointer position: {f.tell()}")
    print(f"Read first 6 bytes: {f.read(6)}")
    print(f"Pointer position after reading 6 bytes: {f.tell()}")
    
    # Move pointer back to the beginning of the file
    f.seek(0)
    print(f"Pointer position after seek(0): {f.tell()}")
    print(f"Read from beginning again: {f.read(25)}")

# Mode 'r+': Read and Write simultaneously without overwriting from scratch
with open(text_file, "r+", encoding="utf-8") as f:
    initial_data = f.read()
    f.write("Line 6: Added via r+ mode pointer at the end.\n")

binary_file = DEMO_DIR / "data.bin"
binary_data = b"\x00\x01\x02\x03\xFF Python Binary Data"

with open(binary_file, "wb") as f:
    f.write(binary_data)

with open(binary_file, "rb") as f:
    raw_bytes = f.read()
    print(f"Read binary data successfully: {raw_bytes[:10]}... (truncated)")

missing_file = DEMO_DIR / "non_existent.txt"

try:
    with open(missing_file, "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print(f"Caught expected error: '{missing_file.name}' does not exist.")
except PermissionError:
    print("Caught error: Permission denied to access this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# modern pathlib shortcuts 

quick_file = DEMO_DIR / "quick_notes.txt"

# Quick write
quick_file.write_text("Written instantly using pathlib write_text()!", encoding="utf-8")

# Quick read
content_quick = quick_file.read_text(encoding="utf-8")
print(f"Pathlib read_text() result -> {content_quick}")

# Check metadata
quick_file = DEMO_DIR / "quick_notes.txt"

# Quick write
quick_file.write_text("Written instantly using pathlib write_text()!", encoding="utf-8")

# Quick read
content_quick = quick_file.read_text(encoding="utf-8")
print(f"Pathlib read_text() result -> {content_quick}")

# Check metadata
if quick_file.exists():
    print(f"File size: {quick_file.stat().st_size} bytes")
    print(f"Is file? {quick_file.is_file()}")


