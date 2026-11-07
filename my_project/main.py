import file_utils

target_file = "notes.txt"

file_utils.write_text_file(target_file, "Learning how to build custom modules in Python!")

content = file_utils.read_text_file(target_file)
print(f"File Content: {content}")