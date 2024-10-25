import os


def file_recursion(path, size=0, max_file_size=(0, '')):
    files = []
    for entry in os.listdir(path):
        if entry.startswith('.') or entry.startswith("node_modules"):  # filter hidden folder
            continue
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            subdir_files, size, max_file_size = file_recursion(
                full_path, size, max_file_size)
            files.extend(subdir_files)
            size = size
            max_file_size = max_file_size
        else:
            folder_name = os.path.basename(os.path.dirname(full_path))
            size += os.path.getsize(full_path)
            maxSize, _ = max_file_size
            if os.path.getsize(full_path) > int(maxSize):
                max_file_size = (os.path.getsize(full_path), full_path)
            files.append((folder_name, entry))
    return (files, size, max_file_size)


def format_size(bytesize):
    if bytesize < 1024:
        return f"{bytesize:.2f} bytes"
    if bytesize < 1024 ** 2:
        return f"{bytesize / 1024:.2f} kb"
    if bytesize < 1024 ** 3:
        return f"{bytesize / 1024 **2:.2f} mb"
    if bytesize < 1024 ** 4:
        return f"{bytesize / 1024 **3:.2f} gb"


path = "/Users/christiannogueras/Documents/Datacamp"
path2 = '/Users/christiannogueras/Documents'
result, sum, max_size = file_recursion(path2)
print(f"file size is: {format_size(sum)}")
print(f"max file size: {format_size(max_size[0])}, file {max_size[1]}")
